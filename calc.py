from tkinter import *

root = Tk()
root.title("Calculator")

frame= Entry(root,width= 40, borderwidth=10)
frame.grid(row=0,column=0, columnspan=3, padx=10, pady=10)

def button_click(num):
	currrent_num= frame.get()
	frame.delete(0,END)
	frame.insert(0,str(currrent_num)+str(num))

def button_clear():
	frame.delete(0,END)

def button_add():
	first_number=frame.get()
	frame.delete(0,END)
	global f_num
	global math
	math ="add"
	f_num= int(first_number)
	 

def button_equal():
	second_number=frame.get()
	frame.delete(0,END)
	if math == "add":
		answer = f_num+ int(second_number)
		frame.insert(0, answer)
	if math == "subt":
		answer = f_num - int(second_number)
		frame.insert(0, answer)
	if math == "mult":
		answer = f_num * int(second_number)
		frame.insert(0, answer)
	if math == "div":
		answer = f_num / int(second_number)
		frame.insert(0, answer)


def button_subt():
	first_number=frame.get()
	frame.delete(0,END)
	global f_num
	global math
	math ="subt"
	f_num= int(first_number)

def button_mult():
	first_number=frame.get()
	frame.delete(0,END)
	global f_num
	global math
	math ="mult"
	f_num= int(first_number)

def button_div():
	first_number=frame.get()
	frame.delete(0,END)
	global f_num
	global math
	math ="div"
	f_num= int(first_number)

button0 = Button(root, text="0", padx=40, pady=20, command=lambda:button_click(0))
button1 = Button(root, text="1", padx=40, pady=20, command=lambda:button_click(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda:button_click(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda:button_click(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda:button_click(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda:button_click(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda:button_click(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda:button_click(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda:button_click(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda:button_click(9))
buttonadd = Button(root, text="+", padx=39, pady=20, command=button_add)
buttonequal = Button(root, text="=", padx=91, pady=20, command=button_equal)
buttonclear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)
buttonsubt = Button(root, text="-", padx=39, pady=20, command=button_subt)
buttonmult = Button(root, text="*", padx=39, pady=20, command=button_mult)
buttondiv = Button(root, text="/", padx=39, pady=20, command=button_div)

button1.grid(row=3 , column= 0)
button2.grid(row=3 , column= 1)
button3.grid(row=3 , column= 2)

button4.grid(row=2 , column= 0)
button5.grid(row=2 , column= 1)
button6.grid(row=2 , column= 2)

button7.grid(row=1 , column= 0)
button8.grid(row=1 , column= 1)
button9.grid(row=1 , column= 2)

button0.grid(row= 4, column= 0)

buttonadd.grid(row=5 , column =0 )
buttonequal.grid(row=5 , column =1, columnspan=2 )
buttonclear.grid(row=4 , column =1, columnspan=2 )
buttonsubt.grid(row=6 , column =0 )
buttonmult.grid(row=6 , column =1 )
buttondiv.grid(row=6, column =2 )


root.mainloop()
root.mainloop()
