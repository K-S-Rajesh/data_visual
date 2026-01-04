import pyautogui
import time
import random


# Set the fail-safe feature to False (use with caution)
# A fail-safe is built in by default: moving the mouse to a corner
# of the screen will stop the program. Highly recommended to keep this on.
# pyautogui.FAILSAFE = False

def move_mouse_randomly():
    """Moves the mouse slightly to a random position."""
    # Get the screen size to ensure movement is within bounds
    screen_width, screen_height = pyautogui.size()

    # Define a small range for movement (e.g., +/- 10 pixels from center-ish area)
    # This range can be adjusted as needed.
    move_range = 20

    # Calculate target position around the center of the screen
    current_x, current_y = pyautogui.position()
    target_x = current_x + random.randint(-move_range, move_range)
    target_y = current_y + random.randint(-move_range, move_range)

    # Ensure the target coordinates are within screen boundaries
    target_x = max(0, min(target_x, screen_width - 1))
    target_y = max(0, min(target_y, screen_height - 1))

    # Move the mouse instantly to avoid interfering with general usage
    pyautogui.moveTo(target_x, target_y, duration=0.1)


def main():
    """Main function to run the mouse movement every 5 minutes."""
    print("Mouse mover script started. Press Ctrl+C to stop.")
    try:
        while True:
            move_mouse_randomly()
            # Wait for 5 minutes (300 seconds)
            time.sleep(60)
    except KeyboardInterrupt:
        print("\nMouse mover script stopped.")


if __name__ == "__main__":
    main()