/* File Name: File 2 - ChangeBrightness.cpp
 * Name: Aimee Valladares
 * Date of Submission: 9/15/2020
 * Purpose: Change a given video's brightness by either increasing or decreasing it
 */

//Include statements
#include "stdafx.h"
#include <opencv2/opencv.hpp>
#include "opencv2/imgcodecs.hpp"
#include "opencv2/highgui.hpp"
#include <iostream>

using namespace cv;
using namespace std;

int main(int argc, char** argv)
{
    // Reads the video file and loads it through file path
    VideoCapture cap("C:/Users/valla/Documents/Courses/Computer Vision/Assignments/barries.mp4");
 
    // If statement meant to check for possible failures
    if (cap.isOpened() == false)
    {
        // If the video retrieval is not successful, exit the program
        cout << "Cannot open the video file" << endl;
        cin.get(); // Wait for user to press any key to exit
        return -1;
    }
 
    // Defining window names (variable) for the above videos
    String windowNameOriginalVideo = "Original Video";
    String windowNameBrightnessHigh50 = "Brightness Increased by 50";
    String windowNameWithBrightnessHigh100 = "Brightness Increased by 100";
    String windowNameBrightnessLow50 = "Brightness Decreased by 50";
    String windowNameBrightnessLow100 = "Brightness Decreased by 100";
 
    // Create and open windows for the above window names
    namedWindow(windowNameOriginalVideo, WINDOW_NORMAL);
    namedWindow(windowNameBrightnessHigh50, WINDOW_NORMAL);
    namedWindow(windowNameWithBrightnessHigh100, WINDOW_NORMAL);
    namedWindow(windowNameBrightnessLow50, WINDOW_NORMAL);
    namedWindow(windowNameBrightnessLow100, WINDOW_NORMAL);
 
    // A while loop to help calculate the change in brightness for the given video by
    // breaking it down to frames while also adding breaks to avoid possible errors like
    // an infinite loop
    while (true)
    {
        //Read a new frame from the video
        Mat frame;
        bool bSuccess = cap.read(frame);
 
        // If statement to break the while loop once the video has ended
        if (bSuccess == false)
        {
            cout << "The video has ended" << endl;
            break;
        }

        // Calculate the brightness adjustment in the given video by using convertTo function
        // convertTo(Output image, Type of output image, alpha, beta)
        // Beta - the brightness adjustment value
        Mat frameBrighnessHigh50;
        frame.convertTo(frameBrighnessHigh50, -1, 1, 50); // Increase the brightness by 50
        Mat frameBrighnessHigh100;
        frame.convertTo(frameBrighnessHigh100, -1, 1, 100); // Increase the brightness by 100
        Mat frameBrighnessLow50;
        frame.convertTo(frameBrighnessLow50, -1, 1, -50); // Decrease the brightness by 50
        Mat frameBrighnessLow100;
        frame.convertTo(frameBrighnessLow100, -1, 1, -100); // Decrease the brightness by 100
 
        //Show above frames inside the created windows.
        imshow(windowNameOriginalVideo, frame);
        imshow(windowNameBrightnessHigh50, frameBrighnessHigh50);
        imshow(windowNameWithBrightnessHigh100, frameBrighnessHigh100);
        imshow(windowNameBrightnessLow50, frameBrighnessLow50);
        imshow(windowNameBrightnessLow100, frameBrighnessLow100);
 
        // A break included based on user input and another way to stop the program from running
        // Break the while loop when 'Esc' key is pressed
        // Continue the loop when any other key is pressed or if any key is not pressed within 10 ms
        if (waitKey(10) == 27) // Wait for 10 ms until any key stroke
        {
            cout << "Esc key is pressed by user. Stopping the video" << endl;
            break;
        }
    }
    return 0;
}
