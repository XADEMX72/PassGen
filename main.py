import string
import random
import tkinter as tk
from tkinter import messagebox


def generate_password():
    password = ''
    password_length = password_length_var.get()
    characters = string.ascii_letters + string.digits + string.punctuation
    for i in range(password_length):
        password += random.choice(characters)
    password_var.set(password)
    check_password_strength(password)


def check_password_strength(password):
    strength = ''
    if any(char.isdigit() for char in password) and any(char.isupper() for char in password) and len(password) >= 12:
        strength = 'strong'
    elif (any(char.isdigit() for char in password) or any(char.isupper() for char in password)) and len(password) >= 8:
        strength = 'moderate'
    if strength:
        messagebox.showinfo('Password Strength', f'The generated password is {strength}.')


def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_var.get()
    if website and username and password:
        with open('passwords.txt', 'a') as file:
            file.write(f'{website} | {username} | {password}\n')
        website_entry.delete(0, tk.END)
        username_entry.delete(0, tk.END)
        password_var.set('')
        messagebox.showinfo('Success', 'Password saved successfully!')
    else:
        messagebox.showerror('Error', 'Please fill in all fields.')


def show_passwords():
    with open('passwords.txt', 'r') as file:
        passwords = file.readlines()
    if passwords:
        window = tk.Toplevel(root)
        window.title('Saved Passwords')
        for i, password in enumerate(passwords):
            password_label = tk.Label(window, text=password)
            password_label.grid(row=i, column=0)
            copy_button = tk.Button(window, text='Copy', command=lambda p=password: copy_password(p))
            copy_button.grid(row=i, column=1)


def copy_password(password):
    root.clipboard_clear()
    root.clipboard_append(password.split(' | ')[2])
    messagebox.showinfo('Success', 'Password copied to clipboard!')


root = tk.Tk()
root.title('Password Manager')
root.geometry('1400x900')

FONT = ('Arial', 16)

tk.Label(root, text='Website:', font=FONT).grid(row=0, column=0)
website_entry = tk.Entry(root, font=FONT)
website_entry.grid(row=0, column=1)

tk.Label(root, text='Username:', font=FONT).grid(row=1, column=0)
username_entry = tk.Entry(root, font=FONT)
username_entry.grid(row=1, column=1)

tk.Label(root, text='Password length:', font=FONT).grid(row=2, column=0)
password_length_var = tk.IntVar()
password_length_var.set(8)
password_length_entry = tk.Entry(root, textvariable=password_length_var, font=FONT)
password_length_entry.grid(row=2, column=1)

tk.Button(root, text='Generate Password', font=FONT, command=generate_password).grid(row=3, column=0)
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, state='readonly', font=FONT).grid(row=3, column=1)

tk.Button(root, text='Save Password', font=FONT, command=save_password).grid(row=4, column=0)
tk.Button(root, text='Show Saved Passwords', font=FONT, command=show_passwords).grid(row=4, column=1)

root.mainloop()
