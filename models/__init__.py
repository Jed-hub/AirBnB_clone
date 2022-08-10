from models.engine import file_storage
"""Init file for resources initialisation"""

storage = file_storage.FileStorage()
storage.reload()
