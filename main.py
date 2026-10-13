from utils import NOTES_FILE, MONTHS, show_menu
from storage import load_notes


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
