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
4. 🚪 Exit  

- **Adding** — enter the note text, then year, month (number or name in English) and day.  
- **Viewing** — displays a list of all notes with numbers and dates.  
- **Deleting** — you will see a list of notes, enter the number and confirm deletion.  
- **Saving** occurs automatically when adding, deleting and before exiting.

## 📁 Storage format

Data is saved to a `notes.json` file in the current folder.  
Example:

```json
[
    {"note": "Buy milk", "date": "2025-03-15"},
    {"note": "Call mom", "date": "2025-04-20"}
]
🗂️ Project structure
text
notes-app/
├── notes.py          # main script
├── notes.json        # notes file (created automatically)
└── README.md         # this file
```

## 🔮 Ideas for improvement
Editing notes

Search by text

Sort by date

Export to TXT / CSV

Set reminders

## 📝 License
The project was created for educational purposes.
You are free to use and modify it.

## 👤 Author
[YOUR NAME] — @miousa
