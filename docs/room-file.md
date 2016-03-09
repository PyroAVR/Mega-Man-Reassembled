**Room File**

*what?*

This file type describes a room.  It is needed because rooms by default do not have objects associated with them, and objects must be added at the time of room creation.
Because this is difficult to do if every room must have its objects instantiated by the caller before the room is created, and it is especially messy, a class is made to
automate this process, reading in this file to do so.

*how?*

JSON.  It's a nice standard.  It is easy to read (sorta) and easy to parse.  Better yet, python3 has it built in.
