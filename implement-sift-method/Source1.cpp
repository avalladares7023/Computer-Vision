#include <iostream>
#include <vector>
#include <opencv2/opencv.hpp>
#include <opencv2/features2d.hpp>  
#include <opencv2/xfeatures2d.hpp>  
#include <opencv2/highgui.hpp>

using namespace cv;
using namespace cv::xfeatures2d;
using namespace std;

int main()
{
	// Read and Load the image
	string img = "blocks_L-150x150-1.png";
	cv::Mat src = cv::imread(img);

	// If statement that will check for possible failures
	if (!src.data) {
		cout << "Unable to open file" << endl;
		getchar();
		return 1;
	}

	//Initialize output variables
	cv::Mat dst;
	cv::Mat dst2;
	cv::Mat dst3;
	cv::Mat dst4;
	cv::Mat dst5;	// Key Point Image

	// Apply Gaussian Blurs for Octaves
	GaussianBlur(src, dst, Size(3, 3), 0, 0);
	GaussianBlur(src, dst2, Size(5, 5), 0, 0);
	GaussianBlur(src, dst3, Size(7, 7), 0, 0);
	GaussianBlur(src, dst4, Size(9, 9), 0, 0);

	//Apply SIFT key stage(s)
	auto detector = cv::xfeatures2d::SiftFeatureDetector::create();
	std::vector<cv::KeyPoint>keypoints;
	detector->detect(img, dst5);

	// Windows and Resulting Images
	cv::namedWindow("Original Image", cv::WINDOW_AUTOSIZE);
	cv::namedWindow("Octave Image", cv::WINDOW_AUTOSIZE);
	cv::namedWindow("Extrema Detection", cv::WINDOW_AUTOSIZE);

	cv::imshow("Original Image", img);
	cv::imshow("Octave Image", dst, dst2, dst3, dst4);
	cv::imshow("Extrema Detection", dst5);

	return 0;
}