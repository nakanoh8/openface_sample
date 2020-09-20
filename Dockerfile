FROM ubuntu:16.04

RUN apt-get update && apt-get install -y sudo

# aptパッケージの更新
# 必要な apt パッケージのインストール
RUN sudo apt update && sudo apt upgrade -y && sudo apt install -y wget python-setuptools python-pip liblapack-dev libatlas-base-dev gfortran g++ build-essential libgtk2.0-dev libjpeg-dev libtiff5-dev libjasper-dev libopenexr-dev cmake python-dev python-numpy python-tk libtbb-dev libeigen3-dev yasm libfaac-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev libqt4-dev libqt4-opengl-dev sphinx-common texlive-latex-extra libv4l-dev libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev default-jdk ant libvtk5-qt4-dev unzip cmake git python-dev python-numpy libboost-dev libboost-python-dev libboost-system-dev
# 必要な pip パッケージのインストール
RUN sudo pip install -U pip && sudo pip install numpy==1.12.0 scipy matplotlib cython scikit-image dlib pandas txaio

# OpenCVのインストール
WORKDIR /root
RUN wget http://downloads.sourceforge.net/project/opencvlibrary/opencv-unix/3.0.0/opencv-3.0.0.zip
RUN unzip opencv-3.0.0.zip
WORKDIR /root/opencv-3.0.0
RUN cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D WITH_FFMPEG=OFF -D BUILD_opencv_python2=ON .
RUN make -j`nproc`
RUN sudo make install
RUN sudo cp lib/cv2.so /usr/local/lib/python2.7/site-packages/
RUN sudo ln /dev/null /dev/raw1394

# Torchのインストール
RUN git clone https://github.com/torch/distro.git ~/torch --recursive
WORKDIR /root/torch
RUN sudo dpkg --configure -a
RUN bash install-deps
RUN ./install.sh -y
RUN . /root/.bashrc
# RUN which th
RUN export PATH=/root/torch/bin:$PATH;
RUN export LD_LIBRARY_PATH=/root/torch/lib:$LD_LIBRARY_PATH;

# Torch用のLUAパッケージをインストール
# luarocksをビルドするのにlua**が必要になるため事前にインストール.
RUN sudo apt-get install lua5.3
RUN sudo apt-get install -y lua5.3-dev

#luarocksをインストール
RUN mkdir luarocks
WORKDIR /root/torch/luarocks
RUN wget https://luarocks.org/releases/luarocks-3.3.1.tar.gz
RUN tar -xf luarocks-3.3.1.tar.gz
WORKDIR /root/torch/luarocks/luarocks-3.3.1
RUN ./configure
RUN make
RUN make install

#LUAパッケージインストール
RUN for NAME in dpnn nn optim optnet csvigo cutorch cunn fblualib torchx tds image nngraph; do sudo /root/torch/install/bin/luarocks install $NAME; done

# OpenFaceのインストール
RUN git clone https://github.com/cmusatyalab/openface ~/openface --recursive
WORKDIR /root/openface
RUN sudo python setup.py install
RUN sudo python3 setup.py install

# 追加で必要なものをインストール
RUN ./models/get-models.sh
RUN ./demos/web/install-deps.sh
RUN sudo pip install -r demos/web/requirements.txt

WORKDIR /root
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
RUN sudo python3 get-pip.py && python3 -m pip install -U pip
RUN sudo apt-get install -y python3-dev
RUN python3 -m pip install opencv_python dlib


