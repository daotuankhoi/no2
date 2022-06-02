#start to create smart 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

import json 
app = QApplication([])

notes = {
    "Welcome!":{
        "text":"hello I don't know how do you know my why do you my app?",
        "tag":['hello', 'hi','po','ok']
    }
}

with open("notes_data.json","w") as file:
    json.dump(notes,file)
    file.close()

main_win = QWidget()
main_win.setWindowTitle("Smart Notes Application?")
main_win.resize(900,600)

lst_nte_lbl = QLabel("List of notes")
lst_tg_lbl = QLabel("List of tags")

Create_note_btn = QPushButton("Create note")
Delete_note_btn = QPushButton("Delete note")
Save_note_btn = QPushButton("Save note")
Add_note_btn  = QPushButton("Add to note")
Untag_note_btn = QPushButton("Untag from note")
Search_note_btn = QPushButton("Search notes by tag")

field_text = QTextEdit()
field_tag  = QLineEdit("Enter tag...")

list_note = QListWidget()
list_tag = QListWidget()

layout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(field_text)

col2.addWidget(lst_nte_lbl)
col2.addWidget(list_note)

row1 = QHBoxLayout()
row1.addWidget(Create_note_btn)
row1.addWidget(Delete_note_btn)

row2 = QHBoxLayout()
row2.addWidget(Save_note_btn)

col2.addLayout(row1)
col2.addLayout(row2)

col2.addWidget(lst_tg_lbl)
col2.addWidget(list_tag)

col2.addWidget(field_tag)

row3 = QHBoxLayout()
row3.addWidget(Add_note_btn)
row3.addWidget(Untag_note_btn)

row4 = QHBoxLayout()
row4.addWidget(Search_note_btn)

col2.addLayout(row3)
col2.addLayout(row4)

layout_notes.addLayout(col1)
layout_notes.addLayout(col2)
main_win.setLayout(layout_notes)

def add_note():
    note_name, ok = QInputDialog.getText(main_win,"Add note","Note name:")

    if ok and note_name != "":
        notes[note_name] = {"text": "", "tag": []}
        list_note.addItem(note_name)
        list_tag.addItems(notes[note_name]["tag"])
        list_note.setCurrentRow(list_note.count()-1)


def show_note():
    note_title = list_note.selectedItems()[0].text()
    print(note_title)
    field_text.setText(notes[note_title]["text"])
    list_tag.clear()
    list_tag.addItems(notes[note_title]["tag"])

def save_note():
    if list_note.selectedItems():
        key = list_note.selectedItems()[0].text()
        notes[key]["text"] = field_text.toPlainText()
        with open("notes_data.json","w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
            file.close()
        print(notes)
    else:
        print("Note to save is not selected.")

def delete_note():
    if list_note.selectedItems():
        curr_note = list_note.currentRow()
        print("Delete note index:",curr_note)
        if curr_note == 0:
            print("You cannot delete this note:")
            return
        key = list_note.selectedItems()[0].text()
        del notes[key]
        list_note.clear()
        list_tag.clear()
        field_text.clear()
        list_note.addItems(notes)
        with open("notes_data.json","w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
            file.close()
        print(notes)
        list_note.setCurrentRow(curr_note - 1)
        note_title = list_note.selectedItems()[0].text()
        print(note_title)
        field_text.setText(notes[note_title]["text"])
        list_tag.clear()
        list_tag.addItems(notes[note_title]["tag"])

    else:
        print("Note to delete is not selected.")

def add_tag():
    if list_note.selectedItems():
        key = list_note.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]["tag"]:
            notes[key]["tag"].append(tag)
            list_tag.addItem(tag)
            field_tag.clear()
        with open("notes_data.json","w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print("Tag to add is not selected.")

def del_tag():
    if list_note.selectedItems():
        key = list_note.selectedItems()[0].text()
        tag = list_tag.selectedItems()[0].text()
        notes[key]["tag"].remove(tag)
        list_tag.clear()
        list_tag.addItems(notes[key]["tag"])
        with open("notes_data.json","w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print("Tag to remove is not selected.")

def search_tag():
    tag = field_tag.text()
    if Search_note_btn.text() == "Search notes by tag" and tag:
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]["tag"]:
                notes_filtered[note] = notes[note]
        list_note.clear()
        list_tag.clear()
        list_note.addItems(notes_filtered)
        Search_note_btn.setText("Reset search")
    elif Search_note_btn.text() == "Reset search":
        list_note.clear()
        list_tag.clear()
        field_tag.clear()
        list_note.addItems(notes)
        Search_note_btn.setText("Search notes by tag")

list_note.itemClicked.connect(show_note)
Create_note_btn.clicked.connect(add_note)
Save_note_btn.clicked.connect(save_note)
Delete_note_btn.clicked.connect(delete_note)
Add_note_btn.clicked.connect(add_tag)
Untag_note_btn.clicked.connect(del_tag)
Search_note_btn.clicked.connect(search_tag)

with open("notes_data.json","r") as file:
    notes = json.load(file)
    file.close()

list_note.addItems(notes)

main_win.show()
app.exec()



from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import * 

app = QApplication([])



app.exec() 
