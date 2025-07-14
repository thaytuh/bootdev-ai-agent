import unittest
from functions.get_files_info import get_files_info


class TestGetFilesInfo(unittest.TestCase):
    def test_get_files_info(self):
        result = get_files_info("calculator",
                                ".")
        print(result)
    
    def test_get_files_info_pkg(self):
        result = get_files_info("calculator",
                                "pkg")
        print(result)
        
    def test_get_files_info_error(self):
        result = get_files_info("calculator",
                                "/bin")
        print(result)
        
    def test_get_files_info_above_working_dir(self):
        result = get_files_info("calculator",
                                "../")
        print(result)
    
if __name__ == "__main__":
    unittest.main()