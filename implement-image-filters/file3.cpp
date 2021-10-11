// File 3 - Sobel Filter with the x-axis Edges
// WITHOUT the Built-in Function
#include <opencv2/opencv.hpp>
#include <iostream>
using namespace std;
using namespace cv;

// Calculate the y gradient vector at a given point in an image
// and then returns the gradient in the y direction
int yGradient(Mat image, int x, int y)
{
    return image.at<uchar>(y - 1, x - 1) +
        2 * image.at<uchar>(y - 1, x) +
        image.at<uchar>(y - 1, x + 1) -
        image.at<uchar>(y + 1, x - 1) -
        2 * image.at<uchar>(y + 1, x) -
        image.at<uchar>(y + 1, x + 1);
}

int main()
{
    // Read the image
    string imgFileName = "dog.bmp";

    // Load the image
    cv::Mat src = cv::imread(imgFileName);

    // Initialize Variables
    cv::Mat dst;
    cv::Mat dst2;
    int gx, gy, sum;

    // If statement that will check for possible failures
    if (!src.data) {
        cout << "Unable to open file" << endl;
        getchar();
        return 1;
    }

    // Remove Noise by blurring the image with a Gaussian 
    // filter while applying the sliding windows
    GaussianBlur(src, dst, Size(3, 3), 0, 0);
    GaussianBlur(src, dst2, Size(7, 7), 0, 0);

    for (int y = 0; y < src.rows; y++)
    {
        for (int x = 0; x < src.cols; x++)
        {
            dst.at<uchar>(y, x) = 0;
        }
    }

    for (int y = 0; y < src.rows; y++)
    {
        for (int x = 0; x < src.cols; x++)
        {
            dst2.at<uchar>(y, x) = 0;
        }
    }

    for (int y = 1; y < src.rows - 1; y++)
    {
        for (int x = 1; x < src.cols - 1; x++)
        {
            gy = yGradient(src, x, y);
            sum = abs(gx) + abs(gy);
            sum = sum > 255 ? 255 : sum;
            sum = sum < 0 ? 0 : sum;
        }
    }

    // Create and open the windows for the window names
    cv::namedWindow("Original Image");
    cv::namedWindow("Sobel Edge with Y-axis without function with 3x3 Sliding Window");
    cv::namedWindow("Sobel Edge with Y-axis without function with 7x7 Sliding Window");

    // Display the image in the created windows
    cv::imshow("Original Image", src);
    cv::imshow("Sobel Edge with Y-axis without function with 3x3 Sliding Window", dst);
    cv::imshow("Sobel Edge with Y-axis without function with 7x7 Sliding Window", dst2);
    cv::waitKey(0);

    // Create a jpg with the filter applied
    cv::imwrite("Sobel Edge with Y-axis without function with 3x3 Sliding Window.jpg", dst);
    cv::imwrite("Sobel Edge with Y-axis without function with 7x7 Sliding Window.jpg", dst2);

    waitKey(0);
    return 0;
}
