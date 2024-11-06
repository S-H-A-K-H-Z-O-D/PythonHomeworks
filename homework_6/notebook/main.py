from tabulate import tabulate
from datetime import date
import json

class Notebook:
    def __init__(self):
        with open("homework_6/notebook/data.json", "r") as file:
            self.notes = json.load(file)

    def showAllNotes(self):
        copyData = []
        for el in self.notes:
            if len(el["Text"]) > 30:
                copyData.append({"id": el["id"], "Text":f"{el["Text"][:15]}...{el["Text"][-10:]}", "date": el["date"]})
            else:
                copyData.append(el)

        print(tabulate(copyData, headers="keys", tablefmt="grid"))

    def noteDetail(self, id):
        print("----------------------------------------")
        print(f"NOTE {id} DETAILS:")
        print(f"Note id: {id}")

        for el in self.notes:
            if el["id"] == id:
                print(f"Note text: {el["Text"]}")

    def addNote(self, note):
        id = self.notes[-1]["id"] + 1
        current_date = date.today()
        self.notes.append({"id": id, "Text": note, "date": f"{current_date}"})
        with open("homework_6/notebook/data.json", "w") as file:
            json.dump(self.notes, file, indent=4)

        print("----------------------------------------")
        print(f"NEW NOTE WITH ID {id} CREATED")

    def updateNote(self, id, note):
        for el in self.notes:
            if el["id"] == id:
                el["Text"] = note
        with open("homework_6/notebook/data.json", "w") as file:
            json.dump(self.notes, file, indent=4)

        print("----------------------------------------")
        print(f"NOTE WITH ID {id} UPDATED")

    def deleteNote(self, id):
        for el in self.notes:
            if el["id"] == id:
                del self.notes[id - 1]
        with open("homework_6/notebook/data.json", "w") as file:
            json.dump(self.notes, file, indent=4)

        print("----------------------------------------")
        print(f"NOTE WITH ID {id} DELETED")


class Terminal:

    def __init__(self):
        self.notebook = Notebook()
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
        try:
            id = int(input("Enter a note id: "))
            self.notebook.noteDetail(id)
            self.chooseOption()

        except Exception:
            print("Enter a valid integer!")
            print()
            self.noteDetail()

    def addNote(self):
        note = input("Enter text: ")
        if len(note.strip()) == 0:
            self.addNote()
        self.notebook.addNote(note)

        self.chooseOption()

    def updateNote(self):
        try:
            id = int(input("Enter id: "))
            note = input("Enter new text: ")
            if len(note.strip()) == 0:
                self.updateNote()
            self.notebook.updateNote(id, note)

            self.chooseOption()

        except Exception:
            print("Enter a valid integer!")
            print()
            self.updateNote()

    def deleteNote(self):
        try:
            id = int(input("Enter id: "))
            self.notebook.deleteNote(id)
            self.chooseOption()
                    
        except Exception:
            print("Enter a valid integer!")
            print()
            self.deleteNote()

    def quitApp(self):
        return
    
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

Terminal()