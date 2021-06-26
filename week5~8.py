import sys
import os.path 
exist = 0
valid = 1
row_list = []
def initialize():
    try:
        open('record.txt')
        return 1
    except:
        return 0

exist = initialize();

if(exist):
    cur = 0
    with open('record.txt' , 'r') as fh:
        for thing in fh.readlines():
            if(cur == 1):
                try:
                    int(thing.rstrip())
                    cur = 0
                except:
                    valid = 0
            elif(cur == 0):
                cur += 1


if(exist & valid):
    print('welcome back')
    with open('record.txt' , 'r') as fh:
        for thing in fh.readlines():
            row_list += [thing]
else:
    if(valid == 0):
        print('Invalid format in records.txt. Deleting the contents.')
    print('How much money do you have?')
    init = input()
    try:
        k = int(init)
        row_list.append('origin\n')
        row_list.append(init+'\n')
    except:
        print('Invalid value for money. Set to 0 by default.') 
        row_list.append('origin\n')
        row_list.append('0\n')

def add():
    global row_list
    print('Add an expense or income record with description and amount: ')
    thing  = input()
    try:
        item = thing.split(' ')
        int(item[1])
        row_list.append(item[0]+'\n')
        row_list.append(item[1]+'\n')
    except:
        print('it should be valid input e.g breakfast -70')
        print('failed to add a record')

def exit_cmd():
    fh = open('record.txt' , 'w')
    for name in row_list:
        fh.write(name)
    exit()

def view():
    cur = 0
    sum_money = 0
    string = ''
    print('here is your expense and income \ndescription  and  amount');
    print(25*'=')
    for name in row_list:
        if(cur == 0):
            string += name.rstrip()
            string += 6*' '
            cur += 1
        elif(cur):
            string += name.rstrip()
            print('%s' %string)
            string = ''
            sum_money += int(name)
            cur = 0

    print(25*'=')
    print('the amount is %d ' %sum_money)

def delete():
    global row_list
    print('Which record do you want to delete?')
    thing = input()
    try:
        item = thing.split(' ')
        int(item[1])
        for index , name in enumerate(row_list):
            if(name.rstrip() == item[0]):
                if(row_list[index+1].rstrip() == item[1]):
                    del row_list[index]
                    del row_list[index]
                    return

        print('There is no decord with %s. Failed to delte a record' %item)

    except:
        print('Invalid format. Fail to delete a record.')

while True:
    command = input('\nWhat do you want to do (add / view / delete / exit)? ')
    if command == 'add':
        add()
    elif command == 'view':
        view()
    elif command == 'delete':
        delete()
    elif command == 'exit':
        exit_cmd()
    else:
        sys.stderr.write('Invalid command. Try again.\n')
