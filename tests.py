import unittest
from functions.run_python import run_python_file


class TestRunPythonFile(unittest.TestCase):
    def test_run_python_file(self):
        result = run_python_file("calculator",
                                 "main.py")
        print(result)
    
    def test_run_python_file_tests(self):
        result = run_python_file("calculator",
                                 "tests.py")
        print(result)
        
    def test_run_python_file_error(self):
        result = run_python_file("calculator",
                                 "../main.py")
        print(result)
        
    def test_run_python_file_nothing(self):
        result = run_python_file("calculator",
                                 "nonexistent.py")
        print(result)

if __name__ == "__main__":
    unittest.main()