# author: Dhruv Shukla
# date: May 29, 2023
# file: game.py a Python program that implements shuffle and click button class for Fifteen Puzzle game
# input: No input from the user taken directly
# output: interactive text messages and a fifteen puzzle game.
from tkinter import *
import tkinter.font as font
from fifteen import Fifteen


def shuffle():
    tiles.shuffle()
    k = 0
    for i in tiles.tiles:
        button = gui.nametowidget(str(i))
        button.grid(row=k // 4, column=k % 4)
        k += 1


def clickButton(button):
    eq = button.cget("text")
    r = button.grid_info()['row']
    c = button.grid_info()['column']
    Or = button0.grid_info()['row']
    Oc = button0.grid_info()['column']
    if tiles.is_valid_move(int(eq)):
        tiles.update(int(eq))
        button.grid_forget()
        button0.grid_forget()
        button0.grid(row=r, column=c)
        button.grid(row=Or, column=Oc)


if __name__ == '__main__':

    # make tiles
    tiles = Fifteen()

    # make a window
    gui = Tk()
    gui.title("Fifteen")

    # make font
    font = font.Font(family='Helveca', size='25', weight='bold')

    # make buttons
    text_shuffle = StringVar()
    text_shuffle.set('shuffle')
    name_shuffle = 'shuffle'
    button_shuffle = Button(gui, text=f'shuffle ', name=str(name_shuffle),
                            bg='white', fg='black', font=font, height=2, width=5,
                            command=lambda: shuffle())
    button_shuffle.configure(bg='coral')
    button_shuffle.grid(row=4, column=3)

    # the key argument name is used to identify the button
    gui.nametowidget(name_shuffle).configure(bg='white')
    for i in range(0, 4):
        for j in range(0, 4):
            if i == 3 and j == 3:
                texti = StringVar()
                texti.set('0')
                namei = 0
                button0 = Button(gui, text=f' ', name=str(namei),
                                 bg='white', fg='black', font=font, height=2, width=5,
                                 command=lambda: clickButton(button0))
                button0.configure(bg='coral')

                # the key argument name is used to identify the button
                gui.nametowidget(namei).configure(bg='white')
                button0.grid(row=i, column=j)

            else:
                texti = StringVar()
                texti.set('' + str(i))
                namei = i * 4 + j + 1
                buttoni = Button(gui, text=f'{i * 4 + j + 1}', name=str(namei),
                                 bg='white', fg='black', font=font, height=2, width=5
                                 )
                buttoni.configure(bg='coral')
                buttoni["command"] = lambda button=buttoni: clickButton(button)
                # the key argument name is used to identify the button
                gui.nametowidget(namei).configure(bg='white')
                buttoni.grid(row=i, column=j)
            # add buttons to the window
            # use .grid() or .pack() methods

        # update the window
    gui.mainloop()
