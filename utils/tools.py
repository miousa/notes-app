import datetime as dt
from supporting import MONTHS

today = dt.datetime.today()


def input_data() -> tuple:
    note = input("Enter note: ").strip()
    if not note:
        print("Note can't be emptyed")

    tag_note = input("Enter note tag: ").strip()
    if not tag_note:
        print("You haven't entered anything, so the tag is marked as - General")
        tag_note = "General"

    date = str(today)[:10]
    dotw = today.strftime("%A")  # Day of the week
    autumn = today.strftime("%B")

    return (note, tag_note, date, dotw, autumn)


print(input_data())
