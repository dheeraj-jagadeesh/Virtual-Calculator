# Hand Gesture Calculator

This project is a hand gesture-based calculator using OpenCV and the `cvzone` library for hand tracking.

## Features
- Perform basic arithmetic operations using hand gestures.
- Interactive GUI for entering equations and displaying results.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/dheeraj-jagadeesh/HandGestureCalculator.git
    ```

2. Navigate to the project directory:
    ```sh
    cd HandGestureCalculator
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

    **Note:** Create a `requirements.txt` file with the following contents:
    ```
    opencv-python
    cvzone
    ```

## Usage

1. Run the script:
    ```sh
    python hand_gesture_calculator.py
    ```

2. Use your hand to interact with the calculator buttons displayed on the screen.

### Controls
- **To clear the equation:** Press the `c` key on your keyboard.
- **To close the application:** Press the `d` key on your keyboard.

## Code Overview

### Button Class
A class representing a button on the calculator.

```python
class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, img):
        cv.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (225, 225, 225), cv.FILLED)
        cv.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (50, 50, 50), 3)
        cv.putText(img, self.value, (self.pos[0] + 40, self.pos[1] + 60), cv.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)

    def checkClick(self, x, y, img):
        if self.pos[0] < x < self.pos[0] + self.width and self.pos[1] < y < self.pos[1] + self.height:
            cv.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (255, 255, 255), cv.FILLED)
            cv.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (50, 50, 50), 3)
            cv.putText(img, self.value, (self.pos[0] + 25, self.pos[1] + 80), cv.FONT_HERSHEY_PLAIN, 5, (0, 0, 0), 5)
            return True
        return False
