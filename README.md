# Image Parsing using EasyOCR

This repository demonstrates how to use [EasyOCR](https://github.com/JaidedAI/EasyOCR) to perform Optical Character Recognition (OCR) on images. EasyOCR is a Python-based library that provides a simple and effective way to extract text from images, supporting over 80 languages.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)

## Introduction
This project utilizes EasyOCR to parse and extract text from images. It can be used in various applications such as digitizing documents, text detection in images, or even real-time OCR applications.

## Features
- Easy-to-use OCR extraction from images
- Supports over 80 languages
- Lightweight and efficient implementation

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/image_parsing_using_EasyOCR.git
    cd image_parsing_using_EasyOCR
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **(Optional) Install EasyOCR separately if not listed in the `requirements.txt`:**
    ```bash
    pip install easyocr
    ```

## Usage

1. **Import the required modules:**
    ```python
    import easyocr
    import cv2  # OpenCV to read images
    ```

2. **Initialize the EasyOCR Reader:**
    ```python
    reader = easyocr.Reader(['en'])  # Specify the language code(s) here
    ```

3. **Read the image using OpenCV and apply OCR:**
    ```python
    image_path = 'path_to_image.jpg'
    result = reader.readtext(image_path)

    # Print the results
    for detection in result:
        print(f'Text: {detection[1]}, Confidence: {detection[2]}')
    ```

4. **Visualize the results (optional):**
    ```python
    # Draw bounding boxes using OpenCV
    image = cv2.imread(image_path)
    for (bbox, text, confidence) in result:
        top_left = tuple(map(int, bbox[0]))
        bottom_right = tuple(map(int, bbox[2]))
        image = cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
        image = cv2.putText(image, text, top_left, cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("Detected Text", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    ```

## Examples

- **Example 1:** Extracting text from a single image.
- **Example 2:** Visualizing OCR results with bounding boxes.
- **Example 3:** Extracting text in different languages.

You can find the example scripts in the `examples/` folder.

## Contributing

Contributions are welcome! If you have any improvements or suggestions, please create a pull request or open an issue.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
