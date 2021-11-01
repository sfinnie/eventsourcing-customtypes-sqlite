from eventsourcing.application import Application
from eventsourcing.persistence import Transcoder, Transcoding
from typing import Dict, List
from bookmarks.domain import BookmarkCollection, Bookmark

# Use SQLite as a persistent store of data instead of the default
# transient, in-memory store.
import os
os.environ["INFRASTRUCTURE_FACTORY"] = "eventsourcing.sqlite:Factory"
os.environ["SQLITE_DBNAME"] = "data/bookmarks.db"


class BookmarkTranscoding(Transcoding):
    type = Bookmark
    name = "Bookmark_as_dict"

    def encode(self, obj: Bookmark) -> str:
        assert isinstance(obj, Bookmark)
        return obj.name
        # return vars(obj)

    def decode(self, data: dict) -> Bookmark:
        assert isinstance(data, dict)
        return Bookmark(**data)


class BookmarksApplication(Application):

    def __init__(self):
        super().__init__()
        self.bookmarks_id = self.create_bookmark_collection()
    
    def register_transcodings(self, transcoder: Transcoder):
        super().register_transcodings(transcoder)
        transcoder.register(BookmarkTranscoding)

    def create_bookmark_collection(self, name: str = "default_bookmark_collection"):
        bookmarks = BookmarkCollection(name)
        self.save(bookmarks)
        return bookmarks.id
    
    def add_bookmark(self, bookmark: Bookmark):
        bookmarks = self.repository.get(self.bookmarks_id)
        bookmarks.add_bookmark(bookmark)
        self.save(bookmarks)

    def get_bookmarks(self):
        bookmarks = self.repository.get(self.bookmarks_id)
        return bookmarks.get_bookmarks()

