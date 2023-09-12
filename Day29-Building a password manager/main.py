from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters=[choice(letters) for _ in range(randint(8, 10))]
    password_symbols=[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers=[choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters+password_numbers+password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    web=web_entry.get()
    user=user_entry.get()
    passw=pass_entry.get()

    if len(web) == 0 or len(user)==0 or len(passw)==0:
        messagebox.showerror(title="Entry Empty", message="You cannot leave any entry empty.")
    else:
        is_ok=messagebox.askokcancel(title="Verification",message=f"Website:{web}\nUsername:{user}\nPassword:{passw}\nIs this the correct information?")

    if is_ok==True:
        with open(".\\data.txt",mode="a") as data:
            data.write(f"{user}, {web}, {passw} \n")
            web_entry.delete(0,END)
            user_entry.delete(0,END)
            pass_entry.delete(0,END)
            web_entry.focus()

# ---------------------------- UI SETUP ------------------------------- #
windows=Tk()
windows.title("Password Manager")
windows.config(padx=50,pady=50)
windows.minsize(width=500,height=500)

canvas=Canvas(width=200,height=200)
logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

# ---------------------------- LABELS ------------------------------- #
website = Label(text="Website",font=("Courier",16),fg="Black")
website.grid(column=0,row=1)

user=Label(text="Email/Username",font=("Courier",16),fg="Black")
user.grid(column=0,row=2)

password=Label(text="Password",font=("Courier",16),fg="Black")
password.grid(column=0,row=3)

# ---------------------------- ENTRIES ------------------------------- #
web_entry=Entry(width=36)
web_entry.grid(column=1,row=1,columnspan=2)
web_entry.focus()

user_entry=Entry(width=36)
user_entry.grid(column=1,row=2,columnspan=2)

pass_entry=Entry(width=36)
pass_entry.grid(column=1,row=3)
# ---------------------------- BUTTONS ------------------------------- #
generate=Button(text="Generate Password",command=generate_password)
generate.grid(column=3,row=3)

add=Button(text="Add",width=36,command=save_password)
add.grid(column=1,row=4,columnspan=2)

windows.mainloop()
