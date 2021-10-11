// File 1 - Box Filter WITHOUT Built-in Function
#include <opencv2/opencv.hpp>
#include <iostream>
using namespace std;
using namespace cv;

int main()
{
    // Read the image
    string imgFileName = "dog.bmp";

    // Load the image and create copies for the modified images to be stored
    cv::Mat src = cv::imread(imgFileName);
    Mat src1 = src.clone();
    Mat src2 = src.clone();

    // If statement that will check for possible failures
    if (!src.data) {
        cout << "Unable to open file" << endl;
        getchar();
        return 1;
    }

    // Initialize mask size and intensity to help simulate the sliding window
    int maskSize1 = 3;
    int maskSize2 = 7;
    Scalar intensity1 = 0;
    Scalar intensity2;
    Scalar intensity3 = 0;
    Scalar intensity4;

    // a for loop used to count the number of rows and columns while 
    // applying a 3x3 Sliding Window
    for (int i = 0; i < src.rows - maskSize1; i++)
    {
        for (int j = 0; j < src.cols - maskSize1; j++)
        {
            for (int p = 0; p < maskSize1; p++)
            {
                for (int q = 0; q < maskSize1; q++)
                {
                    intensity1 = src.at<uchar>(i + p, j + q);
                    intensity2.val[0] += intensity1.val[0];
                }
            }

            src1.at<uchar>(i + (maskSize1 - 1) / 2, j + (maskSize1 - 1) / 2)
                = intensity2.val[0] / (maskSize1 * maskSize1);
        }
    }

    // a for loop used to count the number of rows and columns while 
    // applying a 7x7 Sliding Window
    for (int a = 0; a < src.rows - maskSize2; a++)
    {
        for (int b = 0; b < src.cols - maskSize2; b++)
        {
            for (int c = 0; c < maskSize2; c++)
            {
                for (int d = 0; d < maskSize2; d++)
                {
                    intensity3 = src.at<uchar>(a + c, b + d);
                    intensity4.val[0] += intensity3.val[0];
                }
            }

            src2.at<uchar>(a + (maskSize1 - 1) / 2, b + (maskSize1 - 1) / 2)
                = intensity4.val[0] / (maskSize2 * maskSize2);
        }
    }


    // Create and open the windows for the window names
    cv::namedWindow("Original Image");
    cv::namedWindow("Box Filter without function 3x3 Sliding Window");
    cv::namedWindow("Box Filter without function 7x7 Sliding Window");

    // Display the image in the created windows
    cv::imshow("Original Image", src);
    cv::imshow("Box Filter without function 3x3 Sliding Window", src1);
    cv::imshow("Box Filter without function 7x7 Sliding Window", src2);
    cv::waitKey(0);

    // Create a jpg with the filter applied
    cv::imwrite("Box Filter without function 3x3 Sliding Window.jpg", src1);
    cv::imwrite("Box Filter without function 7x7 Sliding Window.jpg", src2);

    waitKey(0);
    return 0;
}
