import pyautogui as p
from keyboard import add_hotkey, wait
from tkinter import *
from tkinter import messagebox
import random

# print(p.displayMousePosition())
x=0
y=1
def select_pos():
    global position
    position = p.position()

add_hotkey("x", select_pos)
wait("x")
again = True
while again:
    try:
        num = int(input("Enter number for click : "))
        again = False
    except:
        print("only you can enter umber")
for i in range(num):
    X = random.randint(-20, 20)
    Y = random.randint(-30, 30)
    p.click(position[x]+X, position[y]+Y)
