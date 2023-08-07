import unittest
import os
from suraj_vault import suraj_Vault

class TestMyClass(unittest.TestCase):
    def setUp(self):
        # Set up any necessary test fixtures
        self.my_class = suraj_Vault()
        self.my_class.files = ['file1.txt.aes', 'file2.txt']
        self.my_class.hid_dir = '/path/to/hid_dir/'
        self.my_class.key = b'myencryptionkey'
        self.my_class.buffer_size = 64

    def tearDown(self):
        # Clean up after each test
        pass

    def test_del_file_decrypt_and_remove_aes(self):
        # Test that a .aes file is decrypted and removed
        index = 0  # Index of the .aes file in the list
        filename_with_ext = self.my_class.files[index]
        vaultpath = self.my_class.hid_dir + filename_with_ext
        filename = filename_with_ext[:-4]

        # Create a dummy .aes file for testing
        with open(vaultpath, 'w') as file:
            file.write('encrypted content')

        # Call the function being tested
        self.my_class.del_file(index)

        # Assert that the .aes file is decrypted and removed
        self.assertFalse(os.path.exists(vaultpath))
        self.assertTrue(os.path.exists(filename))

        # Clean up the created file
        os.remove(filename)

    def test_del_file_copy_and_remove_non_aes(self):
        # Test that a non-.aes file is copied and removed
        index = 1  # Index of the non-.aes file in the list
        filename_with_ext = self.my_class.files[index]
        vaultpath = self.my_class.hid_dir + filename_with_ext

        # Create a dummy file for testing
        with open(vaultpath, 'w') as file:
            file.write('file content')

        # Call the function being tested
        self.my_class.del_file(index)

        # Assert that the file is copied and removed
        self.assertFalse(os.path.exists(vaultpath))
        self.assertTrue(os.path.exists(filename_with_ext))

        # Clean up the created file
        os.remove(filename_with_ext)


if __name__ == '__main__':
    unittest.main()
