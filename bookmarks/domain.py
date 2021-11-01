from dataclasses import dataclass
from typing import Dict
from eventsourcing.domain import Aggregate, event


@dataclass
class Bookmark:
    """A simple domain datatype to represent a bookmark.
       super-simple, because the purpose is to illustrate 
       adding a custom transcoder for serialising/deserialising
       datatypes.   
    """
    name: str
    url: str

class BookmarkCollection(Aggregate):
    """A trivially simple collection of bookmarks.
       The logic is intentionally simple; the purpose of this
       example isn't to illustrate complex domain logic (even though
       that's the primary use case for Domain-driven design).  Rather,
       it's an architectural example - showing how to piece together domain, 
       application and persistence.
    """

    @event("BookmarkCollectionCreated")
    def __init__(self, name: str):
        self.name = name
        self.bookmarks: Dict[str, Bookmark] = {}

    #TODO: update to use Bookmark datatype instead of a pair of strings
    @event("BookmarkAdded")
    def add_bookmark(self, bookmark: Bookmark) -> None:
        self.bookmarks[bookmark.name] = bookmark

    def get_bookmarks(self):
        return self.bookmarks
