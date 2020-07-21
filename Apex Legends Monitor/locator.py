"""
This file is for the purposes of locating the
health bar and the relevant areas in game
"""
import json

import pyautogui
from pyautogui import ImageNotFoundException

from pathlib import Path
import time

from exceptions import *


class Locator:
    LEFT = 0
    TOP = 0
    WIDTH = 250
    HEIGHT = 60

    INITIALIZED = False

    def __init__(self):
        self.left = self.LEFT
        self.top = self.TOP
        self.width = self.WIDTH
        self.height = self.HEIGHT

        self.initialized = self.INITIALIZED
        self.cwd = self.GetCwd()

    @staticmethod
    def GetCwd():
        """
        A function to get the current path main.py
        """
        cwd = Path(__file__).parents[0]
        cwd = str(cwd)
        return cwd

    def IsInitialized(self):
        """
        Is simply used to check whether or not this instance
        has been initialized or not yet
        :return: -> None
        """
        if not self.initialized:
            raise InstanceNotInitialized

    def Initialize(self):
        """
        This should be called before using this class for the
        first time, this just sets up the relevant cords etc
        :return:
        """
        self.left, self.top, armour = self.LocateHealthAreaTopCords()

        with open("config.json", "r") as f:
            config = json.load(f)

        self.rgb = config[armour]
        print(f"Initialized for {armour} armour")

        self.initialized = True

    def LocateHealthAreaTopCords(self):
        """
        This function loops over all armour combinations to find
        the current top cords for the health bar area on screen
        so that we can further process things in the correct area

        :return: -> Returns an (x, y) tuple of the top left for the health area
        """
        allPossibleArmourImages = {
            "gold": "FullGoldArmourBar.PNG",
            "purple": "FullPurpleArmourBar.PNG",
            "blue": "FullBlueArmourBar.PNG",
            "white": "FullWhiteArmourBar.PNG",
            "evo 1": "Stage1EvoArmour.PNG",
            "evo 2": "Stage2EvoArmour.PNG",
            "evo 3": "Stage3EvoArmour.PNG",
            "evo 4": "Stage4EvoArmour.PNG",
        }
        for key, value in allPossibleArmourImages.items():
            try:
                imageLocation = pyautogui.locateOnScreen(
                    f"{self.cwd}/images/{value}", confidence=0.9
                )
            except ImageNotFoundException:
                continue
            else:
                if imageLocation is None:
                    continue
                return imageLocation[0], imageLocation[1], key
        else:
            raise HealthBarNotFound

    def ScreenshotHealthArea(self):
        """
        A learning function to find and screenshot the health area
        """
        nameLocation = pyautogui.locateOnScreen(
            f"{self.cwd}/images/name.PNG", confidence=0.9
        )
        left = nameLocation[0]
        top = nameLocation[1]
        width = 250
        height = 60

        im = pyautogui.screenshot(
            f"{self.cwd}/screenshots/health area.png",
            region=(left, top, width, height),
        )


if __name__ == "__main__":
    instance = Locator()
    instance.Initialize()
