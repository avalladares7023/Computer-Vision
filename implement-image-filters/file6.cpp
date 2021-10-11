// File 6 - Sobel Filter with the X-axis and Y-axis Edges
// WITH the Built-in Function
#include <opencv2/opencv.hpp>
#include <iostream>
using namespace std;
using namespace cv;

int main()
{
    // Read the image
    string imgFileName = "dog.bmp";

    // Load the image
    cv::Mat src = cv::imread(imgFileName);

    // If statement that will check for possible failures
    if (!src.data) {
        cout << "Unable to open file" << endl;
        getchar();
        return 1;
    }

    // Initialize output variables 
    cv::Mat dst;
    cv::Mat dst2;

    // Remove Noise by blurring the image with a Gaussian 
    // filter while applying the sliding windows

    GaussianBlur(src, dst, Size(3, 3), 0, 0);
    GaussianBlur(src, dst2, Size(7, 7), 0, 0);

    // Use the Sobel function(src, dst, ddepth, dx, dy)
    // src - input image
    // dst - output image
    // ddepth – the output image depth
    // dx - an integer variable representing the x-derivative
    // dy - an integer variable representing the y-derivative
    cv::Sobel(src, dst, -1, 1, 1);
    cv::Sobel(src, dst2, -1, 1, 1);

    // Create and open the windows for the window names
    cv::namedWindow("Original Image");
    cv::namedWindow("Sobel Edge Filter with 3x3 Sliding Window");
    cv::namedWindow("Sobel Edge Filter with 7x7 Sliding Window");

    // Display the image in the created windows
    cv::imshow("Original Image", src);
    cv::imshow("Sobel Edge Filter with 3x3 Sliding Window", dst);
    cv::imshow("Sobel Edge Filter with 7x7 Sliding Window", dst2);
    cv::waitKey(0);

    // Create a jpg with the filter applied
    cv::imwrite("Sobel Edge Filter with 3x3 Sliding Window.jpg", dst);
    cv::imwrite("Sobel Edge Filter with 7x7 Sliding Window.jpg", dst2);

    waitKey(0);
    return 0;
}
