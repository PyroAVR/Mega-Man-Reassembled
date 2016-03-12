**Room File**

*what?*

This file type describes a room.  It is needed because rooms by default do not have objects associated with them, and objects must be added at the time of room creation.
Because this is difficult to do if every room must have its objects instantiated by the caller before the room is created, and it is especially messy, a class is made to
automate this process, reading in this file to do so.

*how?*

JSON.  It's a nice standard.  It is easy to read (sorta) and easy to parse.  Better yet, python3 has it built in.
The format is below.  This example is somewhat skeletal, it has the bare minimum to set up a room.
Currently, the Generator() class only supports the elements listed below.
```json
[
  {
    "x": 0,
    "y": 0,
    "layer" : 0,
    "sprite": "assets/eddieclassic",
    "width" : 32,
    "height" : 32
  },
  {
    "background" : "assets/background",
    "width" : 1920,
    "height" : 1080,
    "music" : "assets/lvlmusic"
  }
]
```
The first {} pair sets up an _object_, something which is placed in the room.  Up to 1000 of these can be placed in one level file (for now).
The second {} pair sets up the _room_, which has many objects in it, a background, music, etc. The Room *must* be the last {} pair in the file.
