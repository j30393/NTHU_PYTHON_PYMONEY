from datetime import *
from tkinter import messagebox
today__ = date.today()
today = today__.strftime("%Y-%m-%d")
class Records:
    """Maintain a list of all the 'Record's and the initial amount of money."""
    def __init__(self):
        #print('this step')
        self.initial_condition = 0 # 1 -> ok file  2-> print('Invalid format in record.txt. Deleting the contents.') 
        self.sum_money = 0
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
                    if(cur == 3):
                        try:
                            k = int(thing.rstrip())
                            self.sum_money += k
                            cur = 0
                        except:
                            self.valid = 0
                    else:
                        cur += 1                        
            if(self.valid and self.find_record):
                self.initial_condition = 1
                with open('record.txt' , 'r') as fh:
                    for thing in fh.readlines():
                        self.row_list += [thing]
                return

        if(self.valid == 0 or self.find_record == 0):
            if(self.valid == 0):
                self.initial_condition = 2
            else:
                self.initial_condition = 3

    def calculate_money(self):
        cur = 0
        self.sum_money = 0
        for name in self.row_list:
            if(cur == 0 or cur == 1 or cur == 2):
                cur += 1
            elif(cur == 3):
                mon = name.rstrip()
                self.sum_money += int(mon)
                cur = 0

    def return_init_cond(self):
        return self.initial_condition

    def set_money(self,num):
        self.row_list = []
        self.row_list.append(today+'\n')
        self.row_list.append('origin\n')
        self.row_list.append('origin\n')
        self.row_list.append(str(num)+'\n')
        self.sum_money = num

    def return_row_list(self):
        editted_row_list = []
        string = ''
        cur = 0
        for name in self.row_list:
            if(cur == 0 or cur == 1 or cur==2):
                string += name.rstrip()
                string += 3*' '
                cur += 1

            elif(cur == 3):
                string += name.rstrip()
                editted_row_list.append(string)
                string = ''
                cur = 0
        return editted_row_list

    def return_sum_money(self):
        return self.sum_money

    def add(self, add_things, name):
        is_arguement_valid = 3
        try:
            cate , item , amount = add_things.split(' ')
        except:
            is_arguement_valid -= 2
        try:
            date , cate, item ,amount = add_things.split(' ')
        except:
            is_arguement_valid -= 1

        try:
            int(amount)
        except:
            is_arguement_valid -= 6

        if(is_arguement_valid <= 0):
            messagebox.showinfo("Someting wrong","invalid input the input should be as < YYYY-MM-DD meal breakfast -50 >")
            return 
        
        if(is_arguement_valid == 2):
            date = today
        elif(is_arguement_valid == 1):
            #print(date)
            try:
                datetime.strptime(date, '%Y-%m-%d')
            except:
                messagebox.showinfo("Someting wrong","invalid date")
                return 
        #check the date -> is_argument_valid = 1 means only three cate
        #while is_arguement = 2 means four parameter
        if(name.is_category_valid(cate) == False):
            messagebox.showinfo("Someting wrong","wrong category")
            return
        self.row_list.append(date+'\n')
        self.row_list.append(cate+'\n')
        self.row_list.append(item+'\n')
        self.row_list.append(amount+'\n')
        self.calculate_money()      

    def delete(self,input):
        try:
            date,categ,item,amount = input.split()
            int(amount)
            for index , name in enumerate(self.row_list):
                if(name.rstrip() == date):
                    if(self.row_list[index+1].rstrip() == categ and self.row_list[index+2].rstrip() == item and self.row_list[index+3].rstrip() == amount):
                        del self.row_list[index]
                        del self.row_list[index]
                        del self.row_list[index]
                        del self.row_list[index]
                        self.calculate_money()
                        return

            print('There is no such decord . Failed to delete a record')
        except:
            print('Invalid format. Fail to delete a record.')

    def return_find_list(self):
        editted_find_list = []
        string = ''
        cur = 0
        for name in self.cate_list:
            if(cur == 0 or cur == 1 or cur==2):
                string += name.rstrip()
                string += 3*' '
                cur += 1

            elif(cur == 3):
                string += name.rstrip()
                editted_find_list.append(string)
                string = ''
                cur = 0
        return editted_find_list       


    def find(self, all_cate,name):
        if(all_cate == []):
            messagebox.showinfo("Someting wrong","wrong category")
            return 
        self.cate_list = []
        for index,name in enumerate(self.row_list):
            for item in all_cate:
                if(name.rstrip()== item):
                    for i in range(-1,3):
                        self.cate_list.append(self.row_list[index+i])

        cur = 0
        self.sum_money = 0
        for name in self.cate_list:
            #print(name.rstrip())
            if(cur == 0 or cur == 1 or cur == 2):
                cur += 1
            elif(cur == 3):
                self.sum_money += int(name)
                cur = 0
 
    def save(self):
        fh = open('record.txt' , 'w')
        for name in self.row_list:
            fh.write(name)
        exit()
