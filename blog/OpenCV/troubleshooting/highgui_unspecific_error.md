# OpenCV Highgui Unspecific Error

编译一段用于显示摄像头图像的 opencv 程序， 运行时出现下面的异常


OpenCV Error: Unspecified error (The function is not implemented. Rebuild the library with Windows, GTK+ 2.x or Carbon support. If you are on Ubuntu or Debian, install libgtk2.0-dev and pkg-config, then re-run cmake or configure script) in cvShowImage, file /home/ethan/Downloads/opencv-master/modules/highgui/src/window.cpp, line 611
terminate called after throwing an instance of 'cv::Exception'


## 1. 重新 cmake, WITH_GTK_2_X 

然后 make, make install, 结果还是出现了同样的异常

## 2. apt install libgtk2.0-dev, 重做1

