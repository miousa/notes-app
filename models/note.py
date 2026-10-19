class Notes:
    def __init__(self):
        self.notes = {}

    def add_note(
        self, note: str, note_tag: str, date: str, dotw: str, autumn: str
    ) -> None:
        self.notes = {
            "Name": note,
            "Tag": note_tag,
            "Date": date,
            "WeekDay": dotw,
            "Autumn": autumn,
        }

    def delete_note(self, name: str, date: str) -> bool:
        if not self.notes:
            return False

        for i, note in enumerate(self.notes):
            if note["Name"] == name and note["Date"] == date:
                try:
                    del self.notes[i]
                except IndexError:
                    return False
        return True

    def edit_note(self, name: str, date: str) -> bool:
        if not self.notes:
            return False

        for note in self.notes:
            if note["Name"] == name and note["Date"] == date:
                note["Name"] = input("Enter new note: ").strip()
                return True

    def show_notes(self):
        if not self.notes:
            return False

        for i, note in enumerate(self.notes):
            print(
                f"Main\n{i}. {note['Name']}\n{note['Tag']}\nOther:\n{note['Date']}\n{note['WeekDay']}\n{note['Autumn']}"
            )
