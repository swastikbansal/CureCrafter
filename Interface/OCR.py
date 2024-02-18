import pytesseract
from pytesseract import Output
import cv2
import csv
import re


def ocr(img_path):
    img = cv2.imread(img_path)
    print(img_path)
    myconfig = r"--psm 11 --oem 3"

    # Update the image path
    # img_path = r'img_path'

    # Check if the image is loaded successfully
    if img is None:
        print(f"Error: Unable to read the image at {img_path}")
    else:
        # 1. Rotate the image if needed
        # Your rotation code here

        # 2. Convert the image to grayscale
        # gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 3. Apply OCR on the grayscale image
        data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)

        detected_words = []  # List to store filtered words

        amount_boxes = len(data["text"])
        for i in range(amount_boxes):
            if float(data["conf"][i]) > 20:
                detected_word = data["text"][i]
                # Replace special characters (except alphanumeric and space) with a space
                cleaned_word = re.sub(r"[^a-zA-Z0-9 ]", " ", detected_word)
                # Check conditions for valid medicine names
                if cleaned_word.strip() and len(cleaned_word) >= 4 and cleaned_word.lower() not in {"tablet","capsule","ear","drops","injection"}:
                    detected_words.append(cleaned_word)

        # Read CSV file with explicit encoding specification
        csv_file_path = (
            "Interface\Chatbot\Datasets\medicine_data.csv"  # Update with your CSV file path
        )
        with open(csv_file_path, "r", encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip the header row and store it for reference

            # Perform search for each word in the list
            for word in detected_words:
                found = False
                csv_file.seek(
                    0
                )  # Reset the file pointer to the beginning for each search
                for row in csv_reader:
                    current_word = row[
                        1
                    ]
                    list_of_words=current_word.split()
                    lower_list=[element.lower() for element in list_of_words]
                    
                    if word.lower() in lower_list:
                        found = True
                        return row

            if not found:
                return "medicine not found in the data file."
