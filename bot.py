import pyautogui
import time
import keyboard

# The image you need to find on the screen
img_path = 'image.png'

# The location of the last click
last_click_location = None

# Key to stop the script when pressed
stop_key = 'q'

# Wait for the image to appear on the screen
while True:
    # Check if the key is pressed to stop
    if keyboard.is_pressed(stop_key):
        print("Script stopped by user.")
        break

    # Searching for an image on the screen
    location = pyautogui.locateOnScreen(img_path, confidence=0.9)

    # If an image is found, we click on its center
    if location:
        local_location = location
        center = pyautogui.center(local_location)
        pyautogui.mouseDown(center)

        last_click_location = center

        pyautogui.mouseUp()

        # Save the coordinates of the click location
        last_click_location = center
    else:
        # If no image is found, click on the last click location if there is one
        if last_click_location:
            pyautogui.click(last_click_location)

        print("The image was not found, let's try again..")
        time.sleep(0.5)
