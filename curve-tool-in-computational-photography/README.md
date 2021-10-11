# Implementation of Image Filters

The main objective for this project is to illustrate the effects image filters can have on an image and how the results will change when using varying sliding window sizes. Specifically, this project is meant to explain and implement the Box, the Sobel Edge Detector, and the Gaussian filters while utilizing two sliding window sizes: 3x3 and 7x7. 

## Report

The **Implementation of Image Filters** PDF is a report meants to discuss the observations made for each filter, the implementation details like the sliding window and convolution, and the testing process.

## Reference Images

The images in the project serve as reference images of what effect each the programs are meant to have on the original image. 

## C++ Programs

Each program is meant to implement a specific image filter and will use the 3x3 and 7x7 sliding window sizes.

- **file1.cpp**: Applies box filter without the use of any OpenCV built-in functions
- **file2.cpp**: Applies the box filter with the user of the OpenCV built-in functions
- **file3.cpp**: Applies the Sobel Edge Detector filter by primarily focusing on the x-axis (horizontal) edges without the use of the OpenCV built-in function
- **file4.cpp**: Applies the Sobel Edge Detector filter by primarily focusing on the y-axis (vertical) edges without the use of the OpenCV built-in function
- **file5.cpp**: Applies the Sobel Edge Detector filter involving the x-axis and y-axis edges without the use of the OpenCV built-in function
- **file6.cpp**: Applies the Sobel Edge Detector filter involving both the x- and y-axis with the use of the OpenCV built-in function
- **file7.cpp**: Applies the Gaussian filter with the use of the OpenCV built-in function.
