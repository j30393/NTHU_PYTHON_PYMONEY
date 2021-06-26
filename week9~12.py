import sys
from typing import List

cate_ok = False
class Records:
    """Maintain a list of all the 'Record's and the initial amount of money."""
    def __init__(self):
        #print('this step')
        self.valid = 1
        self.row_list = []
        self.find_record = 0
        try:
            open('record.txt')
            self.find_record = 1
        except:
            self.find_record = 0

        if(self.find_record):
            cur = 0
            with open('record.txt' , 'r') as fh:
                for thing in fh.readlines():
                    if(cur == 2):
                        try:
                            int(thing.rstrip())
                            cur = 0
                        except:
                            #print('ther must be something wrong')
                            self.valid = 0
                    else:
                        cur += 1                        
            if(self.valid and self.find_record):
                print('welcome back')
                with open('record.txt' , 'r') as fh:
                    for thing in fh.readlines():
                        self.row_list += [thing]
                return

        if(self.valid == 0 or self.find_record == 0):
            if(self.valid == 0):
                print('Invalid format in record.txt. Deleting the contents.')

            print('How much money do you have?')
            init = input()
            try:
                k = int(init)
                self.row_list.append('origin\n')
                self.row_list.append('origin\n')
                self.row_list.append(init+'\n')
            except:
                print('Invalid value for money. Set to 0 by default.')
                self.row_list.append('origin\n')
                self.row_list.append('origin\n')
                self.row_list.append('0\n')
 
    def add(self, add_things, name):
        global cate_ok
        cate_ok = False
        try:
            cate , item , amount = add_things.split(' ')
        except:
            print('invalid input the input should be as < meal breakfast -50 >')
            return
        try:
            int(amount)
        except:
            print('invalid input the input should be as < meal breakfast -50 >')
            return
        name.is_category_valid(cate,name.categories)

        if(cate_ok == 0):
            print('''The specified category is not in the category list.
You can check the category list by command "view categories".
Fail to add a record.''')
            return
        self.row_list.append(cate+'\n')
        self.row_list.append(item+'\n')
        self.row_list.append(amount+'\n')        

    def view(self):
        cur = 0
        sum_money = 0
        string = ''
        print('here is your expense and income \n Category   description  and  amount')
        print(35*'=')
        for name in self.row_list:
            #print(name.rstrip())
            if(cur == 0 or cur == 1):
                string += name.rstrip()
                string += 6*' '
                cur += 1

            elif(cur == 2):
                string += name.rstrip()
                print('%s' %string)
                string = ''
                sum_money += int(name)
                cur = 0
        print(35*'=')
        print('the amount is %d ' %sum_money)

    def delete(self,input):
        try:
            categ,item,amount = input.split(' ')
            int(amount)
            for index , name in enumerate(self.row_list):
                if(name.rstrip() == categ):
                    if(self.row_list[index+1].rstrip() == item and self.row_list[index+2].rstrip() == amount):
                        del self.row_list[index]
                        del self.row_list[index]
                        del self.row_list[index]
                        return
            print('There is no such decord . Failed to delete a record')
        except:
            print('Invalid format. Fail to delete a record.')
 
    def find(self, all_cate,name):
        if(all_cate == []):
            print('Invalid request')
            return 
        self.cate_list = []
        for index,name in enumerate(self.row_list):
            for item in all_cate:
                if(name.rstrip()== item):
                    for i in range(3):
                        self.cate_list.append(self.row_list[index+i])

        cur = 0
        sum_money = 0
        string = ''
        print(f'here is your expense and income under category {name}\n Category   description  and  amount')
        print(35*'=')
        for name in self.cate_list:
            #print(name.rstrip())
            if(cur == 0 or cur == 1):
                string += name.rstrip()
                string += 6*' '
                cur += 1

            elif(cur == 2):
                string += name.rstrip()
                print('%s' %string)
                string = ''
                sum_money += int(name)
                cur = 0
        print(35*'=')
        print('the amount is %d ' %sum_money)
 
    def save(self):
        fh = open('record.txt' , 'w')
        for name in self.row_list:
            fh.write(name)
        exit()


class Categories:
    def __init__(self):
        self.categories = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', [
            'bus', 'railway']], 'income', ['salary', 'bonus']]

    def view(self,catego,num):
        if(catego == None):
            return
        if type(catego) == type([]):
            for child in catego:
                self.view(child,num + 2)
        else:
            print(' '*num,end = '')
            print('-%s' %catego)

    def is_category_valid(self,input,handle):
        global cate_ok
        for things in handle:
            if type(things) == type([]):
                self.is_category_valid(input,things)
            else:
                #print(f'{things}')
                if(things == input):
                    cate_ok = True
                    
    def find_subcategories(self, category):
        def find_subcategories_gen(category, categories, found=False):
            if type(categories) == list:
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child, found)
                    if child == category and index + 1 < len(categories) \
                        and type(categories[index + 1]) == list:
                        # When the target category is found,
                        # recursively call this generator on the subcategories
                        # with the flag set as True.
                        yield from find_subcategories_gen(category, categories[index+1], True)
            else:
                if categories == category or found:
                    yield categories

        gen = find_subcategories_gen(category,categories.categories)
        ans=[i for i in gen]
        return ans

# class definitions here
 
categories = Categories()
records = Records()
 
while True:
    command = input('\nWhat do you want to do (add / view / delete / view categories / find / exit)?')
    if command == 'add':
        record = input('Add an expense or income record with category, description, and amount (separate by spaces):\n')
        records.add(record, categories)
    elif command == 'view':
        records.view()
    elif command == 'delete':
        delete_record = input("Which record do you want to delete? \n")
        records.delete(delete_record)
    elif command == 'view categories':
        categories.view(categories.categories,0)
    elif command == 'find':
        category = input('Which category do you want to find? ')
        target_categories = categories.find_subcategories(category)
        records.find(target_categories,category)
    elif command == 'exit':
        records.save()
        break
    else:
        sys.stderr.write('Invalid command. Try again.\n')