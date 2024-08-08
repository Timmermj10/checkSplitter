from imutils.perspective import four_point_transform
import pytesseract
import argparse
import imutils
import cv2
import re
from PIL import Image
import cv2
import numpy as np

# Path to Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def preprocess_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at path: {image_path}")

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a binary threshold to the image
    _, thresh_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return thresh_image

def extract_text_from_image(image):
    # Convert the image to a PIL Image
    pil_image = Image.fromarray(image)

    # Perform OCR on the preprocessed image
    text = pytesseract.image_to_string(pil_image)
    cleaned_text = text.strip()

    return cleaned_text

def extract_receipt_details(text):
    # Regular expression to find prices
    price_pattern = re.compile(r'([0-9]+\.[0-9]+)')

    # Split the text into lines
    lines = text.split('\n')

    # Find all lines with a price and the greatest price
    lines_with_prices = []
    total = 0.0
    for line in lines:
        match = price_pattern.search(line)
        if match:
            price = float(match.group(1))
            lines_with_prices.append(line)
            if price > total:
                total = price

    # Find the first line with a price
    first_price_index = None
    for i, line in enumerate(lines):
        if price_pattern.search(line):
            first_price_index = i
            break

    # If no price found, return None
    if first_price_index is None:
        return None

    # Extract items between the first price and the first full line of space
    items = []
    for i in range(first_price_index, len(lines)):
        if lines[i].strip() == '':
            break
        parsed = lines[i].split(' ')
        price = parsed[len(parsed) - 1].replace('$', '')
        item = ' '.join(parsed[:len(parsed) - 1])
        items.append((item, price))

    # Create a dictionary to store the extracted details
    receipt_details = {
        "lines_with_prices": lines_with_prices,
        "items": items,
        "total": total
    }

    return receipt_details

if __name__ == "__main__":
    # Construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to input receipt image")
    args = vars(ap.parse_args())

    # Preprocess the image
    preprocessed_image = preprocess_image(args["image"])

    # Extract text from the preprocessed image
    extracted_text = extract_text_from_image(preprocessed_image)

    print("Extracted Text: ", extracted_text)

    # Extract receipt details
    receipt_details = extract_receipt_details(extracted_text)

    print("Receipt Details: ", receipt_details)

