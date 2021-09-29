def birthday(name):
    if name == 'albert':
        print(name,'birthday is',data['albert'])
    elif name == 'benjamin':
        print(name,'birthday is',data['benjamin'])
    elif name == 'frank':
        print(name,'birthday is ',data['frank'])
    else:
        print("the input is not in our dictionary, please recheck!")

data = {'albert': '05/01/1999', 'benjamin': '14/01/1996', 'frank': '21/05/2000'}
print('welcome to the birthday dictionary. we know the birthdays of \nalbert \nbenjamin \nfrank')
name = str(input('who\'s birthday do you want to look up?'))
birthday(name)