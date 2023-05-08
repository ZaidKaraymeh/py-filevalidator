import unittest
from pathlib import Path
from validators import Validator, FileValidator


class TestValidator(unittest.TestCase):

    def test_IsNullOrEmpty(self):
        validator = Validator()
        self.assertTrue(validator.IsNullOrEmpty(
            ""), "IsNullOrEmpty should return True for an empty string.")
        self.assertTrue(validator.IsNullOrEmpty(None),
                        "IsNullOrEmpty should return True for None.")
        self.assertFalse(validator.IsNullOrEmpty(
            "test"), "IsNullOrEmpty should return False for a non-empty string.")


class FileValidatorTest(unittest.TestCase):

    def setUp(self):
        self.validator = FileValidator()

    def test_is_max_size(self):
        small_file = Path("validator\misc\logo.jpg")
        large_file = Path("validator\misc\logo.jpg")
        self.assertTrue(self.validator.is_max_size(small_file))
        self.assertFalse(self.validator.is_max_size(large_file))

    def test_is_file_name_pattern(self):
        valid_name = "example_file.pdf"
        invalid_name = "example_file<>?|.pdf"
        self.assertTrue(self.validator.is_file_name_pattern(valid_name))
        self.assertFalse(self.validator.is_file_name_pattern(invalid_name))

    def test_is_allowed_extension(self):
        allowed_file = "example_file.pdf"
        not_allowed_file = "example_file.txt"
        self.assertTrue(self.validator.is_allowed_extension(allowed_file))
        self.assertFalse(self.validator.is_allowed_extension(not_allowed_file))

    def test_validate(self):
        valid_file = Path("validator\misc\logo.jpg")
        invalid_file = Path("validator\misc\logo.jpg")
        self.assertTrue(self.validator.validate(valid_file))
        self.assertFalse(self.validator.validate(invalid_file))


if __name__ == "__main__":
    unittest.main()
