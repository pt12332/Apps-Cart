import random
import string
from functools import partial
import tkinter
from tkinter import TOP, Button, Checkbutton, Frame, IntVar, Label, StringVar
from phuoc_tran_final_project_CLASS import App, Cart

class MyFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, root)  
        self.init_container()  
        self.cart = Cart()
        self.tax = 4.3
        self.total = 0
        self.welcome()  
        self.data = StringVar(self, 'Subtotal: $0.0')

    def welcome(self):
        self.clear_frame()
        Label(self, text='Welcome to the APPS CART!',
              background="gray90").pack(side=TOP)
        Button(self, text="Select by Category", background="gray90",
               command=self.shop_by_apps_category).pack()
        Button(self, text="Select by Rating", background="gray90",
               command=self.shop_by_apps_ratings).pack()
        Button(self, text="Select by Price", background="gray90",
               command=self.shop_by_apps_price).pack()
        Button(self, text="Exit ",
               background="gray90", command=exit).pack()

    def shop_by_apps_category(self):
        self.clear_frame()
        self.init_container()
        Label(self, text='Choose Apps by Category',
              background="gray90").pack(side=TOP)

        for k, v in App.category_dict.items():
            Button(self, text=k, background="gray90",
                   command=partial(self.start, v)).pack()

        Button(self, text="Go Back", background="gray90",
               command=self.welcome).pack()



    def init_container(self):
        self.states = []  

    def clear_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    def exit_application(self):
        root.destroy()

   


    def shop_by_apps_ratings(self):
        self.clear_frame()
        self.init_container()
        myKeys = list(App.rating_dict.keys())
        myKeys.sort()
        Label(self, text='Choose Apps by Rating',
              background="gray90").pack(side=TOP)
        
        for k in myKeys:
            stars = ""
            for x in range(k):
                stars += "*"
            rating_text = f"{stars} & up"
            Button(self, text=rating_text, background="gray90",
                   command=partial(self.start, App.rating_dict[k])).pack()

        Button(self, text="Go Back", background="gray90",
               command=self.welcome).pack()

    def shop_by_apps_price(self):
        self.clear_frame()
        self.init_container()
        myKeys = list(App.price_dict.keys())
        myKeys.sort()
        Label(self, text='Choose by Price',
              background="gray90").pack(side=TOP)
        for k in myKeys:
            price_text = f"$ {k}.00 - {k+1}.00"
            Button(self, text=price_text, background="gray90",
                   command=partial(self.start, App.price_dict[k])).pack()

        Button(self, text="Go Back", background="gray90",
               command=self.welcome).pack()
        
    def add_to_cart(self, current_items):
        sub_total = 0
        for i in range(len(current_items)):
            if self.states[i].get():
                self.cart.add_item(current_items[i])
                sub_total += float(current_items[i].get_price())
        self.total += sub_total
        self.data.set(f'Subtotal: ${"{:.2f}".format(self.total)}')

    def start(self, current_items):
        self.clear_frame()
        self.init_container()
        row = 0

        for item in current_items:
            self.states.append(IntVar())  
            checkbutton = Checkbutton(self, text=item.get_name(
            ), variable=self.states[row])  
            checkbutton.grid(row=row, column=0)
            label = Label(
                self, text='Free' if item.get_price() == '0' else f"${item.get_price()}")
            label.grid(row=row, column=1)
            label = Label(
                self, text=f"{item.get_id()}")
            label.grid(row=row, column=2)
            label = Label(
                self, text=f"{item.get_developer()}")
            label.grid(row=row, column=3)
            label = Label(
                self, text=f"{item.get_description()}")
            label.grid(row=row, column=4)
            label = Label(
                self, text=f"{item.get_rating()}")
            label.grid(row=row, column=5)
            label = Label(
                self, text=f"{item.get_category()}")
            label.grid(row=row, column=6)
            row += 1

        label = Label(self, text=self.data.get(),
                      background="gray90", textvariable=self.data)
        label.grid(row=row, column=0)

        button = Button(self, text="Main Menu", background="gray90",
                        command=self.welcome)
        button.grid(row=row, column=1)

        button = Button(self, text="Add to Cart", background="gray90",
                        command=partial(self.add_to_cart, current_items))
        button.grid(row=row, column=2)

        button = Button(self, text="Checkout", background="gray90",
                        command=self.checkout)
        button.grid(row=row, column=3)

    def checkout(self):
        self.clear_frame()

        Label(self, text='Your E-Order',
              background="gray90").pack(side=TOP)
        Label(
            self, text=f"E-Order number: {self.get_receipt_number()}").pack(side=TOP)
        Label(self, text='*********').pack(side=TOP)
        headers = ["name", "price", "rating", "genre"]
        Label(self, text='\t'.join(headers)).pack(side=TOP)

        total = 0
        for item in self.cart.items:
            details = '\t'.join([item.get_name(), item.get_price(), item.get_rating(), item.get_category()])
            Label(self, text=details).pack(side=TOP)
            total += float(item.get_price())

        Label(self, text=self.data.get()).pack(side=TOP)
        Label(self, text=f'Tax: {"{:.2f}".format(self.tax)}%').pack(side=TOP)
        Label(self, text=f'Total: {"{:.2f}".format(self.total + self.total*(self.tax / 100))}').pack(side=TOP)
        Label(self, text="Thank you for chossing Apps Cart!").pack(side=TOP)
        Label(self, text='*********').pack(side=TOP)
        Button(self, text="Exit",
               background="gray90", command=exit).pack()

    


    def get_receipt_number(self):
        return ''.join(random.choices(string.ascii_letters.upper() + string.digits, k=4))


root = tkinter.Tk()
root.title("Apps Cart")
myFrame = MyFrame(root)
myFrame.pack()
root.mainloop()