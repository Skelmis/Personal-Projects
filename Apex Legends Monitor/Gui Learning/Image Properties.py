from PIL import Image
from pathlib import Path


def GetImageWidthHeight():
    """
    A function to get width and height of an image
    :return:
    """
    im = Image.open("bar area.PNG")
    width, height = im.size
    print(f"Width: {width: <4}px | Height: {height: <4}px")


def GetImagePixelColor():
    """
    A function to get the pixel color of an image
    :return:
    """
    cwd = Path(__file__).parents[1]
    cwd = str(cwd)

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
        im = Image.open(f"{cwd}/images/{value}")
        im = im.convert("RGB")

        width = im.size[0]
        height = im.size[1]

        print(im.getpixel((width / 2, height / 2)))


if __name__ == "__main__":
    GetImagePixelColor()
