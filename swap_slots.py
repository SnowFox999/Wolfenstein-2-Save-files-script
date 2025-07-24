import os
import sys

BASE_PATH = r"C:\Users\Jonas\Saved Games\MachineGames\Wolfenstein II The New Colossus\base\savegame.user\76561198317597328"

SLOTS = ["SLOT0", "SLOT1", "SLOT2"]

def swap_folders(slot_a, slot_b):
    if slot_a not in SLOTS or slot_b not in SLOTS:
        print(f"Error, allowed slots - {SLOTS}")
        return

    path_a = os.path.join(BASE_PATH, slot_a)
    path_b = os.path.join(BASE_PATH, slot_b)
    temp_name = "__TEMP_SWAP__"

    path_temp = os.path.join(BASE_PATH, temp_name)

    if not os.path.exists(path_a) or not os.path.exists(path_b):
        print("Error: one of the folders doesnt exist")
        return

    try:
        os.rename(path_a, path_temp)
        os.rename(path_b, path_a)
        os.rename(path_temp, path_b)
        print(f"Done")
    except Exception as e:
        print(f"Error")

if __name__ == "__main__":
    if len(sys.argv) !=3:
        print("Use python swap_slots")
    else:
        swap_folders(sys.argv[1], sys.argv[2])

    