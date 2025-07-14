import unittest
from functions.get_file_content import get_file_content


class TestGetFilesInfo(unittest.TestCase):
    def test_get_file_content_main(self):
        result = get_file_content("calculator", "main.py")
        print(result)
        
    def test_get_file_content_calculator(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)
        
    def test_get_file_content_error(self):
        result = get_file_content("calculator", "/bin/cat")
        print(result)

if __name__ == "__main__":
    unittest.main()