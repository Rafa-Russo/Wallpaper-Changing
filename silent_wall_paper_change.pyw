import ctypes
import os
import random


def path():
    """Reads the path from the path.txt file and returns it as a string.

    Returns:
        path_str (str): The path to the folder containing the screenshots.
        """
    with open("path.txt", "r") as f:
        path_str = f.read()

    if path_str[-1] != "\\":
        path_str += "\\"

    return path_str


def get_screenshots(path_str):
    """Returns a list of all the screenshots in the folder.

    Args:
        path_str (str): The path to the folder containing the screenshots.

    Returns:
        screenshots (list): A list of all the screenshots in the folder.
        """
    screenshots = os.listdir(path_str)
    return screenshots


def get_random_screenshot(screenshots):
    """Returns a random screenshot from the list of screenshots.

    Args:
        screenshots (list): A list of all the screenshots in the folder.

    Returns:
        random_screenshot (str): A random screenshot from the list of screenshots.
        """
    random_screenshot = random.choice(screenshots)
    return random_screenshot


def set_wallpaper(path_str, random_screenshot):
    """Sets the wallpaper to the random screenshot.

    Args:
        path_str (str): The path to the folder containing the screenshots.
        random_screenshot (str): A random screenshot from the list of screenshots.
        """
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, str(path_str + random_screenshot), 0)


if __name__ == "__main__":
    path_str = 'path\\to\\silent script\\'  # Needs a trailing backslash
    screenshots = get_screenshots(path_str)
    random_screenshot = get_random_screenshot(screenshots)
    set_wallpaper(path_str, random_screenshot)
