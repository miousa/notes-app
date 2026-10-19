from note import Note

"""
themes = {
    'theme': {
        'name_note': object.__class__(Notes),
        'name_note': object.__class__(Notes)
    }
}
"""


class NoteManager:
    def __init__(self):
        self.themes = {}

    def create_theme(self, theme: str) -> bool:
        if theme:
            self.themes.setdefault(theme, {})
            return True
        return False

    def delete_theme(self, theme: str) -> bool:
        if theme:
            try:
                del self.notes[theme]
                return True
            except KeyError:
                return False
        return False

    def show_theme(self) -> bool:
        if not self.themes:
            return False
        for theme in self.themes:
            print(f"\n{theme.upper()}\n")
            for i, note in enumerate(self.notes[theme]):
                print(f"[{i}. {note}")

    def write_notes(self, theme: str) -> Note | bool:
        if theme not in self.themes:
            return False

        self.themes[theme] = Note()
        return self.themes[theme]


test = NoteManager()
test.create_theme("Школьные заметки")
print(test.notes)
