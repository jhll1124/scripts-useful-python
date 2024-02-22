import keyboard
import pyautogui


while True:
    keyboard.wait('z')
    x, y = pyautogui.position()
    pyautogui.click(x, y, button='right')
    pyautogui.click(x, y, button='left')
    pyautogui.click(x, y, button='right')
