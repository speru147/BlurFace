# BlurFace
## Face Detection and Blur

This Python script uses OpenCV to detect faces in images and automatically blur them.

## Features

- Face detection using Haar Cascade Classifier
- Automatic face blurring
- Support for single image processing
- Visual output with face detection boundary box

## Usage

1. Place your input image in the project directory (default filename: 'face.jpg')
2. Run the script:
```bash
python main.py
```

3. The script will:
   - Detect faces in the image
   - Draw blue rectangles around detected faces
   - Apply blur effect to the detected face regions
   - Display the result in a window

4. Press any key to close the display window

## How It Works

1. The script first converts the input image to grayscale
2. It uses a pre-trained Haar Cascade Classifier to detect faces
3. For each detected face:
   - Draws a boundary box
   - Extracts the face region
   - Applies a blur effect
   - Replaces the original face with the blurred version


## Acknowledgments

- Built with OpenCV
- OpenCV documentation and community
- Project created to understand image processing fundamentals

