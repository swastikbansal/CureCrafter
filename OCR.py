import pytesseract
from pytesseract import Output  
import cv2

myconfig = r"--psm 6 --oem 3"

# Update the image path
img_path = r'E:\Downloads\drug_name1.jpg'

# Read the image
img = cv2.imread(img_path)

# Check if the image is loaded successfully
if img is None:
    print(f"Error: Unable to read the image at {img_path}")
else:
    # 1. Rotate the image if needed
    # Your rotation code here

    # 2. Convert the image to grayscale
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 3. Apply OCR on the grayscale image
    data = pytesseract.image_to_data(gray_img, config=myconfig, output_type=Output.DICT)

    amount_boxes = len(data['text'])
    for i in range(amount_boxes):
        if float(data['conf'][i]) > 20:
            (x, y, width, height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
            img = cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 2)
            img = cv2.putText(img, data['text'][i], (x, y + height + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)

    # Show the image with rectangles and text
    cv2.imshow("img", img)
    cv2.waitKey(0)
