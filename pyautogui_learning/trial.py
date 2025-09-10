import pyautogui as pg
import time
print(pg.size()) # Get the screen size

print(pg.position()) # Get the current mouse position

pg.moveTo(100,100, duration=1) # Move the mouse to (100,100) in 1 second

pg.moveRel(0,100, duration=1) # Move the mouse 100 pixels down from its current position

print(pg.position()) # Get the current mouse position

pg.click(100,100) # Click at (100,100)

# now lets draw a box using pyautogui 
time.sleep(5) #gives 7 sec time to switch between windows

pg.moveTo(200,200, duration=1) # Move the mouse to (100,100) in 1 second

# pg.scroll(200) # Scroll up 200 units

pg.dragRel(100,0, duration=1) # Move the mouse 100 pixels to the right

pg.dragRel(0,100, duration=1) # Move the mouse 100 pixels down

pg.dragRel(-100,0, duration=1) # Move the mouse 100 pixels to the left

pg.dragRel(0,-100, duration=1) # Move the mouse 100 pixels up

# moving to next box
pg.moveRel(200,0,duration=1) # Move the mouse 200 pixels to the right

# 2nd box drawing
pg.dragRel(100,0, duration=1) # Move the mouse 100 pixels right

pg.dragRel(0,100, duration=1) # Move the mouse 100 pixels down

pg.dragRel(-100,0, duration=1) # Move the mouse 100 pixels left

pg.dragRel(0,-100, duration=1) # Move the mouse 100 pixels up

# moving to next box
pg.moveRel(0,200,duration=1)

# 3rd box drawing
pg.dragRel(100,0,duration=1)# Move the mouse 100 pixels right

pg.dragRel(0,100, duration=1) # Move the mouse 100 pixels down

pg.dragRel(-100,0, duration=1) # Move the mouse 100 pixels left

pg.dragRel(0,-100, duration=1) # Move the mouse 100 pixels up

# moving to next box
pg.moveRel(-200,0,duration=1)

# 4th box drawing
pg.dragRel(100,0, duration=1)# Move the mouse 100 pixels right

pg.dragRel(0,100, duration=1) # Move the mouse 100 pixels down

pg.dragRel(-100,0, duration=1) # Move the mouse 100 pixels left

pg.dragRel(0,-100, duration=1) # Move the mouse 100 pixels up

pg.click(400,400)

pg.typewrite('print("hello world")', interval=0.25) 
pg.typewrite(["a", "left", "ctrlleft"])

pg.hotkey('shift',"3") # This will type the '#' character