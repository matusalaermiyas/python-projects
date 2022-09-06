import shutil

from pathlib import Path
from tkinter import *
from tkinter import filedialog, messagebox

app = Tk()

app.geometry('500x500')
app.title('File remover')

try:
    directory = filedialog.askdirectory()
    folders = Path(directory).glob('*')

    for folder in folders:
        video_in_folder = Path(folder).glob('*.mp4')

        for video in video_in_folder:
            shutil.move(video, directory)

except Exception as ex:
    print('Error occured try again')
