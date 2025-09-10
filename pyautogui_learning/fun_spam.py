import pyautogui as pg
import time

# print(pg.position())
time.sleep(5)

pg.click(550,704)
a=15
while a!=0:
    pg.typewrite("hello",interval=0.2)
    pg.typewrite(['enter'])
    time.sleep(0.2)
    a=a-1