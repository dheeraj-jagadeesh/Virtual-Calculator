import cv2 as cv
from cvzone.HandTrackingModule import HandDetector


class Button:
    def __init__(self, pos, width, height, value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value

    def draw(self, img):
        # Draw button
        cv.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (225, 225, 225), cv.FILLED)
        cv.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (50, 50, 50), 3)
        cv.putText(img, self.value, (self.pos[0] + 40, self.pos[1] + 60), cv.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)

    def checkClick(self, x, y, img):
        # Check if the click is within button bounds
        if self.pos[0] < x < self.pos[0] + self.width and self.pos[1] < y < self.pos[1] + self.height:
            # Highlight button when clicked
            cv.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (255, 255, 255), cv.FILLED)
            cv.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (50, 50, 50), 3)
            cv.putText(img, self.value, (self.pos[0] + 25, self.pos[1] + 80), cv.FONT_HERSHEY_PLAIN, 5, (0, 0, 0), 5)
            return True
        else:
            return False

# Initialize webcam
cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Button values and creation
buttonListValues = [['7', '8', '9', '*'],
                    ['4', '5', '6', '-'],
                    ['1', '2', '3', '+'],
                    ['0', '/', '.', '=']]
buttonList = [Button((x * 100 + 800, y * 100 + 150), 100, 100, buttonListValues[y][x]) for y in range(4) for x in range(4)]

# Variables
myEquation = ''
delayCounter = 0

# Main loop
while True:
    success, img = cap.read()
    img = cv.flip(img, 1)  # Flip horizontally

    # Detect hands
    hands, img = detector.findHands(img, flipType=False)

    # Draw all buttons
    cv.rectangle(img, (800, 70), (800 + 400, 70 + 100), (225, 225, 225), cv.FILLED)
    cv.rectangle(img, (800, 70), (800 + 400, 70 + 100), (50, 50, 50), 3)
    for button in buttonList:
        button.draw(img)

    # Check for hand presence
    if hands:
        lmList = hands[0]['lmList']
        length, _, img = detector.findDistance(lmList[8][:2], lmList[12][:2], img)
        x, y = lmList[8][:2]

        if length < 50:
            for button in buttonList:
                if button.checkClick(x, y, img) and delayCounter == 0:
                    myValue = button.value
                    if myValue == "=":
                        try:
                            myEquation = str(eval(myEquation))
                        except:
                            myEquation = "Error"
                    else:
                        myEquation += myValue
                    delayCounter = 1

    # Avoid duplicate clicks
    if delayCounter != 0:
        delayCounter += 1
        if delayCounter > 20:
            delayCounter = 0

    # Display the equation/result
    cv.putText(img, myEquation, (810, 130), cv.FONT_HERSHEY_PLAIN, 3, (50, 50, 50), 3)

    # Display the image
    cv.imshow("Image", img)
    if cv.waitKey(1) & 0xFF == ord('d'):
        break

    key = cv.waitKey(1)
    if key == ord('c'):
        myEquation = ''

# Release resources
cap.release()
cv.destroyAllWindows()
