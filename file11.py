import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
import file1
import subprocess
from tkinter.messagebox import showwarning



# Main Window Commands
window = tk.Tk()
window.title('Linux controller')
# width, height = window.winfo_screenwidth()/1.6, window.winfo_screenheight()/1.5
width, height = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry('%dx%d+0+0' % (width,height))
window.configure(background='light steel blue')


#Global varibale
date_output_file11 = 0



# folder_path = StringVar()

message = tk.Label(window,  text = "Linux controller", bg="slate blue", fg="black", height=2, width=int(window.winfo_screenwidth()/2), font=('times', 30, 'italic bold ')).pack()



terminal_result = tk.Label(window, text="Terminal Result: ", fg="black", bg="light steel blue", font=('Helvetica 15 underline', 18), )
terminal_result.place(x=650, y=130)
dataFrameRight = Frame(window, bd=10, padx=20, relief=RIDGE)
dataFrameRight.place(x=650, y=170, width=590, height=400)
#frames left and right
# terminal_result = tk.Label(window, text="Terminal Result: ", fg="black", bg="light steel blue", font=('Helvetica 15 underline', 18), )
# terminal_result.place(x=650, y=130)


# termf = Frame(window)
# dataFrameRight.pack(side=BOTTOM, fill=X)
# id=dataFrameRight.winfo_id()
# try:
#     p = subprocess.Popen(
#         ["xterm", "-into", str(id), "-geometry", "80x20"],
#         stdin=subprocess.PIPE, stdout=subprocess.PIPE)
# except FileNotFoundError:
#    showwarning("Error", "xterm is not installed")
#    raise SystemExit 


this = tk.Label(window, text="Choose the name of the command", fg="black", bg="light steel blue", font=('Helvetica 15 underline', 18), )
this.place(x=50, y=100)
this.pack(padx=20 ,pady=40 ,anchor="w")

this_1 = tk.Label(window, text="1 --> Date", fg="black", bg="light steel blue", font=('Helvetica 15 underline', 18), )
this_1.place(x=50, y=120)
this_1.pack(padx=50 ,pady=5 ,anchor="w")

this_2 = tk.Label(window, text="2 --> Calender", fg="black", bg="light steel blue", font=('Helvetica 15 underline', 18), )
this_2.place(x=50, y=140)
this_2.pack(padx=50 ,pady=5 ,anchor="w")

this_3 = tk.Label(window, text="3 --> SSH(please enter the IP address and \n the command in the terminal)", fg="black", bg="light steel blue", font=('Helvetica 15 underline', 18), )
this_3.place(x=50, y=160)
this_3.pack(padx=50 ,pady=5 ,anchor="w")

this_4 = tk.Label(window, text="4 --> Configure httpd server", fg="black", bg="light steel blue", font=('Helvetica 15 underline', 18), )
this_4.place(x=50, y=180)
this_4.pack(padx=50 ,pady=5 ,anchor="w")

this_5 = tk.Label(window, text="5 --> Clear", fg="black", bg="light steel blue", font=('Helvetica 15 underline', 18), )
this_5.place(x=50, y=200)
this_5.pack(padx=50 ,pady=5 ,anchor="w")

#invoking the IP address input

# def ip_window():
#    ip_input_window = tk.Label(window, text="Enter choice:", width=10, height=2, fg="black", bg="light steel blue", font=('times', 15, ' bold '))
#    ip_input_window.place(x=20, y=460)

#    ip_varible = tk.Entry(window, width=40, bg="linen", fg="gray9",font=('times', 15, ' bold '))
#    ip_varible.place(x=150, y=480)

# URL Message
def prt():
#    print(url.get())
   global date_output_file11
   # date_output_file11 = file1.opt(url.get())
   # print ("HELLO")
   # file1.opt(url.get())
   date_output_file11 = file1.opt(url.get())
   # date_output_file11 = "Hello"
   
   result = tk.Label(window, text=date_output_file11, width=30, height=10, fg="black", font=('Helvetica 15 underline', 18))
   result.place(x=690, y=200)


# date_output_file11=5
# lbl_url = tk.Label(window, text=x, width=10, height=2, fg="black", bg="light steel blue", font=('times', 15, ' bold '))



lbl_url = tk.Label(window, text="Enter value:", width=10, height=2, fg="black", bg="light steel blue", font=('times', 15, ' bold '))
lbl_url.place(x=20, y=470)

url = tk.Entry(window, width=40, bg="linen", fg="gray9",font=('times', 15, ' bold '))
url.place(x=150, y=480)


# # Path Message
# lbl_path = tk.Label(window, text="Enter Path :", width=10, height=2, fg="black", bg="light steel blue", font=('times', 15, ' bold '))
# lbl_path.place(x=20, y=490)

# path = tk.Entry(window, width=40, bg="linen", fg="gray9", font=('times', 15, ' bold '))
# path.place(x=150, y=500)

#button
# clearButton = tk.Button(window, text="Clear",fg="black" ,bg="dark turquoise" ,width=10 ,height=2 , activebackground = "Red" ,font=('times', 15, ' bold '))
# clearButton.place(x=180, y=570)

#Partition Line



# Add a line in canvas widget
# canvas.create_line(25,40,25,40, fill="green", width=5)


down = tk.Button(window, text="Enter", fg="black" ,bg="yellow green" ,width=10 ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '), command=prt)
down.place(x=250, y=520)


# message = tk.Label(window,  text = "", bg="slate blue",
#             fg="black", height=1, width=int(window.winfo_screenwidth()/2), font=('times', 30, 'italic bold ')).pack(side = BOTTOM)
# sep = ttk.Separator(window, orient='vertical')
# sep.pack(padx=5, pady=5, fill= tk.Y, expand= True)

# Making two extra slot for taking input of IP address and command in option SSH connection
# Taking IP input
# ip_label = tk.Label(window, text="Enter IP address:", fg="black", bg="light steel blue", font=('times', 15))
# ip_label.place(x=11, y=490)
# ip_entry = tk.Entry(window, width=40, bg="linen", fg="gray9",font=('times', 15, ' bold '))
# ip_entry.place(x=150, y=490)

# Taking Command input
# cmd_label = tk.Label(window, text="Enter Command :", fg="black", bg="light steel blue", font=('times', 15))
# cmd_label.place(x=11, y=530)
# cmd_entry = tk.Entry(window, width=40, bg="linen", fg="gray9",font=('times', 15, ' bold '))
# cmd_entry.place(x=150, y=530)

# def ssh_func():
#    return [ip_entry.get(),cmd_entry.get()]



window.mainloop()
