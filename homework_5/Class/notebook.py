from tabulate import tabulate

initData = [
    {"id": 1, "Text": "Doing homework sjhdbfvjksd jhsbdcns lakmsc lmkxcbn, mqwiu lkjmasdbk clor sit amet"},
    {"id": 2, "Text": "Cleaning a room"},
    {"id": 3, "Text": "Preparing a meal"},
    {"id": 4, "Text": "Go to the Gym"}
]

def shorten_text(text): 
    return f"{text[:15]}...{text[-10:]}"

def options():
    print("CHOOSE OPTION")
    print("     1: SHOW ALL NOTES")
    print("     2: SHOW NOTE DETAILS")
    print("     3: CREATE NOTE")
    print("     4: UPDATE NOTE")
    print("     5: DELETE NOTE")
    print("     Q: QUIT THE APPLICATION")
    print("     M: SHOW MENU AGAIN")
    
    print()
    a = input("Choice: ")
    whichOption(a)

def showAllNotes():
    copyData = []
    for el in initData:
        if len(el["Text"]) > 30:
            copyData.append({"id": el["id"], "Text": shorten_text(el["Text"])})
        else:
            copyData.append(el)

    print(tabulate(copyData, headers="keys", tablefmt="grid"))

    print()
    a = input("Choice: ")
    whichOption(a)

def noteDetail():

    try:
        id = input("Enter a note id: ")
        print("----------------------------------------")
        print(f"NOTE {id} DETAILS:")
        print(f"Note id: {id}")

        for el in initData:
            if el["id"] == int(id):
                print(f"Note text: {el["Text"]}")
        
        print()
        a = input("Choice: ")
        whichOption(a)

    except Exception:
        print("Enter a valid integer!")
        print()
        noteDetail()

def addNote():
    note = input("Enter text: ")
    id = initData[-1]["id"] + 1

    if len(note.strip()) == 0:
        addNote()

    initData.append({"id": id, "Text": note})
    print("----------------------------------------")
    print(f"NEW NOTE WITH ID {id} CREATED")

    print()
    a = input("Choice: ")
    whichOption(a)

def updateNote():
    try:
        id = int(input("Enter id: "))
        note = input("Enter new text: ")

        if len(note.strip()) == 0:
            updateNote()

        for el in initData:
            if el["id"] == id:
                el["Text"] = note

        print("----------------------------------------")
        print(f"NOTE WITH ID {id} UPDATED")

        print()
        a = input("Choice: ")
        whichOption(a)

    except Exception:
        print("Enter a valid integer!")
        print()
        updateNote()

def deleteNote():
    try:
        id = int(input("Enter id: "))

        for el in initData:
            if el["id"] == id:
                 del initData[id + 1]

        print("----------------------------------------")
        print(f"NOTE WITH ID {id} DELETED")

        print()
        a = input("Choice: ")
        whichOption(a)
                 
    except Exception:
        print("Enter a valid integer!")
        print()
        deleteNote()
        

def quitApp():
    return

def whichOption(opt):
    match opt:
        case "1":
            showAllNotes()
        case "2":
            noteDetail()
        case "3":
            addNote()
        case "4":
            updateNote()
        case "5":
            deleteNote()
        case "Q":
            quitApp()
        case "M":
            options()
        case _:
            print("Enter only one of these options(1, 2, 3, 4, 5, Q, M)!")

            print()
            a = input("Choice: ")
            whichOption(a)

options()
