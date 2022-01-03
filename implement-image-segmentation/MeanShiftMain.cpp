#include <iostream>
#include "MeanShift.h"

int main() {
	// Load, Read image
	Mat Img = imread("S00-150x150.png");
	resize(Img, Img, Size(256, 256), 0, 0, 1);
	
	// Show that image
	namedWindow("The Original Picture");
	imshow("The Original Picture", Img);

	// Convert color from RGB to Lab
	cvtColor(Img, Img, COLOR_RGB2Lab);

	// Initilize Mean Shift with spatial bandwith and color bandwith
	MeanShift MSProc(12, 16);
	
	// Segmentation Process include Filtering Process (Region Growing)
	MSProc.MSSegmentation(Img);

	// Convert color from Lab to RGB then convert from RGB to Gray-level image
	cvtColor(Img, Img, COLOR_Lab2RGB);
	cvtColor(Img, Img, COLOR_RGB2GRAY);

	// Show the result image
	namedWindow("MS Picture");
	imshow("MS Picture", Img);

	waitKey();
	return 1;
}
