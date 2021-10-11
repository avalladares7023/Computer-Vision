// File 7 - Gaussian Filter WITH Built-in Function
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

    // Use the boxFilter function(src, dst, size, sigmaX, sigmaY)
    // src - input image
    // dst - output image
    // size - the blurring kernel size
    // sigmaX - is the Gaussian kernel standard deviation in X direction
    // sigmaY - is the Gaussian kernel standard deviation in Y direction
    cv::GaussianBlur(src, dst, Size(3, 3), 0, 0);
    cv::GaussianBlur(src, dst2, Size(7, 7), 0, 0);

    // Create and open the windows for the window names
    cv::namedWindow("Original Image");
    cv::namedWindow("Gaussian Filter with 3x3 Sliding Window");
    cv::namedWindow("Gaussian Filter with 7x7 Sliding Window");

    // Display the image in the created windows
    cv::imshow("Original Image", src);
    cv::imshow("Gaussian Filter with 3x3 Sliding Window", dst);
    cv::imshow("Gaussian Filter with 7x7 Sliding Window", dst2);
    cv::waitKey(0);

    // Create a jpg with the filter applied
    cv::imwrite("Gaussian Filter with 3x3 Sliding Window.jpg", dst);
    cv::imwrite("Gaussian Filter with 7x7 Sliding Window.jpg", dst2);

    return 0;
}
