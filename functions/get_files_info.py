import os

def get_files_info(working_directory, directory=None):
    path = os.path.join(working_directory, directory)
    if directory != "." and directory not in os.listdir(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(path):
        return f'Error: "{directory}" is not a directory'
    
    files = os.listdir(path)
    file_list = []
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            file_list.append(f"- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir=True")
        else:
            file_list.append(f"- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir=False")

    return "\n".join(file_list)


# - README.md: file_size=1032 bytes, is_dir=False
# - src: file_size=128 bytes, is_dir=True
# - package.json: file_size=1234 bytes, is_dir=False