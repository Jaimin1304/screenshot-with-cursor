import cv2
import numpy as np
import pyautogui
import keyboard
import os
import time
from cursor_state import get_current_cursor


def capture_screenshot_with_cursor():
    # Create screenshots directory if it doesn't exist
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    # Capture the screen using pyautogui
    screenshot = pyautogui.screenshot()
    
    # Save current cursor state
    cursor_state = get_current_cursor()
    print(f'current cursor state: {cursor_state}')

    # Convert the screenshot to a numpy array (which OpenCV uses)
    img = np.array(screenshot)

    # Convert RGB to BGR (OpenCV uses BGR by default)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Get the current position of the mouse cursor using pyautogui
    cursor_x, cursor_y = pyautogui.position()

    # Draw a simple cursor on the screenshot (a small white circle)
    cv2.circle(img, (cursor_x, cursor_y), 10, (255, 255, 255), -1)

    # Generate the base filename using the current timestamp
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    base_filename = f"screenshot_{timestamp}"

    # Generate a unique filename to avoid overwriting
    output_file = os.path.join("screenshots", f"{base_filename}.png")
    counter = 1
    while os.path.exists(output_file):
        output_file = os.path.join("screenshots", f"{base_filename}_{counter}.png")
        counter += 1

    # Save the final image in the screenshots directory with the unique filename
    cv2.imwrite(output_file, img)
    print(f"Screenshot saved as {output_file}")


def on_hotkey():
    capture_screenshot_with_cursor()


def main():
    print("Press 'Ctrl+Shift+K' to capture a screenshot with the cursor.")
    # Register the hotkey
    keyboard.add_hotkey("ctrl+shift+k", on_hotkey)

    # Wait for the user to press ESC to exit the program
    print("Press 'ESC' to exit.")
    keyboard.wait("esc")


if __name__ == "__main__":
    main()
