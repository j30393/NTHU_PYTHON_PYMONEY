import pycategory
import pyrecord
import sys
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import simpledialog

categories = pycategory.Categories()
records = pyrecord.Records()
# for the initial category
categories.view(categories.categories,0)
cate_string = categories.get_cate_list()
# end the category 

#import the content of scroll box
row_list = records.return_row_list()
#print(row_list)

#tracing the money and records avaible 
money = 0
init_condition = records.return_init_cond()
#end tracing

root = tk.Tk()
#setting title
root.title("Pymoney")
#setting window size
width=600
height=500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.resizable(width=False, height=False)
root.geometry(alignstr)

def set_command():
    s = simpledialog.askinteger("input int", "please input the original money")
    records.set_money(s)
    money = 0
    Show_item.delete(0,'end')
    row_list = records.return_row_list()
    for index,thing in enumerate (row_list):
        Show_item.insert(index,thing)
    money = records.return_sum_money()
    Total_money.config(text = str(money))


def search_command():
    global money
    money = 0
    find_thing = search_entry.get()
    target_categories = categories.find_subcategories(find_thing)
    records.find(target_categories,find_thing)
    find_list = records.return_find_list()
    Show_item.delete(0,'end')
    for index,thing in enumerate (find_list):
        Show_item.insert(index,thing)
    money = records.return_sum_money()
    Total_money.config(text = str(money))


def delete_command():
    global money
    money = 0
    for thing in Show_item.curselection():
        records.delete(Show_item.get(thing))
    row_list = records.return_row_list()
    Show_item.delete(0,'end')
    for index,thing in enumerate (row_list):
        Show_item.insert(index,thing)
    money = records.return_sum_money()
    Total_money.config(text = str(money))

    
def add_command():
    global money
    money = 0
    add_thing = Add_entry.get()
    records.add(add_thing, categories)
    row_list = records.return_row_list()
    Show_item.delete(0,'end')
    for index,thing in enumerate (row_list):
        Show_item.insert(index,thing)
    money = records.return_sum_money()
    Total_money.config(text = str(money))



search_buttun=tk.Button(root)
search_buttun["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
search_buttun["font"] = ft
search_buttun["fg"] = "#000000"
search_buttun["justify"] = "center"
search_buttun["text"] = "搜尋"
search_buttun.place(x=420,y=40,width=83,height=30)
search_buttun["command"] = search_command

Show_item=tk.Listbox(root)
Show_item["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
Show_item["font"] = ft
Show_item["fg"] = "#333333"
Show_item["justify"] = "center"
Show_item.place(x=140,y=90,width=243,height=327)
#add thing 
for index,thing in enumerate (row_list):
    Show_item.insert(index,thing)
money = records.return_sum_money()

search_entry=tk.Entry(root)
search_entry["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
search_entry["font"] = ft
search_entry["fg"] = "#333333"
search_entry["justify"] = "center"
search_entry["text"] = "SEARCH_Entry"
search_entry.place(x=150,y=40,width=217,height=30)

Delete_button=tk.Button(root)
Delete_button["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
Delete_button["font"] = ft
Delete_button["fg"] = "#000000"
Delete_button["justify"] = "center"
Delete_button["text"] = "刪除"
Delete_button.place(x=410,y=380,width=83,height=30)
Delete_button["command"] = delete_command

Add_button=tk.Button(root)
Add_button["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
Add_button["font"] = ft
Add_button["fg"] = "#000000"
Add_button["justify"] = "center"
Add_button["text"] = "加入紀錄"
Add_button.place(x=410,y=430,width=82,height=32)
Add_button["command"] = add_command

Add_entry=tk.Entry(root)
Add_entry["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
Add_entry["font"] = ft
Add_entry["fg"] = "#333333"
Add_entry["justify"] = "center"
Add_entry["text"] = "ADD_Entry"
Add_entry.place(x=140,y=430,width=240,height=30)

Show_cate=tk.Label(root)
ft = tkFont.Font(family='Times',size=12)
Show_cate["font"] = ft
Show_cate["fg"] = "#333333"
Show_cate["justify"] = "left"
Show_cate["text"] = cate_string
Show_cate.place(x=0,y=30,width=120,height=400)

Show_money=tk.Label(root)
ft = tkFont.Font(family='Times',size=18)
Show_money["font"] = ft
Show_money["fg"] = "#333333"
Show_money["justify"] = "center"
Show_money["text"] = "目前總額"
Show_money.place(x=410,y=110,width=99,height=49)

Total_money=tk.Label(root)
ft = tkFont.Font(family='Times',size=18)
Total_money["font"] = ft
Total_money["fg"] = "#333333"
Total_money["justify"] = "center"
Total_money["text"] = str(money)
Total_money.place(x=410,y=160,width=99,height=49)
Total_money.config(text = str(money))

Set_button=tk.Button(root)
Set_button["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
Set_button["font"] = ft
Set_button["fg"] = "#000000"
Set_button["justify"] = "center"
Set_button["text"] = "初始化"
Set_button.place(x=410,y=350,width=82,height=32)
Set_button["command"] = set_command

### use for first time 
def popup():
    messagebox.showinfo("First time","This is the first time....or something wrong \n Remember to add your init money")

if(init_condition == 2 or init_condition == 3):
    popup()
elif(init_condition == 1):
    row_list = records.return_row_list()
    Show_item.delete(0,'end')
    for index,thing in enumerate (row_list):
        Show_item.insert(index,thing)
    money = records.return_sum_money()
    Total_money.config(text = str(money))

### handling close
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        records.save()
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()