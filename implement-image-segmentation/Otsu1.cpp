#include <opencv2/opencv.hpp>
#include <iostream>
using namespace cv;
using namespace std;

// Class that converts the input image into a gray-level image for the thresholding segmentation
class Conversion
{
public:
    Conversion() {
        Mat image;
        Mat gray;

          cv::cvtColor(image, gray, COLOR_BGR2GRAY);
    }
};

// Applies the simple Otsu thresholding method with only one threshold
class Thresholding
{
public:
    Thresholding(){
        Mat gray;
        Mat thresh1;

            threshold(gray, thresh1, 0, 255, THRESH_BINARY + THRESH_OTSU);
    }

};

int main()
{
    // Initialize variables
    Mat image;      // Input image
    Mat gray;       // gray-level
    Mat thresh;     // Threshold

    // Read and Load the input image
    image = imread("edge_L-150x150.png", IMREAD_COLOR);
    cv::imshow("Original image", image);
    cv::waitKey();

    // Used to check for possible errors when reading and/or loading the input image
    if (image.empty()) {
        cout << "Error loading image" << endl;
        return -1;
    }

    // Declare object for class Conversion
    Conversion obj1;

    // Declare object for class Thresholding
    Thresholding obj2;

    // Displaying the images in the windows
    cv::imshow("Original Image", image);
    cv::imshow("Otsu's simple thresholding", thresh);

    // Create a jpg with the method applied
    cv::imwrite("Original Image", image);
    cv::imwrite("Otsu's-binarization implementation w/ 2 classes", thresh);

    cv::waitKey(0);
    return 0;
}