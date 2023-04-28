# write new note
def write_note(note_name, note_description):
    notes = []
    with open("./data/notes.csv", "r", encoding="utf-8") as f:
        for line in f.readlines():
            id, name = line.strip("\n").split(";")
            notes.append([id, name])
        notes.append([str(int(id) + 1), note_name])
    with open("./data/notes.csv", "w", encoding="utf-8") as f:
        note_lines = []
        for note in notes:
            note_lines.append(";".join(note))
        f.write('\n'.join(note_lines))
    note_file_name = f"./data/notes/note_{str(int(id)+1)}"
    with open(note_file_name, "w", encoding="utf-8") as f:
        f.write(note_description)

# read notes from notes.csv
def get_notes_to_show():
    notes = []
    ids = []
    with open("./data/notes.csv", "r", encoding="utf-8") as f:
        for line in f.readlines():
            id, name = line.strip("\n").split(";")
            notes.append([id, name])
            ids.append(int(id))
    for id in ids:
        with open(f"./data/notes/note_{id}", "r", encoding="utf-8") as f:
            notes[id-1].append([l.strip('\n') for l in f.readlines()])
    print(notes)
    return notes