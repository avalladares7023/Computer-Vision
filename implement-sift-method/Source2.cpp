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
	cv::Mat dst6;	// Localized Key Point Image
	cv::Mat dst7;	// Orientation

	// Apply Gaussian Blurs for Octaves
	GaussianBlur(src, dst, Size(3, 3), 0, 0);
	GaussianBlur(src, dst2, Size(5, 5), 0, 0);
	GaussianBlur(src, dst3, Size(7, 7), 0, 0);
	GaussianBlur(src, dst4, Size(9, 9), 0, 0);

	//Apply SIFT key stage(s)
	auto detector = cv::xfeatures2d::SiftFeatureDetector::create();
	std::vector<cv::KeyPoint>keypoints;
	detector->detect(img, dst5);

	// Extract Localized Key Points
	auto extractor = cv::xfeatures2d::SiftFeatureDetector::create();
	extractor->compute(dst5, dst6);

	//Assign Orientation to Key Points
	vector<double> orien;
	vector<double> mag;
	for (k = 0; k < NUM_BINS; k++)
	{
		if (hist_orient[k] > 0.8 * max_peak)
		{
			double x1 = k - 1;
			double y1;
			double x2 = k;
			double y2 = hist_orient[k];
			double x3 = k + 1;
			double y3;

			if (k == 0)
			{
				y1 = hist_orient[NUM_BINS - 1];
				y3 = hist_orient[1];
			}
			else if (k == NUM_BINS - 1)
			{
				y1 = hist_orient[NUM_BINS - 1];
				y3 = hist_orient[0];
			}
			else
			{
				y1 = hist_orient[k - 1];
				y3 = hist_orient[k + 1];
			}
		}

		for (int i = 0; i < m_numOctaves; i++)
		{
			for (int j = 1; j < m_numIntervals + 4; j++)
			{
				printf("%f\t", m_absSigma[i][j - 1]);
			}
			printf("dst7");
		}
	}

	// Windows and Resulting Images
	cv::namedWindow("Original Image", cv::WINDOW_AUTOSIZE);
	cv::namedWindow("Key Localization", cv::WINDOW_AUTOSIZE);
	cv::namedWindow("Orientation Assignment", cv::WINDOW_AUTOSIZE);

	cv::imshow("Original Image", img);
	cv::imshow("Key Localization", dst6);
	cv::imshow("Orientation Assignment", dst7);

	return 0;