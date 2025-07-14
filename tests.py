import unittest
from functions.write_file import write_file


class TestGetFilesInfo(unittest.TestCase):
    def test_write_file(self):
        result = write_file("calculator",
                            "lorem.txt",
                            "wait, this isn't lorem ipsum")
        print(result)
    
    def test_write_file_new(self):
        result = write_file("calculator",
                            "pkg/morelorem.txt",
                            "lorem ipsum dolor sit amet")
        print(result)
    
    def test_write_file_error(self):
        result = write_file("calculator",
                            "/tmp/temp.txt",
                            "this should not be allowed")
        print(result)

if __name__ == "__main__":
    unittest.main()