import tkinter as tk
from tkinter import messagebox
import webbrowser
import ctypes

# Hide the console window
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

GAMES = {
    'Repo PingPong': 'https://github.com/KernFerm/PingPong',
    'Repo Snake': 'https://github.com/KernFerm/Snake',
    'Repo Tetris': 'https://github.com/KernFerm/Tetris',
    'Tetris.exe': 'https://file.io/sAR5083W4pXs',
    '2nd Tetris.exe if first link expires or is broken': 'https://file.io/wl0BkoIhmV1a',
    '3rd Tetris.exe if first and second link expires or is broken': 'https://file.io/sYz2HmbyDL3N',
}

def select_game(game):
    repo_url = GAMES[game]
    webbrowser.open(repo_url)
    messagebox.showinfo("Info", "To Download The Repo From Fnbubbles420 Github Page, Click On The Green Box Upper Right Hand Corner, Click Download Zipfile. Make Sure To Read All The Intruction on The README.md File. From The Download Link When You Click Tetris.exe If You Get A Suspicious Warning From Your Browser -Click Continue Download-  The Tetris.exe is NOT digitally signed, so you will get a warning from Windows Defender. Click on More Info and then Run Anyway.") 
     
root = tk.Tk()
root.geometry("400x500")
root.title("FNBUBBLES420 GITHUB GAME HUB")

game_menu = tk.OptionMenu(root, tk.StringVar(), *GAMES.keys(), command=select_game)
game_menu.pack()

root.mainloop()
