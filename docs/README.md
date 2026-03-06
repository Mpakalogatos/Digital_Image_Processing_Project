# Digital Image Processing - Project 1

This project is a Python-based image processing tool developed for the "Digital Image Processing" course. It provides a menu-driven interface to apply various transformation and filtering techniques to grayscale images.

## 🛠️ Features

The application implements the following image processing techniques:
- **Negative Transformation:** Inverts image colors using bitwise operations.
- **Image Smoothing:** Supports Soft (Averaging), Medium (Median), and Hard (Gaussian) blurring with customizable kernel sizes.
- **Laplacian Sharpening:** Enhances image edges using a Laplacian convolution kernel.
- **Histogram Visualization:** Generates and displays pixel intensity frequency plots.
- **Histogram Matching:** Adjusts the pixel distribution of an input image to match a reference image's profile.

## 🚀 Technologies Used
- **Python 3.x**
- **OpenCV (cv2):** For core image processing algorithms.
- **NumPy:** For matrix operations and kernel definitions.
- **Matplotlib:** For plotting histograms.
- **PyCharm:** Development environment.

## 📋 How to Use

1. **Setup:** Ensure you have the required libraries installed:
   ```bash
   pip install opencv-python numpy matplotlib
