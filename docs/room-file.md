**Room File**

*What?*

This file type describes a room.  It is needed because rooms by default do not have objects associated with them, and objects must be added at the time of room creation.
Because this is difficult to do if every room must have its objects instantiated by the caller before the room is created, and it is especially messy, a class is made to
automate this process, reading in this file to do so.

*How?*

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
  "type": "DialogBox",
  "nframes": "2",
  "text1" : "lorem ipsum dolor sit amet,",
  "text2" : "consectetur adipiscing elit...",
  "char1" : "assets/mmclassicface",
  "char2" : "assets/zeroXface"
  },
  {
    "tmx" : "assets/lvl/lvl.tmx",
    "music" : "assets/lvlmusic"
  }
]
```
The first {} pair sets up an _object_, something which is placed in the room.  Up to 1000 of these can be placed in one level file (for now).
The last {} pair sets up the _room_, which has many objects in it, a background, music, etc. The Room element **must** be the last {} pair in the file.

The Generator() searches through _object_ elements and first reads their type, a required field.  It then branches to the correct method in order to create that object type.

**Supported Keys**

The _"type"_ key is _required_ for all _objects_

Object Types:
- AIObject
- Player
- DialogBox
