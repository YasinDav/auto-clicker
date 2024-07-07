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
        num_click = int(input("Enter number for click : "))
        again = False
    except:
        print("only you can enter umber")

again = True
while again:
    try:
        num_again = int(input("Enter number for again : "))
        again = False
    except:
        print("only you can enter umber")

again = True
while again:
    try:
        num_sleep = int(input("Enter number for sleep : "))
        again = False
    except:
        print("only you can enter umber")


for j in range(num_again):
    for i in range(num_click):
        X = random.randint(-20, 20)
        Y = random.randint(-30, 30)
        p.click(position[x]+X, position[y]+Y)
    p.sleep(num_sleep)
