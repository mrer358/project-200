from tkinter import *
import threading
import random
import time
import socket
import tkMessageBox
import base64

class Start(threading.Thread):
    def __init__(self, balance=0, My_account=500000):
        threading.Thread.__init__(self)
        self.listaccount = []
        self.registernamelist = []
        self.registerpasswordlist = []
        self.balance = balance
        self.My_account = My_account
        self.root = Tk()
        self.root.title('welcome to the bank')
        self.root.geometry('250x250+250+250')
        self.lebel1 = Label(self.root, text='welcome  to the bank', bg='black', fg='green', font=50)
        self.lebel1.pack(
            side=TOP, anchor=CENTER, expand=YES
        )
        self.lebel2 = Label(self.root, text='username:', font=15)
        self.lebel2.pack(
            side=TOP, anchor=CENTER, expand=YES,
        )
        self.entry1 = Entry()
        self.entry1.pack(
            side=TOP, anchor=CENTER, expand=YES,
        )
        self.lebel3 = Label(self.root, text='password:', font=15)
        self.lebel3.pack(
            side=TOP, anchor=CENTER, expand=YES,
        )
        self.entry2 = Entry(self.root, show='*')
        self.entry2.pack(
            side=TOP, anchor=CENTER, expand=YES,
        )
        self.button1 = Button(self.root, text='OK', bg='black', fg='green', command=self.Bruge)
        self.button1.pack(
            side=TOP, anchor=S,
        )
        self.button2 = Button(self.root, text='register', bg='black', fg='green', command=self.Window)
        self.button2.pack(
            side=TOP, anchor='se', expand='YES',
        )
        t1 =threading.Thread(target=self.Socket)
        t1.daemon = True
        t1.start()
        mainloop()

    def Window(self):
        list = []
        self.GUI2 = Tk()
        self.GUI2.title('welcome to registration of the bank')
        self.GUI2.geometry('300x300')
        self.lebel = Label(self.GUI2, text='please insert your info here ', bg='black', fg='green', font=35)
        self.lebel.pack(
            side=TOP, anchor=CENTER, expand=YES
        )
        self.lebel4 = Label(self.GUI2, text='username or name:', font=15, width=50, height=1)
        self.lebel4.pack(
            side=TOP, anchor=N, expand=YES
        )
        self.enlt1 = Entry(self.GUI2, font=20)
        self.enlt1.pack(
            side=TOP, anchor=N, expand=YES
        )
        self.lebel5 = Label(self.GUI2, text=' insert your password', font=20)
        self.lebel5.pack(
            side=TOP, anchor=N, expand=YES,
        )
        self.lebel6 = Label(self.GUI2, text=' you want to create:', font=20)
        self.lebel6.pack(
            side=TOP, anchor=N, expand=YES
        )
        self.enlt2 = Entry(self.GUI2, font=20, show='*')
        self.enlt2.pack(
            side=TOP, anchor=N, expand=YES,
        )
        self.GUI2.butte2 = Button(self.GUI2, text='OK', fg='green', bg='black', command=self.Genretore)
        self.GUI2.butte2.pack(
            side=TOP, anchor=N, expand=YES
        )
        mainloop()

    def Genretore(self):
        print (self.enlt1.get())
        print (self.enlt2.get())
        self.registernamelist.append(self.enlt1.get())
        self.registerpasswordlist.append(self.enlt2.get())
        for ff in range(1, 100):
            a = random.randrange(1, 20000)
            namelibl = Label(self.GUI2, text=('this is your username  ', self.registernamelist)).pack()
            passwordlibl = Label(self.GUI2, text=('this is your password ', self.registerpasswordlist)).pack()
            lenb = Label(self.GUI2, text=(str('this is your number account '), a)).pack()
            self.listaccount.append(a)
            time.sleep(0.4)
            break

    def Bruge(self):
        print self.registerpasswordlist
        print (self.entry2.get())
        if (self.entry2.get()) == self.registerpasswordlist[0] == (self.entry2.get()):
            if (self.entry1.get()) == self.registernamelist[0] == (self.entry1.get()):
                self.ShopBank()
            elif (self.entry1.get()) != self.registernamelist[0] != (self.entry1.get()):
                tkMessageBox.showerror('error', message='error bad user or password')
        elif (self.entry2.get()) != self.registerpasswordlist[0] != (self.entry2.get()):
            tkMessageBox.showerror('error', message='error bad password')
        else:
            print 'bad way'

    def checkButtns(self, *e):
        indexes = self.Checklist.curselection()
        if indexes == (0,):
            self.withdraw(50)
            print self.My_account
        elif indexes == (1,):
            self.withdraw(20000)
            print self.My_account
        elif indexes == (2,):
            self.withdraw(25000)
            print self.My_account
        elif indexes == (3,):
            self.withdraw(2000)
            print self.My_account
        elif indexes == (4,):
            self.withdraw(500)
            print self.My_account
        elif indexes == (5,):
            self.withdraw(66000)
            print self.My_account
        elif indexes == (6,):
            self.withdraw(2600)
            print self.My_account
        elif indexes == (7,):
            self.withdraw(5)
            print self.My_account
        elif indexes == (8,):
            self.withdraw(6000)
            print self.My_account
        elif indexes == (9,):
            self.withdraw(4000)
            print self.My_account
        elif indexes == (10,):
            self.withdraw(600)
            print self.My_account
        elif indexes == (11,):
            self.withdraw(500)
            print self.My_account
        elif indexes == (12,):
            self.withdraw(15000)
            print self.My_account
        elif indexes == (13,):
            self.withdraw(2600)
            print self.My_account
        elif indexes == (14,):
            self.withdraw(4000)
            print self.My_account
        elif indexes == (15,):
            self.withdraw(10000)
            print self.My_account
        else:
            print 'error'

    def deposit(self, amount):
        self.My_account += int(amount)

    def withdraw(self, amount):
        self.My_account -= int(amount)

    def ShopBank(self):
        self.Shop = Tk()
        self.Shop.title('welcome  to the bank shop!')
        self.Shop.geometry('460x460')
        self.LE1 = Label(self.Shop, font=5,
                         text=('hello user=', self.registernamelist, 'number account=', self.listaccount))
        self.LE1.pack(

        )
        self.LE2 = Label(self.Shop, text='chose what you want to buy', font=20, bg='black', fg='green')
        self.LE2.pack(
            side=TOP, anchor=CENTER
        )
        self.Checklist_text = Text(self.Shop, height=15, width=65)
        quote = """A bank account is a financial account maintained by a financial institution for a customer. A
       bank account can be a deposit account, a credit card account, or any other type of account offered
       by a financial institution, and represents the funds that a customer has entrusted to the financial
       institution and from which the customer can make withdrawals. Alternatively, accounts may be loan
       accounts in which case
       the customer owes money to the financial institution.
       The financial transactions which have occurred within a given period of time on a bank account are reported to
       the customer on a bank statement and the balance of the accounts at any point in time is the financial
       position of the
       customer with the institution.
       The laws of each country specify the manner in which accounts may be opened and operated. They may specify,
       for example,
       who may open an account, how the signatories can identify themselves, deposit and withdrawal limits and many other
       matters."""

        self.Checklist_text.insert(END, quote)
        self.Checklist_text.pack(
            side=BOTTOM, anchor=W
        )
        self.Checklist = Listbox(self.Shop, font=35, height=10, width=30, bg='black', fg='green')
        self.Checklist.insert(1, 'cat 50$')
        self.Checklist.insert(2, 'home 20000')
        self.Checklist.insert(3, 'truck new 25000$')
        self.Checklist.insert(4, 'a computer 2000$')
        self.Checklist.insert(5, 'a woman 500$')
        self.Checklist.insert(6, 'boat 66,000')
        self.Checklist.insert(7, 'CD form 70s 2,600')
        self.Checklist.insert(8, 'moer 5$ ')
        self.Checklist.insert(9, 'phone android 6,000$')
        self.Checklist.insert(10, 'phone apple 4,000$')
        self.Checklist.insert(11, 'phone fake android 600$')
        self.Checklist.insert(12, 'phone apple fake 500$')
        self.Checklist.insert(13, 'tools  for security 15,000$')
        self.Checklist.insert(14, 'rege a car for one day 2.600$')
        self.Checklist.insert(15, 'rege a boles 4.000$')
        self.Checklist.insert(16, 'rege a hackers 10.000$')
        self.Checklist.pack(
            side=LEFT, anchor=NW
        )
        self.Checklist.bind('<<ListboxSelect>>', self.checkButtns)
        self.Checklist_lebl = Label(self.Shop, text='insert money for account', bg='black', fg='green').pack()
        self.Checklist_inout_enley = Entry(self.Shop)
        self.Checklist_inout_enley.pack()
        self.Checklist_inout_money = Button(self.Shop, text='ok', bg='black', fg='green',
                                            command=self.PlusAccouns).pack()

        mainloop()

    def PlusAccouns(self):
        ssss = self.Checklist_inout_enley.get()
        self.deposit(int(ssss))
        tkMessageBox.showinfo(title='update balanse', message=self.My_account)

    def Socket(self):
        self.host = '127.0.0.1'
        self.port = 4434
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.host, self.port))
        self.datA()

    def datA(self):
        while True:
            try:
                self.data = self.s.recv(2048)
                decoder  = base64.b64decode(self.data)
                if decoder > 0:
                    if decoder == 'status':
                        fe = self.My_account
                        self.s.send(base64.b64encode('status account '+ str(fe)))
                    elif decoder == 'info':
                        user = self.registernamelist
                        paswd= self.registerpasswordlist
                        self.s.send(base64.b64encode("--info on the user you loged-- ""\n"'username: '+str(user)+'\n''password: '+str(paswd)+'\nnumber of the account: '+ str(self.listaccount)))
                    elif decoder == '1':
                        self.s.send('ok')

                    else:
                        self.s.send('we dont have its options')
            except:
                print ('error in '+ str(socket.error))
        self.s.close()



b = Start(500000)
b.start()
