
#  To solve for all 12 days not just since day
def twelve_days(day):
    day_in_word = ["first", "second"]
    # print(day_in_word[day-1])
    day_of_christmas = print(f"On the {day_in_word[day-1]} day of Christmas")
    verse = print(f"On the first day of Christmas\nMy true love gave to me:\nA partridge in a pear tree.")
     
    print(f"On the first day of Christmas\nMy true love gave to me:\nA partridge in a pear tree.")
    print(verse)
    # verse = print(f"On the {day_in_word[day-1]} day of Christmas\nMy true love gave to me:\nA partridge in a pear tree.")
    # verse = str( str(day_of_christmas) + "\nMy true love gave to me:\nA partridge in a pear tree.")
    if day==1:
        return "On the first day of Christmas\nMy true love gave to me:\nA partridge in a pear tree."

def test_first_day():
    assert twelve_days(1) == "On the first day of Christmas\nMy true love gave to me:\nA partridge in a pear tree."

test_first_day()