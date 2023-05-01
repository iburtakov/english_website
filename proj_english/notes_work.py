# write new note
import csv
import os

NOTES_FILE = "./data/notes.csv"
NOTES_DIR = "./data/notes"

def write_note(note_name, note_description):
    # Read notes from file
    with open(NOTES_FILE, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter=";")
        notes = list(reader)

    # Get the ID for the new note
    new_note_id = int(notes[-1][0]) + 1 if notes else 1

    # Append new note to list
    new_note = [str(new_note_id), note_name]
    notes.append(new_note)

    # Write notes to file
    with open(NOTES_FILE, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerows(notes)

    # Write note description to file
    note_file_path = f"{NOTES_DIR}/note_{new_note[0]}"
    with open(note_file_path, "w", encoding="utf-8") as f:
        f.write(note_description)


# read notes from notes.csv
def get_notes_to_show():
    notes = []
    notes_file = "./data/notes.csv"

    # read notes from file and append to list
    with open(notes_file, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            notes.append(row)

    # read note descriptions and append to corresponding notes
    for note in notes:
        note_id = int(note[0])
        note_file_name = f"./data/notes/note_{note_id}"
        try:
            with open(note_file_name, "r", encoding="utf-8") as f:
                note_description = f.readlines()
                note.append(note_description)
        except IOError:
            notes = []
            break
    
    return notes