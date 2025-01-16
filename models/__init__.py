__all__ = ["base_model", "file_storage"]

# Import the submodules
from . import base_model
from .engine.file_storage import FileStorage

# Create a unique FileStorage instance for your application
storage = FileStorage()
storage.reload()