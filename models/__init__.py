# models/__init__.py
# we include this init file to make the directory a module
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
