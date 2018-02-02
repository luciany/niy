@echo off

cd ..
@del test.exe

rem nvcc --version

set path=^
C:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\IDE;^
C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin;^
C:\Program Files (x86)\Microsoft SDKs\Windows\v7.1A\Bin\;^
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.1\bin;^
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.1\libnvvp;^
C:\Windows\System32

set include=^
C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\include;^
C:\Program Files (x86)\Microsoft SDKs\Windows\v7.1A\Include;^
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.1\include

set lib=^
C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\lib;^
C:\Program Files (x86)\Microsoft SDKs\Windows\v7.1A\Lib;^
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.1\lib\x64

rem -arch=compute_60 -code=sm_60 ^

nvcc -Wno-deprecated-gpu-targets ^
-Xcompiler "/wd 4819 /nologo /W2 /O2 /MT" ^
-Xlinker "" ^
-o test.exe ^
-I"./" ^
-I"./src/inc" ^
src/test.cu


test.exe

pause