from bookmarks.application import *
from bookmarks.domain import Bookmark

# Convenience for testing/debugging purposes.
# Run `pytest` for tests

if __name__ == "__main__":
    app = BookmarksApplication()
    app.add_bookmark(Bookmark("hacker news", "https://news.ycombinator.com"))
