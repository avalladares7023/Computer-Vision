#include <iostream>
#include <opencv2/opencv.hpp>
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include <string>

using namespace cv;
using namespace std;

    int theObject[2] = { 0, 0 };

    // Bounding rectangle of the object, we will use the center of this as its position.
    Rect objectBoundingRectangle = Rect(0, 0, 0, 0);

    void searchForMovement(Mat thresholdImage, Mat &cameraFeed) {
        // Notice how we use the '&' operator for the cameraFeed. This is because we wish
        // to take the values passed into the function and manipulate them, rather than just working with a copy.
        // e.g. we draw to the cameraFeed in this function which is then displayed in the main() function.

        bool objectDetected = false;
        Mat temp;
        thresholdImage.copyTo(temp);
        
        // These two vectors needed for output of findContours
        vector<vector<Point>> contours;
        vector<Vec4i> hierarchy;

        // Find contours of filtered image using openCV findContours function
        // findContours(temp, conturs, hierarchy, CV_RETR_CCOMP, CV_CHAIN_APPROX_SIMPLE); // Retrieves all contours
        findContours(temp, contours, hierarchy, RETR_EXTERNAL, CHAIN_APPROX_SIMPLE); // Retrieves external contours

        // If contours vector is not empty, we have found some objects
        if (contours.size() > 0) {
            objectDetected = true;
        }
        else {
            objectDetected = false;
        }

        if (objectDetected) {
            // The largest contour is found at the end of the contours vector
            // We will simply assume that the biggest contour is the object we are looking for.
            vector <vector<Point>> largestContourVec;
            largestContourVec.push_back(contours.at(contours.size() - 1));

            // Make a bounding rectangle around the largest contour then find its centroid
            // This will be the object's final estimated position.
            objectBoundingRectangle = boundingRect(largestContourVec.at(0));
            int xpos = objectBoundingRectangle.x + objectBoundingRectangle.width / 2;
            int ypos = objectBoundingRectangle.y + objectBoundingRectangle.height / 2;

            // Update the objects position by changing the "theObject" array values
            theObject[0] = xpos, theObject[1], ypos;
        }

        // Make some temp x and y variables so we don't have to type out so much
        int x = theObject[0];
        int y = theObject[1];

        // Draw some crosshairs on the object
        circle(cameraFeed, Point(x, y), 20, Scalar(0, 255, 0), 2);
        line(cameraFeed, Point(x, y), Point(x, y - 25), Scalar(0, 255, 0), 2);
        line(cameraFeed, Point(x, y), Point(x, y + 25), Scalar(0, 255, 0), 2);
        line(cameraFeed, Point(x, y), Point(x - 25, y), Scalar(0, 255, 0), 2);
        line(cameraFeed, Point(x, y), Point(x + 25, y), Scalar(0, 255, 0), 2);

        // putText(cameraFeed, "Tracking object at (" + , Point(x, y), 1, 1, Scalar(0, 0, 255), 2);
    }


int main(int argc, char** argv) 
{
    // Capture the video from web cam
    VideoCapture cap(0);

    // If not success, then exit the program
    if (!cap.isOpened())
    {
        cout << "Cannot open the web cam" << endl;
        return -1;
    }

    // Create a "Control" window
    namedWindow("Control", WINDOW_NORMAL);

    int iLowH = 0;
    int iHighH = 179;

    int iLowS = 0;
    int iHighS = 255;

    int iLowV = 0;
    int iHighV = 255;

    // Create trackbars in the "Control window
    createTrackbar("Low H", "Control", &iLowH, 179); // Hue (0 - 179)
    createTrackbar("High H", "Control", &iHighH, 179); 
    createTrackbar("Low S", "Control", &iLowS, 255); // Saturation (0 - 255)
    createTrackbar("High S", "Control", &iHighS, 255); 
    createTrackbar("Low V", "Control", &iLowV, 255); // Value (0 - 255)
    createTrackbar("High V", "Control", &iHighV, 255);

    while (true) 
    {
        Mat imgOriginal;

        // Read a new frame from video
        bool bSuccess = cap.read(imgOriginal);

        // if not successful, break the loop
        if (!bSuccess)
        {
            cout << "Cannot read a frame from the video stream" << endl;
            break;
        }

        Mat imgHSV;

        // Convert the aptured frame from BGR to HSV
        cvtColor(imgOriginal, imgHSV, COLOR_BGR2HSV);

        Mat imgThresholded;

        // Threshold the image
        inRange(imgHSV, Scalar(iLowH, iLowS, iLowV), Scalar(iHighH, iHighS, iHighV), imgThresholded);

        // Morphological opening (remove small objects from the foreground)
        erode(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)));
        dilate(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)));

        // Morphological closing (fill small holes in the foreground)
        dilate(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)));
        erode(imgThresholded, imgThresholded, getStructuringElement(MORPH_ELLIPSE, Size(5, 5)));
        searchForMovement(imgThresholded, imgOriginal);
        imshow("Threshold Image", imgThresholded);
        imshow("Original", imgOriginal);

        if (waitKey(30) == 27)
        {
            cout << "esc key is pressed by user" << endl;
            break;
        }
    }
    return 0;
}