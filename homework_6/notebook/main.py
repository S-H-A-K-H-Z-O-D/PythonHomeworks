from tabulate import tabulate
from datetime import date
import json
import os
import reprlib

class Notebook:
    base_dir = os.path.dirname(__file__)
    data_file_path = os.path.join(base_dir, "data.json")

    def __init__(self):      
        if not os.path.exists(self.data_file_path):
            with open(self.data_file_path, "w") as file:
                json.dump([], file)
        
        with open(self.data_file_path, "r") as file:
            self.notes = json.load(file)

    def showAllNotes(self):
        copyData = []
        for el in self.notes:
            shortened_string = reprlib.repr(el["Text"])
            copyData.append({"id": el["id"], "Text":shortened_string, "date": el["date"]})

        print(tabulate(copyData, headers="keys", tablefmt="grid"))

    def noteDetail(self, id):
        print("----------------------------------------")
        print(f"NOTE {id} DETAILS:")
        print(f"Note id: {id}")

        for el in self.notes:
            if el["id"] == id:
                print(f"Note text: {el["Text"]}")

    def addNote(self, note):
        id = 1 if len(self.notes) == 0 else self.notes[-1]["id"] + 1
        current_date = date.today()
        self.notes.append({"id": id, "Text": note, "date": f"{current_date}"})
        with open(self.data_file_path, "w") as file:
            json.dump(self.notes, file, indent=4)

        print("----------------------------------------")
        print(f"NEW NOTE WITH ID {id} CREATED")

    def updateNote(self, id, note):
        for el in self.notes:
            if el["id"] == id:
                el["Text"] = note
        with open(self.data_file_path, "w") as file:
            json.dump(self.notes, file, indent=4)

        print("----------------------------------------")
        print(f"NOTE WITH ID {id} UPDATED")

    def deleteNote(self, id):
        for el in self.notes:
            if el["id"] == id:
                self.notes.remove(el)
        with open(self.data_file_path, "w") as file:
            json.dump(self.notes, file, indent=4)

        print("----------------------------------------")
        print(f"NOTE WITH ID {id} DELETED")


class Terminal:
    def __init__(self):
        self.notebook = Notebook()

    def run(self):
        self.options()

    def chooseOption(self):
        print()
        a = input("Choice: ").lower()
        self.whichOption(a)

    def options(self):
        print("CHOOSE OPTION")
        print("     1: SHOW ALL NOTES")
        print("     2: SHOW NOTE DETAILS")
        print("     3: CREATE NOTE")
        print("     4: UPDATE NOTE")
        print("     5: DELETE NOTE")
        print("     Q: QUIT THE APPLICATION")
        print("     M: SHOW MENU AGAIN")
        
        self.chooseOption()
    
    def noteDetail(self):
        id = self.get_id(self.noteDetail)
        self.notebook.noteDetail(id)
        self.chooseOption()

    def addNote(self):
        note = input("Enter text: ")
        if len(note.strip()) == 0:
            self.addNote()
        self.notebook.addNote(note)

        self.chooseOption()

    def updateNote(self):
        id = self.get_id(self.updateNote)
        note = input("Enter new text: ")
        if len(note.strip()) == 0:
            self.updateNote()
        self.notebook.updateNote(id, note)

        self.chooseOption()

    def deleteNote(self):
        id = self.get_id(self.deleteNote)
        self.notebook.deleteNote(id)
        self.chooseOption()

    def get_id(self, func):
        try:
            id = int(input("Enter a note id: "))
            return id
        except ValueError:
            print("Enter a valid integer!")
            print()
            func()


    def quitApp(self):
        exit()
    
    def whichOption(self, opt):
        match opt:
            case "1":
                self.notebook.showAllNotes()
                self.chooseOption()
            case "2":
                self.noteDetail()
            case "3":
                self.addNote()
            case "4":
                self.updateNote()
            case "5":
                self.deleteNote()
            case "q":
                self.quitApp()
            case "m":
                self.options()
            case _:
                print("Enter only one of these options(1, 2, 3, 4, 5, Q, M)!")
                self.chooseOption()

app = Terminal()
app.run()