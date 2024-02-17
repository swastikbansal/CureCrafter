import pytesseract
from pytesseract import Output
import cv2
import csv

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

    detected_words = []  # List to store filtered words

    amount_boxes = len(data['text'])
    for i in range(amount_boxes):
        if float(data['conf'][i]) > 20:
            detected_word = data['text'][i]
            # Check conditions for valid medicine names
            if not detected_word.isdigit() and detected_word.isalnum() and len(detected_word) >= 4:
                detected_words.append(detected_word)

    # Read CSV file with explicit encoding specification
    csv_file_path = 'E:\Downloads\modified_data.csv'  # Update with your CSV file path
    with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)  # Skip the header row and store it for reference

        # Perform binary search for each word in the list
        for word in detected_words:
            found = False
            for row in csv_reader:
                current_word = row[1]  # Assuming the second column is the medicine names

                if current_word == word:
                    found = True
                    # Print the data attributes
                    print(f"Sub-Category: {row[0]}, Product Name: {current_word}")

                    # Print data of other columns in the same row after the second column
                    for col_index in range(2, len(row)):
                        print(f"{header[col_index]}: {row[col_index]}")
                    break

            if not found:
                print(f"{word} not found in the CSV file.")
