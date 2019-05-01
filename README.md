#Trash can can

#Concept 
Recycling and sorting waste is something that is widely talked about, yet still seems to be difficult for individuals in the sense that 100% of the people we interviewed want to do it more and better. Issues include unclear directions at recycling stations, lack of resources at home and just plain laziness. We can even see people treating trash in a completely ignorant way, when it’s all over streets, parks and festival areas. And when asked how people feel about this, the words hate, mad, littering fines, terrible, awful and uncivilized came up. So we built a product to make recycling more effortless, fun, and directly valuable for people.

TrashCanCan is a service to be combined with the increased use of city bikes. The city bikes are already attached to stops that serve as fixed locations the users are going to visit anyway.
The idea is that when a city bike stop is attached to a TrashCanCan, in order to lock the bike, a piece of trash has to be thrown in the can. The coolest part is that the trash can only has one input so the user doesn’t need to think about recycling, but the can will automatically sort the trash inside itself to different containers with the help of image recognition and robotics.
Here is a simple demo how it sorts pieces of trash into two categories:


#What this program do

The camera will scan for trash on the plateform, if detected it will rotate to put the trash in the appropriate compartment, cup will go to the right, orange, apple, spoon, bottle and other object will go left.
A led will lit up when an object is detected

#Installation of the dependencies

sudo aptitude install -y  python3-pip gfortran python3-dev python-setuptools    python3-pyqt5 libtbb2   libqt4-test  libv4l-dev libxvidcore-dev libx264-dev libgtk-3-dev  libatlas-base-dev   libilmbase-dev libopenexr-dev libgstreamer1.0-dev libqtgui4  libatlas3-base libopencv-dev libpng12-dev    libhdf5-dev libjpeg8-dev  libjpeg-dev libtiff5-dev liblcms2-dev libwebp-dev libharfbuzz-dev libfribidi-dev tcl8.6-dev tk8.6-dev python-tk libgtk2.0-dev libavcodec-dev libavformat-dev libswscale-dev    libtbb-dev ibtiff-dev libjasper-dev libdc1394-22-dev

#Installation of tensorflow
python3 -m pip install --user -Uv tensorflow

#Installation of the other dependencies for the image recognition
python3 -m pip install --user -Uv  pillow keras h5py matplotlib opencv-python  picamera scipy numpy RPi.GPIO

#Installation of the image recognition
python3 -m pip install -Uv --user https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.2/imageai-2.0.2-py3-none-any.whl

#Installation of wiringpi to control the motor  (/!\ don't forget the sudo)
sudo python3 -m pip install --user -Uv wiringpi


#Pinout (BCM numbering)

Control Pin of the motor : 18
Led positive pin : 14

#How to use it 

To start the program type python3 main.py