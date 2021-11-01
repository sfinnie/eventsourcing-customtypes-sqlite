from bookmarks.application import *
from bookmarks.domain import Bookmark

def test_added_bookmark_saved():
    app = BookmarksApplication()
    app.add_bookmark(Bookmark("hacker news", "https://news.ycombinator.com"))
    app.add_bookmark(Bookmark("the register", "https://theregister.co.uk"))

    bookmarks = app.get_bookmarks()
    assert len(bookmarks) == 2