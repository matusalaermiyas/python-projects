import os

from pathlib import Path
from tkinter import *
from tkinter import filedialog, messagebox
# from tkinter import ttk


# def handle_delete():
#     try:
#         directory = filedialog.askdirectory()

#         files = Path(directory).glob('*.vtt')

#         for file in files:
#             os.remove(file)

#         messagebox.showinfo('Hooray 😁', 'Subtitles deleted successfully')
#     except Exception as ex:
#         print(ex)
#         messagebox.showerror(
#             'Error', 'Error while deleting, maybe run it as an admin')


app = Tk()

app.geometry("500x500")

app.title('Remove | Subtitles')

try:
    directory = filedialog.askdirectory()

    files = Path(directory).glob('*.zip')

    for file in files:
        os.remove(file)

    messagebox.showinfo('Hooray 😁', 'Subtitles deleted successfully')
except Exception as ex:
    print(ex)
    messagebox.showerror(
        'Error', 'Error while deleting, maybe run it as an admin')

# frame = Frame(app)
# frame.place(relx=0.5, rely=0.5, anchor="c")

# x = ttk.Style()
# x.configure("BW.TLabel", foreground="white",
#             background="darkgrey", font=('calibri', 15, 'bold'), padding=10)


# delete_button = ttk.Button(frame, text='Start Here',
#                            command=handle_delete, style='BW.TLabel')
# delete_button.pack()

# app.mainloop()
