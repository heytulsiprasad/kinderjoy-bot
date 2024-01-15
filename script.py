import os
import time
import pyautogui
import tkinter as tk

# PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen.
pyautogui.FAILSAFE = False

# Get the screen size
screenWidth, screenHeight = pyautogui.size()

# Default time
interval = 1 * 60 # 1 mins
# interval = 2

counter = 1
play = False

def start():
    global play
    play = True
    label.config(text="STATUS: ON")
    print("Start Automation")
    automate()

def stop():
    global play
    label.config(text="STATUS: OFF")
    print("Stop Automation")
    play = False

def automate():
    global counter
    if play:
        # Move the mouse to bottom left cornor and click twice
        pyautogui.moveTo(0, screenHeight-1)
        pyautogui.click()
        pyautogui.click()

        # print("Ping number: " + str(counter))
        # counter += 1

        # Wait for the interval and run automate again
        root.after(interval*1000, automate) # tkinter uses milliseconds

# Create the main window
root = tk.Tk()

# Set window size
root.geometry("250x250")

# Give title to window
root.title("Kinderjoy")

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Create a "Start" button
start_button = tk.Button(button_frame, text="Start", command=start, font=("Arial", 16))
start_button.pack(side=tk.LEFT, padx=10)

# Create a "Stop" button
stop_button = tk.Button(button_frame, text="Stop", command=stop, font=("Arial", 16))
stop_button.pack(side=tk.LEFT, padx=10)

# Create a label
label = tk.Label(root, text="STATUS: OFF" , font=("Arial", 14))
label.pack(pady=20)

# Center the window
root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())

# Start the main loop
root.mainloop()