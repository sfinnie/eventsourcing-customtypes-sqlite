from eventsourcing.application import Application
from typing import Dict, List
from bookmarks.domain import BookmarkCollection

class BookmarksApplication(Application):

    def __init__(self):
        super().__init__()
        self.bookmarks: BookmarkCollection = BookmarkCollection("default_collection")
    
    def add_bookmark(self, name: str, url: str):
        self.bookmarks.add_bookmark(name, url)
        self.save(self.bookmarks)

    def get_bookmarks(self):
        return self.bookmarks.get_bookmarks()
