# Ubuntu16.04 安裝 Anaconda/Tensorflow/Keras

## Install Anaconda
Download [Anaconda2](https://www.anaconda.com/products/individual#linux) for Python2.7 version.(本章節使用[Anaconda2-5.3.1-Linux-x86_64.sh](https://repo.anaconda.com/archive/Anaconda2-5.3.1-Linux-x86_64.sh))

After downloading Anaconda, go to the directory in located download file and enter the follow command.

    $ bash Anaconda2-x.x.x-Linux-x86_64.sh

Key `yes` `no` `no` to complete installed Anaconda.

Set the default Anaconda path in the `.bashrc` file.

    export PATH="/home/user_name/anaconda2/bin:$PATH"

Source the `.bashrc`

    $ source ~/.bashrc
    
Enter the below command.

    $ python -V
    
If Anaconda is installed, you can see `Python 2.7.xx :: Anaconda, Inc.`
    
## Install ROS dependency packages
To use ROS and Anaconda together, you must additionally install ROS dependency packages.

    $ pip install -U rosinstall msgpack empy defusedxml netifaces argparse pyhamcrest
    
## Install Tensorflow
    $ conda create -n tensorflow pip python=2.7
    $ pip install --ignore-installed --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.8.0-cp27-none-linux_x86_64.whl
This tutorial is used python 2.7(CPU only). If you want to use another python version and GPU, please refer to [TensorFlow](https://www.tensorflow.org/install/).

## Install Keras
[Keras](https://keras.io/) is a high-level neural networks API, written in Python and capable of running on top of TensorFlow.

    $ pip install keras==2.1.5

## Debug
* Warning message.

        tensorboard 1.8.0 has requirement bleach==1.5.0, but you'll have bleach 2.1.4 which is incompatible.
        tensorboard 1.8.0 has requirement html5lib==0.9999999, but you'll have html5lib 1.0.1 which is incompatible.
    
    Enter the below command.

        pip uninstall bleach
        pip install bleach==1.5.0
        
* Import Numpy error.

        ImportError: Something is wrong with the numpy installation. While importing we detected an older version of numpy
        
    Enter the below command.
    
        pip uninstall numpy (two times)
        pip install numpy
    
