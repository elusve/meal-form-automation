import pyautogui
import time

# main
def main():

    #getPos() # used for testing to get the mouse position
    automation(2)

# meal can either be breakfast or lunch
def mealType(type: int, origin: int) -> None:
    
    if type == 1: # breakfast
        pyautogui.leftClick(142, 808)
        origin = scrollBar(origin, 25)
        pyautogui.leftClick(142, 478)
        pyautogui.leftClick(142, 823)
        origin = scrollBar(origin, 30)
        pyautogui.leftClick(142, 478)
        pyautogui.leftClick(142, 817)
        origin = scrollBar(origin, 10)
        pyautogui.leftClick(142, 442)
        pyautogui.leftClick(142, 781)
        scrollBar(origin, 100)
        pyautogui.leftClick(163, 630)
        #pyautogui.leftClick(163, 752)
    else: # lunch
        pyautogui.leftClick(142, 860)
        origin = scrollBar(origin, 25)
        pyautogui.leftClick(142, 390)
        pyautogui.leftClick(142, 727)
        origin = scrollBar(origin, 20)
        pyautogui.leftClick(142, 464)
        pyautogui.leftClick(142, 811)
        origin = scrollBar(origin, 20)
        pyautogui.leftClick(142, 381)
        pyautogui.leftClick(142, 724)
        scrollBar(origin, 120)
        pyautogui.leftClick(167, 540)
        #pyautogui.leftClick(167, 662)

# using the scroll bar
def scrollBar(origin: int, change: int) -> int:

    pyautogui.moveTo(1909, origin)
    newPos = origin + change
    pyautogui.mouseDown(1909, newPos)
    time.sleep(1)
    pyautogui.mouseUp()
    return newPos # returns new mouse position

# clicks on text box and fills it in with 1st string arg
def boxAns(input: str, x: int, y: int) -> None:

    pyautogui.leftClick(x, y)
    time.sleep(0.2)
    pyautogui.write(input)
    time.sleep(0.2)

# fills out meal form
def automation(mealChoice: int) -> None:

    time.sleep(3)
    pyautogui.leftClick(1234, 156) 
    time.sleep(3)

    scrollBarPos = scrollBar(254, 290)
    boxAns("John", 142, 322)
    boxAns("Doe", 971, 322)
    boxAns("123456789", 142, 576)
    pyautogui.leftClick(142, 775)
    boxAns("123-456-7890", 142, 974)
    scrollBarPos = scrollBar(scrollBarPos, 110)
    boxAns("johndoe@gmail.com", 142, 437)
    boxAns("13/01/2026", 142, 650)
    mealType(mealChoice, scrollBarPos)

# retrieves mouse position
def getPos() -> None:

    time.sleep(5)
    print(pyautogui.position())


main()