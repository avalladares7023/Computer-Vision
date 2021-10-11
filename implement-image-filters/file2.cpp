// File 2 - Box Filter WITH Built-in Function
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

    // Use the boxFilter function(src, dst, ddepth, size)
    // src - input image
    // dst - output image
    // ddepth - the output image depth
    // size - the blurring kernel size
    cv::boxFilter(src, dst, -1, cv::Size(3, 3));
    cv::boxFilter(src, dst2, -1, cv::Size(7, 7));

    // Create and open the windows for the window names
    cv::namedWindow("Original Image");
    cv::namedWindow("Box Filter with 3x3 Sliding Window");
    cv::namedWindow("Box Filter with 7x7 Sliding Window");

    // Display the image in the created windows
    cv::imshow("Original Image", src);
    cv::imshow("Box Filter with 3x3 Sliding Window", dst);
    cv::imshow("Box Filter with 7x7 Sliding Window", dst2);
    cv::waitKey(0);

    // Create a jpg with the filter applied
    cv::imwrite("Box Filter with 3x3 Sliding Window.jpg", dst);
    cv::imwrite("Box Filter with 7x7 Sliding Window.jpg", dst2);

    return 0;
}
