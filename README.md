# Save Slot Switcher Script

This script helps you manage save files in a game that only supports three save slots — SLOT0, SLOT1, and SLOT2.

Due to a bug in the game, only the last opened save slot is actually playable. This means that if your save is in SLOT0 or SLOT1, you can't load it properly.
This script makes it easy to swap file names so that any save can be renamed to SLOT2 — effectively tricking the game into loading the save you want to play.


## How to start:

> 👉 **Step 1** 

```bash
$ git clone https://github.com/SnowFox999/Wolfenstein-2-Save-files-script.git
```
Or download the file manually

<br />

> 👉 **Step 2**


Change the BASE_PATH to your path with saved files of the game

<br />

> 👉 **Step 2**

Open the terminal. Choose which slot you want to change to the latest. The latest slot could also be the SLOT1, depends on how much games did you open. The availoble range is - SLOT0, SLOT1, SLOT2

Example: you want to change your saved game SLOT1 to the playable SLOT2
```bash
python swap_slots.py SLOT1 SLOT2
```

<br />

Enjoy!
