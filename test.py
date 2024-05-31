import keyboard  # Requires the `keyboard` module
import pyperclip as pc
# Main function to capture keyboard inputs
def capture_keyboard():
    while True:  # Infinite loop to keep the program running
        try:
            # Wait for the specific key combination
            keyboard.wait('ctrl+shift+space')
            print("Ctrl+Shift+Space was pressed.")
            print(pc.paste())
        except KeyboardInterrupt:  # Handle the Ctrl+C interruption
            print("Ctrl+C pressed. Exiting...")
            break  # Exit the loop

# Execute the function
capture_keyboard()
