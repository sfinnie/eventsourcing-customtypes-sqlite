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
        self.bookmarks_id = self.create_bookmark_collection()
    
    def create_bookmark_collection(self, name: str = "default_bookmark_collection"):
        bookmarks = BookmarkCollection(name)
        self.save(bookmarks)
        return bookmarks.id
    
    def add_bookmark(self, name: str, url: str):
        bookmarks = self.repository.get(self.bookmarks_id)
        bookmarks.add_bookmark(name, url)
        self.save(bookmarks)

    def get_bookmarks(self):
        bookmarks = self.repository.get(self.bookmarks_id)
        return bookmarks.get_bookmarks()

