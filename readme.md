# Event Sourcing in Python with SQLite and custom domain datatypes

This project illustrates using the Python [eventsourcing](https://github.com/johnbywater/eventsourcing) library using:

* SQLite as a persistent datastore, and
* Custom domain datatypes using Python [dataclasses](https://docs.python.org/3/library/dataclasses.html)

The purpose isn't to demonstrate complex domain logic: it's about illustrating how the domain, application and persistence work using SQLite and custom domain datatypes.  The domain logic is consequently trivially simple, supporting a list of bookmarks that can be added to.  See [domain.py](bookmarks/domain.py).


## Status

This is work in progress.  Currently working:

1. Minimal but sufficient [domain model](bookmarks/domain.py).  
1. Minimal [application](bookmarks/application.py) that uses SQLite to persist domain data.
1. Minimal [test](tests/test_bookmarks.py).

### To Do

1. Retrieve existing aggregates from storage when the app is stopped and re-started
1. Update domain and application classes to use custom `Bookmark` datatype
1. Create custom Transcoder for serialising and de-serialising `Bookmark`s
1. Register custom transcoder in the application object at startup


## Setup

1. Ensure you have [Python installed](https://www.python.org/downloads/).  The example has been tested using version 3.8; no known reason why it won't work with anything later, though it's not been tested.
1. Set up the project:

        $ cd wherever/you/want/the/project
        $ git clone https://github.com/sfinnie/eventsourcing-customtypes-sqlite.git
        $ cd eventsourcing-customtypes-sqlite
        $ python3 -m venv venv
        $ source venv/scripts/activate
        $ python3 -m pip install eventsourcing pytest

1. run the tests:

        $ pytest

