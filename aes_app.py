from aes import AES
from tkinter import *
from tkinter import messagebox
from base64 import b64encode, b64decode

import os
import pyperclip


class AesApp:
    def __init__(self):
        self.key = os.urandom(32)
        self.aes = AES(self.key)

        self.root = Tk()
        self.root.title("AES Encryption")
        self.root.geometry("600x600")

        menubar = Menu(self.root)

        encrypt_menu = Menu(menubar, tearoff=0)
        encrypt_menu.add_command(label="Encrypt", command=self.encrypt)

        decrypt_menu = Menu(menubar, tearoff=0)
        decrypt_menu.add_command(label="Decrypt", command=self.decrypt)

        help_menu = Menu(menubar, tearoff=0)
        help_menu.add_command(label="Exit", command=exit)

        menubar.add_cascade(label="Encrypt", menu=encrypt_menu)
        menubar.add_cascade(label="Decrypt", menu=decrypt_menu)
        menubar.add_cascade(label="Help", menu=help_menu)

        frame = Frame(self.root)
        frame.place(relx=0.5, rely=0.5, anchor="c")

        welcome_label = Label(
            frame, text="Welcome to AES Encryption and Decryption App",
            font=("Arial", 14, 'bold')
        )
        welcome_label.pack()

        select_label = Label(
            frame, text="Please Select One Of The Items From Above Menu",
            font=("Arial", 10, 'bold')
        )
        select_label.pack()

        self.root.config(menu=menubar)
        self.root.mainloop()

    def exit(self):
        self.root.exit()

    def encrypt(self):
        encrypt_window = Tk()
        encrypt_window.title("Encrypt")
        encrypt_window.geometry("500x500")

        frame = Frame(encrypt_window)
        frame.place(relx=0.5, rely=0.5, anchor="c")

        self.message = Text(frame, height=5, width=50)
        self.message.tag_configure('center', justify='center')
        self.message.pack()

        encrypt_button = Button(
            frame, text="Encrypt", command=self.handle_encrypt, height=2, width=34)
        encrypt_button.pack()

    def handle_encrypt(self):
        data = self.message.get("1.0", END).strip()

        if(data == ""):
            return messagebox.showerror("Error", "Enter some text to encrypt")

        cipher_text, iv = self.aes.encrypt(str.encode(data))

        self.iv_key = iv

        encrypted_message = b64encode(cipher_text).decode('utf-8')

        # copy the encrypted data to the clipboard
        pyperclip.copy(encrypted_message)

        messagebox.showinfo("Encrypted successfully", encrypted_message)

    def decrypt(self):
        decrypt_window = Tk()
        decrypt_window.title("Decrypt")
        decrypt_window.geometry("500x500")
        frame = Frame(decrypt_window)
        frame.place(relx=0.5, rely=0.5, anchor="c")

        self.decrypt_input = Text(frame, height=5, width=50)
        self.decrypt_input.pack()

        decrypt_button = Button(
            frame, text="Decrypt", command=self.handle_decrypt, height=2, width=32)
        decrypt_button.pack()

    def handle_decrypt(self):

        encrypted_data = self.decrypt_input.get("1.0", END)
        encrypted_data = b64decode(encrypted_data)

        if(encrypted_data == ""):
            return messagebox.showerror("Error", "Enter the encrypted message")

        decrypted_data = self.aes.decrypt(encrypted_data,  self.iv_key)

        messagebox.showinfo("Success", decrypted_data[0:])


# start the app
try:
    AesApp()
except:
    print("Closing application")
