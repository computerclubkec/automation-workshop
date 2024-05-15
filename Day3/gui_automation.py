import pyautogui
import time
import os

# Change directory to the script's directory
os.chdir(os.path.dirname(__file__))

# Paths to images
moles = ["assets/mole1.png", "assets/mole2.png"]
START_BUTTON = "assets/start_button.png"
CONTINUE_BUTTON = "assets/continue_button.png"

def click_button(image_path, button_name):
    """
    Locate and click a button on the screen.

    Parameters:
        image_path (str): Path to the button image.
        button_name (str): Name of the button for display purposes.
    """
    print(f"Locating {button_name} Button!")
    try:
        button_location = pyautogui.locateOnScreen(image_path, confidence=0.8)
        pyautogui.click(button_location)
    except pyautogui.ImageNotFoundException:
        print(f"Error locating {button_name} button!")

def whack_mole():
    """
    Whack moles on the screen.
    """
    for mole_image in moles:
        try:
            moles_location = pyautogui.locateOnScreen(mole_image, confidence=0.8)
            pyautogui.click(moles_location)
            print("Whacked!")
        except pyautogui.ImageNotFoundException:
            print("No Mole on Screen")

if __name__ == "__main__":
    click_button(CONTINUE_BUTTON, "Continue")
    click_button(START_BUTTON, "Start")
    while True:
        whack_mole()
        time.sleep(0.1)  # Small delay to prevent excessive CPU usage
