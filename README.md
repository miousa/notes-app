# 📝 Notes App — console note manager

A simple but convenient application for taking notes directly in the terminal.  
Notes are saved to a file `notes.json` and loaded each time you start it.  
Ideal for those who want to quickly write down important thoughts without being distracted from working in code.

## ✨ Features

- ✅ Adding notes with manual date entry.
- ✅ View all notes with serial numbers.
- ✅ Deleting notes by number (with confirmation).
- ✅ Automatically save to `notes.json` file.
- ✅ Tooltip for months in English.
- ✅ Input error handling (letters instead of numbers, etc.).

## 🧪 Technologies

- **Python 3.10+**
- Working with files (`json`, `os`)
- Built-in `datetime` library (for future improvements)

## 🚀 Launch
First, follow the link and install git on your computer: https://git-scm.com/download/win.

1. Clone the repository  
   `git clone https://github.com/miousa/notes-app.git`  
   `cd notes-app`

2. Run the program  
   `python notes.py`  

   Make sure Python 3.10 or higher is installed.

## 🎮 How to use

After launch, the menu appears:

1. ➕ Add note
2. 📋 Show all notes
3. ❌ Delete note
4. 🔍 Search note
5. ✏️ Edit note
6. 💾 Save & Exit 

- **Adding** — enter the note text, then specify the year, month (as a number or English name) and day.
- **Viewing** — displays a list of all saved notes with their numbers and dates.
- **Deleting** — shows the list of notes, then you enter the number of the note to delete and confirm the action.
- **Searching** — allows you to find notes by text, date, or tag.
- **Editing** — lets you change the text, date, or tag of an existing note.
- **Saving** — happens automatically when adding, deleting, editing, and before exiting the program.

## 📁 Storage format

Data is saved to a `notes.json` file in the current folder.  
Example:

```json
[
  {
    "note": "Buy Milk",
    "date": "2026-09-06",
    "tag": "General"
  },
  {
    "note": "KickFlip",
    "date": "2026-09-06",
    "tag": "Procces..."
  }
]
```
## 🗂️ Project structure
```
notes-app/
├── notes.py          # main script
├── notes.json        # notes file (created automatically)
└── README.md         # this file
```
## 🔮 Ideas for improvement
Add External API

Sort by date

Export to TXT / CSV

Set reminders

and more ...

## 📝 License
The project was created for educational purposes.
You are free to use and modify it.

## 👤 Author
@miousa
