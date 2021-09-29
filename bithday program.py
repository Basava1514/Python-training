""" Write a program (function!) that takes a list and returns a new list that contains all the elements
of the first list minus all the duplicates.
For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that
information based on their name. Create a dictionary (in your file) of names and birthdays.
When you run your program it should ask the user to enter a name, and return the birthday of
that person back to them. The interaction should look something like this:
#>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
#>>> Who's birthday do you want to look up?
Benjamin Franklin
#>>> Benjamin Franklin's birthday is 01/17/1706"""


data = [{"name": 'albert', 'd.o.b': '05/01/1999'},
        {'name': 'benjamin', 'd.o.b': '14/01/1996'},
        {'name': 'frank', 'd.o.b': '21/05/2000'}]
print("Welcome to the birthday dictionary. We know the birthdays of:\n albert\n benjamin\nfrank")
d = str(input("Who's birthday do you want to look up?"))
for d in data:
    for key in d:
        pass
print(d[key])
