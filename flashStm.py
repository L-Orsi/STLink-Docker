import json
import os

FLASH_CMD = "st-flash --reset --format binary write %s %s" # format: <addr> <size> 

if __name__ == "__main__":
    # Loads config.
    config = {}
    with open("flashConfig.json", "r") as json_file:
        config = json.load(json_file)
    # Runs the stm commands.
    os.system(FLASH_CMD % ((config["filename"], config["address"])))

