import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)

#gets message
def get_message():
    global x, y
    position = pt.locateOnScreen("whatsapp/smile_clip.jpg", confidence = .6)
    x = position[0]
    y = position[1]
    pt.moveTo(x,y, duration=.05)
    pt.moveTo(x + 85, y-50, duration = .5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(15, -120)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("message reveived: " + whatsapp_message)
    return whatsapp_message

#posts
def post_response(message):
    global x, y
    position = pt.locateOnScreen("whatsapp/smile_clip.jpg", confidence = .6)
    x = position[0]
    y = position[1]
    pt.moveTo(x+200, y + 20, duration= .5)
    pt.click()
    pt.typewrite(message, interval= 0.01)
    #pt.typewrite("\n", interval= 0.01)

# processes post_response
def process_response(message):
    random_no = random.randrange(3)
    if "?" in str(message).lower():
        return "Don't ask me any question"
    else:
        if random_no == 0:
            return "That's cool!"
        elif random_no == 1:
            return "remember to subscribe to code palace!"
        else:
            return "I want to eat something."

 
# check for new messages
def check_for_new_messages():
    pt.moveTo(x +80,y-35)
    while True:
        #continuously check for green dot and new messages
            position = pt.locateOnScreen("whatsapp/green_dot.jpg", confidence=.9)
            pt.moveTo(position)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
            else:
                print("no new other users with new messages located")
            if pt.pixelMatchesColor(int(x+80), int(y-35), (255,255,255), tolerance=10):
                print("is_white")
                processed_message = process_response(get_message())
                post_response(processed_message)
                sleep(3)
check_for_new_messages()