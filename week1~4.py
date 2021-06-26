print('How much money do you have? ')
init = int(input())
while True:
    print('Add an expense or income record with description and amount:')
    modify = input()
    if modify == '':
        print('Bye~')
        break
    string = (modify.split())
    lost_or_gain =  int(string[1]);
    init += lost_or_gain;
    print('Now you have %d dollars.\n' %init)
