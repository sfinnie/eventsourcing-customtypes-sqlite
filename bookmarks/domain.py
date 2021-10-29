from typing import Dict
from eventsourcing.domain import Aggregate, event

class BookmarkCollection(Aggregate):
    """A trivially simple collection of bookmarks.
       The logic is intentionally simple; the purpose of this
       example isn't to illustrate complex domain logic (even though
       that's the primary use case for Domain-driven design).  Rather,
       it's an architectural example - showing how to piece together domain, 
       application and persistence.
    """

    @event("BookmarkCollectionCreated")
    def __init__(self, name: str = "default_bookmark_collection"):
        self.name = name
        self.bookmarks: Dict[str, str] = {}

    @event("BookmarkAdded")
    def add_bookmark(self, name: str, url: str) -> None:
        self.bookmarks[name] = url

    def get_bookmarks(self):
        return self.bookmarks