from hashlib import new
import cv2
import numpy as np
from pyzbar.pyzbar import decode
from datetime import datetime
from unicodedata import decimal

# getting the camera
capture = cv2.VideoCapture(0)
capture.set(3,640)
capture.set(4,480)

while True:
    success, image = capture.read()
    for code in decode(image):
        # decoding the data as string
        theData = code.data.decode('utf-8')

        # creating a shape around the qrcode or barcode
        points = np.array([code.polygon], np.int32)
        points = points.reshape((-1,1,2))
        cv2.polylines(image,[points], True, (255,0,255), 5)

        # getting the date and time
        dateTime = datetime.now()
        formatDateAndTime = dateTime.strftime("Date: %B %d, %Y \nTime: %H:%M:%S")

        # generating a new text file
        newTextFile = open('assignment10.txt', 'w')
        newTextFile.write(f'{theData}\n\n{formatDateAndTime}')
        print(f'Preview: {theData}\n\n{formatDateAndTime}') # Preview

    cv2.imshow('Result', image)
    cv2.waitKey(1)