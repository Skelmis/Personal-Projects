import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()  # Get the size of the primary monitor.
print(f"Screen size: {screenWidth} x {screenHeight}")


def GetMouseCords():
    """
    A simple function which prints the current X & Y
    of the mouse every half a second for 10 seconds
    :return:
    """
    for i in range(20):
        (currentMouseX, currentMouseY,) = pyautogui.position()
        print(
            f"Current Mouse X: {currentMouseX: <4} | Current Mouse Y: {currentMouseY: <4}"
        )
        time.sleep(0.5)


def ClickOnStopButton():
    """
    Move the mouse to the stop button and click on it after 3 seconds
    :return:
    """
    time.sleep(3)
    pyautogui.leftClick("Stop Button.png")


def FindStopButton():
    """
    Finds the cords for the stop button and prints to screen
    :return:
    """
    leftX, topY, width, height = pyautogui.locateOnScreen("Stop Button.png")
    print(
        f"Left X: {leftX: <4} | Top Y: {topY: <4} | Width: {width: <4} | Height: {height: <4}"
    )


if __name__ == "__main__":
    FindStopButton()
    time.sleep(10)
