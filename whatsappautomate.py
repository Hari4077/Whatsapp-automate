import pyautogui
import webbrowser
import time
person_name=input("enter the nameyou want:")
msg=input("enter the message:")
webbrowser.open('https://web.whatsapp.com/')
time.sleep(10)
print(pyautogui.position())
pyautogui.click(249,197)
pyautogui.typewrite(person_name)
time.sleep(5)
pyautogui.click(319,448)
time.sleep(5)
pyautogui.typewrite(msg)
time.sleep(3)
pyautogui.click(1720,972)
