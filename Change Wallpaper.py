import tkinter as tk
import shutil
import time
from tkinter import filedialog


print('Choose Wallpaper...')
path = tk.filedialog.askopenfilename()
if path.endswith('.jpg'):
    shutil.copyfile(path, 'C:\\Program Files (x86)\\Steam\\steamapps\\workshop\\content\\431960\\845587216\\1.jpg')
    print('Change complete.')
else:
    print('The file must be .jpg!')
print('The program will be shut down in 5s...')
time.sleep(5)
