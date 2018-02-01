#
# The script downloads ICV package
#
# On return this will define:
# OPENCV_ICV_PATH - path to unpacked downloaded package
#

function(download_ippicv root_var)
  # Commit SHA in the opencv_3rdparty repo
  set(IPPICV_BINARIES_COMMIT "81a676001ca8075ada498583e4166079e5744668")
  # Define actual ICV versions
  if(APPLE)
    set(OPENCV_ICV_PACKAGE_NAME "ippicv_macosx_20151201.tgz")
    set(OPENCV_ICV_PACKAGE_HASH "4ff1fde9a7cfdfe7250bfcd8334e0f2f")
    set(OPENCV_ICV_PLATFORM "macosx")
    set(OPENCV_ICV_PACKAGE_SUBDIR "/ippicv_osx")
  elseif(UNIX)
    if(ANDROID AND NOT (ANDROID_ABI STREQUAL x86 OR ANDROID_ABI STREQUAL x86_64))
      return()
    endif()
    set(OPENCV_ICV_PACKAGE_NAME "ippicv_2017u3_lnx_intel64_general_20170822.tgz")
    set(OPENCV_ICV_PACKAGE_HASH "808b791a6eac9ed78d32a7666804320e")
    set(OPENCV_ICV_PLATFORM "linux")
    set(OPENCV_ICV_PACKAGE_SUBDIR "/ippicv_lnx")
  elseif(WIN32 AND NOT ARM)
    set(OPENCV_ICV_PACKAGE_NAME "ippicv_windows_20151201.zip")
    set(OPENCV_ICV_PACKAGE_HASH "04e81ce5d0e329c3fbc606ae32cad44d")
    set(OPENCV_ICV_PLATFORM "windows")
    set(OPENCV_ICV_PACKAGE_SUBDIR "/ippicv_win")
  else()
    return() # Not supported
  endif()

  set(OPENCV_ICV_UNPACK_PATH "${CMAKE_CURRENT_LIST_DIR}/unpack")
  set(OPENCV_ICV_PATH "${OPENCV_ICV_UNPACK_PATH}${OPENCV_ICV_PACKAGE_SUBDIR}")

  message(STATUS "ICV: Package successfully downloaded")
  set(OPENCV_ICV_PATH "${OPENCV_ICV_PATH}" PARENT_SCOPE)
endfunction()
