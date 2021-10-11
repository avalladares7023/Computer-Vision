/* File Name: File 1 - ChangeContrast.cpp
 * Name: Aimee Valladares
 * Date of Submission: 9/15/2020
 * Purpose: Change a given video's contrast by either increasing or decreasing it
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
    VideoCapture cap("C:/Users/valla/Documents/Courses/Computer Vision/Assignments/barrier.mp4");
 
    // If statement meant to check for possible failures
    if (cap.isOpened() == false)
    {
        // If the video retrieval is not successful, exit the program
        cout << "Cannot open the video file" << endl;
        cin.get(); // Wait for user to press any key to exit
        return -1;
    }
 
    // Defining window names (variables) for the above videos
    String windowNameOriginalVideo = "Original Video";
    String windowNameContrastHigh20 = "Contrast Increased by 20";
    String windowNameContrastHigh40 = "Contrast Increased by 40";
    String windowNameContrastLow0_05 = "Contrast Decreased by 0.05";
    String windowNameContrastLow0_025 = "Contrast Decreased by 0.025";
 
    // Create and open windows for the above window names
    namedWindow(windowNameOriginalVideo, WINDOW_NORMAL);
    namedWindow(windowNameContrastHigh20, WINDOW_NORMAL);
    namedWindow(windowNameContrastHigh40, WINDOW_NORMAL);
    namedWindow(windowNameContrastLow0_05, WINDOW_NORMAL);
    namedWindow(windowNameContrastLow0_025, WINDOW_NORMAL);
 
    // A while loop to help calculate the change in contrast for the given video by
    // breaking it down to frames while also adding breaks to avoid errors like an
    // infinite loop.
    while (true)
    {
        // Read every new frame from the video
        Mat frame;
        bool bSuccess = cap.read(frame);
 
        // If statement to break the while loop once the video has ended
        if (bSuccess == false)
        {
            cout << "The video has ended" << endl;
            break;
        }
 
        // Calculate the contrast adjustment in the given video by using convertTo function
        // convertTo(Output image, Type of output image, alpha, beta)
        // Alpha - the contrast adjustment value
        Mat frameContrastHigh20;
        frame.convertTo(frameContrastHigh20, -1, 20, 0); // Increase the contrast by 20
        Mat frameContrastHigh40;
        frame.convertTo(frameContrastHigh40, -1, 40, 0); // Increase the contrast by 40
        Mat frameContrastLow0_05;
        frame.convertTo(frameContrastLow0_05, -1, 0.05, 0); // Decrease the contrast by 0.05
        Mat frameContrastLow0_025;
        frame.convertTo(frameContrastLow0_025, -1, 0.025, 0); // Decrease the contrast by 0.025
 
        //Show above frames inside the created windows.
        imshow(windowNameOriginalVideo, frame);
        imshow(windowNameContrastHigh20, frameContrastHigh20);
        imshow(windowNameContrastHigh40, frameContrastHigh40);
        imshow(windowNameContrastLow0_05, frameContrastLow0_05);
        imshow(windowNameContrastLow0_025, frameContrastLow0_025);
 
        // A break included based on user input and another way to stop the program from running
        // Break the while loop when 'Esc' key is pressed
        // Continue the loop when any other key is pressed or if any key is not pressed within 10 ms
        if (waitKey(10) == 27) //Wait for 10 ms until any key stroke
        {
            cout << "Esc key is pressed by user. Stopping the video" << endl;
            break;
        }
    }
    return 0;
}