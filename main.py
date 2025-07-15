import sys
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function
from prompts import system_prompt


def main():
    load_dotenv()
    
    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
        
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    
    user_prompt = " ".join(args)
    
    if verbose:
        print(f"User prompt: {user_prompt}\n")
        
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    i = 0
    while i < 20:
        try:
            response = generate_content(client, messages, verbose)
            i += 1
            if not response.function_calls:
                print(response.text)
                break
        except Exception as e:
            print(f"Error: {e}")
    
    print(response.text)


def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
),
    )
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    
    for candidate in response.candidates:
        messages.append(candidate.content)

    if not response.function_calls:
        return response

    function_call_results = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if not function_call_result.parts[0].function_response.response:
            raise Exception(f"Function call failed: {function_call_part.name}")
        
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        
        function_call_results.append(function_call_result.parts[0])
        
    actual_results = types.Content(
        role="tool",
        parts=function_call_results,
    )    
    
    messages.append(actual_results)
    return response

if __name__ == "__main__":
    main()
