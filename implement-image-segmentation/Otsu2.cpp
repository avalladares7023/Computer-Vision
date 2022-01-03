// Need to reformat

#include <opencv2/opencv.hpp>
#include <iostream>
using namespace std;
using namespace cv;

class Conversion
{
public:
    Conversion() {
        Mat image;
        Mat gray;
        Mat thresh1;

        cv::cvtColor(image, gray, COLOR_BGR2GRAY);
        cv::Sobel(image, gray, -1, 1, 1);
        GaussianBlur(image, gray, Size(3, 3), 0, 0);
    }
};

class Thresholding1
{
public:
    Thresholding1() {
        Mat image;
        Mat gray;
        Mat thresh1;

        threshold(gray, thresh1, 0, 150, THRESH_OTSU);
    }
};

class Thresholding2
{
public:
    Thresholding2() {
        Mat image;
        Mat gray;
        Mat thresh2;

        threshold(gray, thresh2, 151, 255, THRESH_OTSU);
    }

};

int main()
{
    // Read the image
    string imgFileName = "S01-150x150.png";

    // Load the image
    cv::Mat src = cv::imread(imgFileName);

    // If statement that will check for possible failures
    if (!src.data) {
        cout << "Unable to open file" << endl;
        getchar();
        return 1;
    }

    // Initialize output variables
    cv::Mat gray;
    cv::Mat thresh1;
    cv::Mat thresh2;
    cv::Mat thresh3;

    // Combining the threshold
    thresh3 = thresh1 + thresh2;

    // Create and open the windows for the window names
    cv::namedWindow("Original Image");
    cv::namedWindow("Otsu Implementation with Multiple Classes");


    // Display the image in the created windows
    cv::imshow("Original Image", src);
    cv::imshow("Otsu Implementation with Multiple Classes", thresh3);

    cv::waitKey(0);

    // Create a jpg with the filter applied
    cv::imwrite("Otsu Implementation with Multiple Classes.jpg",thresh3);

    waitKey(0);
    return 0;
}