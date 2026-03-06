import cv2
import numpy as np
import matplotlib.pyplot as plt

#Function to generate the negative of an image
def negative_image(image):
    return cv2.bitwise_not(image)

#Function to apply smoothing filters to an image
def smooth_image(image, filter_type, kernel_size):
    if filter_type == 'soft':
        return cv2.blur(image, (kernel_size, kernel_size))
    elif filter_type == 'medium':
        return cv2.medianBlur(image, kernel_size)
    elif filter_type == 'hard':
        return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

#Function to apply Laplacian sharpening to an image
def laplacian_sharpen(image):
    #Define the Laplacian kernel for sharpening
    kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
    return cv2.filter2D(image, -1, kernel)

#Function to show the histogram of an image
def plot_histogram(image):
    #Calculate histogram using OpenCV function
    histogram = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.plot(histogram, color='black')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()

# Function for simple histogram matching between two images
def simple_histogram_matching(reference_image, input_image):
    #Calculate histograms of reference and input images
    hist_ref, _ = np.histogram(reference_image.flatten(), 256, [0, 256])
    hist_input, _ = np.histogram(input_image.flatten(), 256, [0, 256])

    #Calculate cumulative distribution functions (CDF) of histograms
    cdf_ref = hist_ref.cumsum()
    cdf_input = hist_input.cumsum()

    #Normalize CDFs to range [0, 255]
    cdf_ref = (cdf_ref - cdf_ref.min()) * 255 / (cdf_ref.max() - cdf_ref.min())
    cdf_input = (cdf_input - cdf_input.min()) * 255 / (cdf_input.max() - cdf_input.min())

    matched_image = np.interp(input_image.flatten(), cdf_input, cdf_ref).reshape(input_image.shape)

    #Ensure the pixel values of the matched image are within [0, 255]
    matched_image = np.clip(matched_image, 0, 255)

    matched_image = matched_image.astype(np.uint8)

    matched_hist, _ = np.histogram(matched_image.flatten(), 256, [0, 256])
    reference_hist, _ = np.histogram(reference_image.flatten(), 256, [0, 256])

    return matched_image, matched_hist, reference_hist

def main():
    image_files = ['cameraman.tif', 'house.tif']  # Add your image files here

    for image_file in image_files:
        input_image = cv2.imread(image_file, cv2.IMREAD_GRAYSCALE)

        while True:
            print(f"\nMENU for {image_file}:")
            print("a. Display negative image")
            print("b. Smooth image")
            print("c. Sharpen image")
            print("d. Plot histogram")
            print("e. Histogram matching")
            print("f. Next image")
            print("g. Quit")

            choice = input("\nEnter your choice: ")

            if choice == 'a':
                #Show the negative image
                negative = negative_image(input_image)
                cv2.imshow('Negative Image', negative)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif choice == 'b':
                #Use smoothing filter for image
                filter_type = input("Choose filter type (soft, medium, hard): ")
                kernel_size = int(input("Enter kernel size (3, 9, 15): "))
                smoothed = smooth_image(input_image, filter_type, kernel_size)
                cv2.imshow('Smoothed Image', smoothed)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif choice == 'c':
                #Use Laplacian sharpening for image
                sharpened = laplacian_sharpen(input_image)
                cv2.imshow('Sharpened Image', sharpened)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif choice == 'd':
                #Show histogram of the image
                plot_histogram(input_image)
            elif choice == 'e':
                #Histogram matching with the 2nd image
                reference_image = cv2.imread('house.tif', cv2.IMREAD_GRAYSCALE)
                matched_image, matched_hist, reference_hist = simple_histogram_matching(reference_image, input_image)

                plt.plot(matched_hist, color='blue', label='Matched Histogram')
                plt.plot(reference_hist, color='red', label='Reference Histogram')
                plt.xlabel('Pixel Value')
                plt.ylabel('Frequency')
                plt.title('Histogram Matching')
                plt.legend()
                plt.show()

                cv2.imshow('Histogram Matched Image', matched_image.astype(np.uint8))
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            elif choice == 'f':
                print("Moving to next image...")
                break
            elif choice == 'g':
                print("Exiting program...")
                return
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()