# write new note
import csv
import os

def write_note(note_name, note_description):
    notes = []
    notes_file = "./data/notes.csv"
    id = 0

    # read notes from file and append to list
    with open(notes_file, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            notes.append(row)
            id = int(row[0])

    # append new note to list and write all notes to file
    new_note = [str(id + 1), note_name]
    notes.append(new_note)
    with open(notes_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerows(notes)

    # write note description to a new file
    note_file_name = f"./data/notes/note_{new_note[0]}"
    with open(note_file_name, "w", encoding="utf-8") as f:
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