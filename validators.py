
import sys
from pathlib import Path
import re

sys.path.insert(0, str(Path(__file__).resolve().parent))

class Validator:
    """Base class for all validators."""

    def __init__(self):
        pass

    def __call__(self, value: str) -> str:
        return value.upper()
    
    def __repr__(self):
        return f"Validator({self.message!r})"
    
    def __str__(self):
        return f"Validator({self.message!s})"
    
    def IsNullOrEmpty(self, value: str) -> bool:
        return value is None or not value 


class FileValidator(Validator):
    """Validates a file path."""

    def __init__(
            self, 
            max_size: int = 3000, 
            file_name_pattern: str = r'^[a-zA-Z0-9-_ .]+$', 
            allowed_extensions: list = ["pdf"]):
        
        self.max_size = max_size
        self.file_name_pattern = file_name_pattern
        self.allowed_extensions = allowed_extensions

    def __call__(self, value: str) -> str:
        if self.IsNullOrEmpty(value):
            raise ValueError(self.message)
        return value
    
    def is_max_size(self, value: str) -> bool:
        return Path(value).stat().st_size <= self.max_size
    

    def is_file_name_pattern(self, file_name: str) -> bool:
        return bool(re.match(self.file_name_pattern, file_name))
    
    def is_allowed_extension(self, file_name: str) -> bool:
        return Path(file_name).suffix[1:] in self.allowed_extensions
    
    def validate(self, file) -> bool:
        return self.is_max_size(file.name) and self.is_file_name_pattern(file.name) and self.is_allowed_extension(file.name)


# file = open(".misc/Group 15.jpg", "r")
# file_validator = FileValidator()
# file_validator.validate(file)