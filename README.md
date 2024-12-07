# Calculator Application

This project is a graphical calculator application built using the **CustomTkinter** library. The calculator allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division. It also provides a backspace functionality and supports input from both the keyboard and on-screen buttons.

## Features

- Perform basic arithmetic operations: addition, subtraction, multiplication, and division.
- Keyboard input support for numbers and operators.
- On-screen buttons for mouse interaction.
- Backspace functionality to delete the last entered character.
- Clear all functionality to reset the input field.
- Real-time result evaluation with the "Enter" key.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- `customtkinter` library.
- `Pillow` library (optional if using an icon).

### Steps

1. Clone this repository or copy the code.
2. Install the required libraries:
   ```bash
   pip install customtkinter
   ```
3. Place an icon file (e.g., `icon.ico`) in the same directory as the script if you want to customize the window icon.
4. Run the script using Python:
   ```bash
   python calculator.py
   ```

## How to Use

1. **On-screen Buttons:**

   - Click on the number or operator buttons to build your expression.
   - Press the `=` button to evaluate the result.
   - Use the `CE` button to clear the input field.

2. **Keyboard Input:**

   - Enter numbers and operators using your keyboard.
   - Press `Enter` to evaluate the result.
   - Press `Backspace` to remove the last entered character.

## Key Bindings

- `0-9`: Insert numbers into the input field.
- `+`, `-`, `*`, `/`: Insert operators into the input field.
- `Backspace`: Remove the last entered character.
- `Enter`: Evaluate the entered expression.

## Code Explanation

- **`insert_text`**** Function:**
  Handles inserting characters (numbers or operators) into the entry field based on keyboard input or button presses.

- **`remove_text`**** Function:**
  Removes the last character from the entry field when `Backspace` is pressed. Supports clearing the entire field with the `CE` button.

- **`evaluate_expression`**** Function:**
  Evaluates the mathematical expression entered in the field and displays the result.

- **CustomTkinter Buttons:**
  Each button is created using `CTkButton` from the CustomTkinter library and is assigned a specific position on the interface using `place()`.

## Layout

- **Entry Field:**

  - Positioned at the top of the window.
  - Displays the current expression or result.

- **Buttons:**

  - Numbers (`0-9`): Positioned in a grid layout.
  - Operators (`+`, `-`, `*`, `/`): Positioned to the right of the number buttons.
  - `=`: Positioned at the bottom right.
  - `CE`: Positioned to the left of the `=` button.

## Example

1. Input: `12 + 7`
2. Press `=` or `Enter`.
3. Output: `19` displayed in the entry field.

## Customization

- **Window Icon:**
  To customize the window icon, replace `icon.ico` with your own `.ico` file.

- **Button Appearance:**
  Modify the `width`, `height`, `font`, and `colors` of buttons in the `CTkButton` configuration.

## Screenshots

(Include screenshots of the application interface here.)

## Future Enhancements

- Add advanced mathematical operations (e.g., square root, percentage).
- Support for parentheses and operator precedence.
- Include a history feature to track previous calculations.

## License

This project is open-source and free to use.

---

Enjoy using this calculator! If you have any questions or suggestions, feel free to reach out.

