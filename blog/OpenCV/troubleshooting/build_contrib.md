# Build OpenCV Extra Module 
The opencv_contrib's README tells the way to config cmake file. 

## Unable to download IPPICV
If it is caused by network connection timeout, you may modify the cmake config file in ippicv source code folder. change the download url to an available one. or download manually and set download path parameter. 

A modified cmake config file:
https://github.com/EthanNote/Blog/blob/master/OpenCV/cmake/ippicv.cmake
