import json
import os

# Constant Variable
NOTES_FILE = "notes.json"

# Dictionary month -> number
MONTHS = {
    "january": '01', "february": '02', "march": '03', "april": '04',
    "may": '05', "june": '06', "july": '07', "august": '08',
    "september": '09', "october": '10', "november": '11', "december": '12'
}

# File operations
def load_notes():
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Convert old format (list of strings) to new format
            if data and isinstance(data[0], str):
                return [{"note": item, "date": "Date unknown", "tag": "Unknown"} for item in data]
            
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_notes(notes):
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)

# Program functions
def show_notes(notes):
    if not notes:
        print("There are no notes.")
    else:
        print("\n--- ALL NOTES ---")
        for i, note in enumerate(notes, start=1):
            print(f"{i}. {note['note']} — {note['date']}. Tag: {note['tag']}")
        print()

def show_menu():
    print("\n" + "=" * 20)
    print("NOTES")
    print("=" * 20)
    print("1. Add note")
    print("2. Show all notes")
    print("3. Delete note")
    print("4. Search note")
    print("5. Edit note")
    print("6. Exit")
    print("-" * 20)

def add_note(notes):
    note = input("Enter the text of note: ").strip()

    if not note:
        print("Empty note not added.")
        return

    print("\nEnter date:")

    # Year
    year = input("Year (e.g., 2025): ").strip()

    if not year.isdigit():
        print("Invalid year. Note not added.")
        return

    # Month
    print("\nAvailable months:")
    for eng, num in MONTHS.items():
        print(f"  {eng} → {num}")
    
    month_input = input("Month (01-12 or name in English): ").strip().lower()

    if not month_input:
        print("Month cannot be empty. Note not added.")
        return

    if month_input in MONTHS:
        month = MONTHS[month_input]
    elif month_input.isdigit() and 1 <= int(month_input) <= 12:
        month = f"{int(month_input):02d}"
    else:
        print("Invalid month. Note not added.")
        return

    # Day
    day = input("Day (01-31): ").strip()

    if not (day.isdigit() and 1 <= int(day) <= 31):
        print("Invalid day. Note not added.")
        return
    
    day = f"{int(day):02d}"
    date = f"{year}-{month}-{day}"

    tag_note = input("Enter note tag: ")
    if not tag_note:
        print("You haven't entered anything, so the tag is marked as - General")
        tag_note = "General"
        
    
    notes.append({"note": note, "date": date, "tag": tag_note})
    save_notes(notes)
    print("Note added and saved.")

def delete_note(notes):
    if not notes:
        print("No notes to delete.")
        return

    while True:
        show_notes(notes)
        try:
            num = int(input(f"Number of note to delete (1-{len(notes)}): "))
        except ValueError:
            print("Enter a number!")
            continue

        if 1 <= num <= len(notes):
            confirm = input(f"Delete note {num}? (YES/NO): ").lower().strip()

            if confirm == "yes":
                del notes[num - 1]
                save_notes(notes)
                print("Note deleted.")
                break
            else:
                print("Deletion canceled.")
                break
        else:
            print(f"Number must be between 1 and {len(notes)}.")

def _print_search_results(notes, found_indices):
    if not found_indices:
        print("No matching notes found.")
    else:
        print("\n--- SEARCH RESULTS ---")
        for i in found_indices:
            note = notes[i-1]
            print(f"{i}. {note['note']} — {note['date']}. Tag: {note['tag']}")
        print()

def search_note(notes):
    print("\n--- SEARCH MENU ---")
    print("1. Search by text")
    print("2. Search by date")
    print("3. Search by tag")
    print()

    if not notes:
        print("No notes to search.")
        return
    
    choice = input("Enter: ")
    found_indices = []

    if choice == "1":
        request = input("Enter keyword: ").lower().strip()

        for i, note in enumerate(notes, start=1):
            if request in note['note'].lower():
                found_indices.append(i)

    elif choice == "2":
        print("\nAvailable months:")
        for eng, num in MONTHS.items():
            print(f"  {eng} → {num}")

        request = input("Enter the date (YYYY-MM-DD): ").strip()

        for i, note in enumerate(notes, start=1):
            if request in note['date']:
                found_indices.append(i)

    elif choice == "3":
        request = input("Input tag: ").lower().strip()

        for i, note in enumerate(notes, start=1):
            if request in note['tag'].lower():
                found_indices.append(i)

    else:
        print("Invalid choice.")
        return
    
    _print_search_results(notes, found_indices)

def edit_note(notes):
    if not notes:
        print("No notes to edit.")
        return

    show_notes(notes)
    try:
        ind_edit = int(input("Enter num note: "))

        if not 1 <= ind_edit <= len(notes):
            print("Invalid note number.")
            return
    except ValueError:
        print("Enter a valid number.")
        return
    
    print("\n--- EDIT MENU ---")
    print("1. Edit text")
    print("2. Edit date")
    print("3. Edit tag")
    print()

    choice = input("Choose: ")
    
    if choice == "1":
        text_edit = input("Enter text: ")

        if not text_edit:
            print("Note text cannot be empty.")
            return
        
        notes[ind_edit - 1]['note'] = text_edit
        save_notes(notes)
        print("Note updated.")

    elif choice == "2":
        date_edit = input("Enter new date ('2000-01-20' 10 char): ")

        if not date_edit:
            print("Date cannot be empty")
            return
        
        if len(date_edit) == 10 and date_edit[4] == '-' and date_edit[7] == '-':
            notes[ind_edit - 1]['date'] = date_edit
            save_notes(notes)
            print("Note update")

    elif choice == "3":
        tag_edit = input("Enter new tag: ")

        if not tag_edit:
            print("Tag cannot be empty")
            return
        
        notes[ind_edit - 1]['tag'] = tag_edit
        save_notes(notes)
        print("Note update")

# Main
def main():
    notes = load_notes()
    print(f"Loaded notes: {len(notes)}")

    while True:
        show_menu()
        choice = input("Your choice: ")

        if choice == "1":
            add_note(notes)
        elif choice == "2":
            show_notes(notes)
        elif choice == "3":
            delete_note(notes)
        elif choice == "4":
            search_note(notes)
        elif choice == "5":
            edit_note(notes)
        elif choice == "6":
            save_notes(notes)
            print("Notes saved. Goodbye!")
            break
        else:
            print("Invalid choice. Enter 1-6.")

if __name__ == "__main__":
    main()
