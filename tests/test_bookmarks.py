from bookmarks.application import *

def test_added_bookmark_saved():
    app = BookmarksApplication()
    app.add_bookmark("hacker news", "https://news.ycombinator.com")
    app.add_bookmark("the register", "https://theregister.co.uk")

    bookmarks = app.get_bookmarks()
    assert len(bookmarks) == 2