from eventsourcing.application import Application
from typing import Dict, List
from bookmarks.domain import BookmarkCollection

# Use SQLite as a persistent store of data instead of the default
# transient, in-memory store.
import os
os.environ["INFRASTRUCTURE_FACTORY"] = "eventsourcing.sqlite:Factory"
os.environ["SQLITE_DBNAME"] = "data/bookmarks.db"

class BookmarksApplication(Application):

    def __init__(self):
        super().__init__()
        self.bookmarks: BookmarkCollection = BookmarkCollection()
    
    def add_bookmark(self, name: str, url: str):
        self.bookmarks.add_bookmark(name, url)
        self.save(self.bookmarks)

    def get_bookmarks(self):
        return self.bookmarks.get_bookmarks()
