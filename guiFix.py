import tkinter as tk

# instantiate variables
acc_id = tk.StringVar()
transnumber = tk.StringVar()
transmed = tk.StringVar()
withamt = tk.StringVar()
depamt = tk.StringVar()

# Top level window
bank = tk.Tk()
bank.title("Indian Service Bank")
label=tk.Label(bank,text = "INDIAN SERVICE BANK")
label.pack(side="top")
bank.geometry('400x200')

def triggerTransation():
 web2=tk.Tk()
 web2.geometry('400x200')
 web2.title("Transaction")
 label2=tk.Label(web2,text="TRANSACTION")
 label2.grid(row=1,column=1)
 label1=tk.Label(web2,text="Account I'd: ")
 label1.grid(row=2,column=2,pady=(0,20))
 ent11 = tk.Entry(web2,width=15)
 ent11.grid(row=2,column=2,pady=(0,20))

 def func():
  acc_id = ent11.get()
  print(acc_id)

 butt4=tk.Button(web2,text="Enter",command=func)
 butt4.grid(row=5,column=1)

transactBtn=tk.Button(bank,text="TRANSACTION",command=triggerTransaction)
transactBtn.pack()
bank.mainloop()


