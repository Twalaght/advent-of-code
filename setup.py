#!/usr/bin/python3

from datetime import timedelta, timezone, datetime
from pathlib import Path
from os import getenv
from shutil import copy
from requests import get

# Get the Advent of Code current server time
aoc_time = datetime.now(timezone(timedelta(hours = -5)))

# Check that session token has been set
session_token = getenv("aoc_session")
if not session_token:
	print("Error - Set AoC session token as an environment variable named aoc_session")
	exit(1)

# Check it is a valid day
if aoc_time.month == 12 and 1 <= aoc_time.day <= 25:
	target_path = Path.cwd() / str(aoc_time.year) / f"day{aoc_time.day:02}"

	# Make the folder and copy the template file
	print(f"Creating folder for {aoc_time.year}/{aoc_time.day:02}...")
	Path(target_path).mkdir(parents = True, exist_ok = True)
	if (target_path / f"{aoc_time.day:02}.py").exists():
		print("Folder already exists")
		exit(1)

	copy(Path.cwd() / "template.py", target_path / f"{aoc_time.day:02}.py")

	# Save the input for the day to the new folder
	print(f"Getting input for {aoc_time.year}/{aoc_time.day:02}...")
	cookies = {"session": session_token}
	url = f"https://adventofcode.com/{aoc_time.year}/day/{aoc_time.day}/input"
	day_input = get(url, cookies = cookies)

	if day_input.status_code != 200:
		print("Error - Input could not be downloaded. Check session token")
		exit(1)

	with open(target_path / "input.txt", "w") as f: f.write(day_input.text)
	print("Done")
