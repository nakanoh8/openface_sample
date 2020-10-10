FROM ubuntu:16.04

# aptパッケージの更新
# 必要な apt パッケージのインストール
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y tzdata && \
    apt-get install -y wget sudo python-setuptools \
    liblapack-dev libatlas-base-dev gfortran g++ build-essential \
    libgtk2.0-dev libjpeg-dev libtiff5-dev libopenexr-dev \
    libtbb-dev libeigen3-dev yasm libfaac-dev \
    libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev \
    libxvidcore-dev libx264-dev sphinx-common \
    texlive-latex-extra libv4l-dev libdc1394-22-dev libavcodec-dev \
    libavformat-dev libswscale-dev default-jdk ant unzip cmake \
    git python3-dev python3-pip libboost-dev libboost-python-dev \
    libboost-system-dev python-numpy python-tk software-properties-common libqt4-dev libqt4-opengl-dev
# RUN apt-get install -y libjasper-dev libvtk5-qt4-dev

# Torchのインストール
WORKDIR /root
RUN git clone https://github.com/torch/distro.git ~/torch --recursive
WORKDIR /root/torch
RUN sudo dpkg --configure -a
# COPY install-deps .
RUN bash install-deps
RUN ./install.sh -y
RUN . /root/.bashrc
RUN export PATH=/root/torch/bin:$PATH; && \
    export LD_LIBRARY_PATH=/root/torch/lib:$LD_LIBRARY_PATH;

# Torch用のLUAパッケージをインストール
# luarocksをビルドするのにlua**が必要になるため事前にインストール.
RUN sudo apt-get install -y lua5.3 lua5.3-dev
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
RUN for NAME in dpnn nn optim optnet csvigo cutorch cunn fblualib torchx tds image nngraph; \
    do sudo /root/torch/install/bin/luarocks install $NAME; done

# OpenFaceのインストール
RUN git clone https://github.com/cmusatyalab/openface ~/openface --recursive
WORKDIR /root/openface
RUN sudo python3 setup.py install
# 追加で必要なものをインストール
RUN ./models/get-models.sh
RUN git config --global url.https://github.com/.insteadOf git://github.com/
RUN ./demos/web/install-deps.sh

# python3でOpenFaceを動かすために必要なものをインストール
RUN python3 -m pip install -U pip && python3 -m pip install -y opencv_python dlib flask
WORKDIR /home


