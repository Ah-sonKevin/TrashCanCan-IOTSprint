from imageai.Detection import VideoObjectDetection
import os
import cv2
import ledControl
import time

execution_path = os.getcwd()                                                                                                         
detector = VideoObjectDetection()                                                     
ledController = ledControl.LedController()
#Time since the last time an boject was recognised
lastReco=0
print('sudo python3 '+os.getcwd()+'/motorManager.py --right') 

detector.setModelTypeAsTinyYOLOv3()                                                   
detector.setModelPath(os.path.join(execution_path , "yolo-tiny.h5"))                  
detector.loadModel(detection_speed="fast")  

camera = cv2.VideoCapture(0)

def forFrame(frame_number, output_array, output_count):
    global lastReco
    #Wait 5sec between recognition, to avoid recognizing many time the same object
    if(time.time() - lastReco > 5):
        print("FOR FRAME " , frame_number)
        print("Output for each object : ", output_array)
        for el in output_array:
            if(el['name'] == 'orange'  or  el['name'] == 'apple'):
                print('fruit  detected')
                time.sleep(1)
                ledController.endLed()
                #To control the motor we use the PWM mode of the pin, to do that we use the wiringpi library, to work it have to ba call using sudo, or due to some issue with numpy
                #the ImagaAI library can't be call using sudo, so we call the ImageAI library as an user and when we need the motor we use the os.system method to call the
                #motorManager script with sudo via the shell
                os.system('sudo python3 '+os.getcwd()+'/motorManager.py --left')
                lastReco = time.time()
            elif(el['name']== 'cup'):
                print('cup detected')
                time.sleep(1)
                ledController.endLed()
                os.system('sudo python3 '+os.getcwd()+'/motorManager.py --right')
                lastReco = time.time()
            elif(el['name'] == 'spoon'):
                print('spoon detected')
                time.sleep(1)
                ledController.endLed()                                                       
                os.system('sudo python3 '+os.getcwd()+'/motorManager.py --left')
                lastReco = time.time()
            elif(el['name'] == 'bottle'):
                print('bottle detected')
                ledController.endLed()
                os.system('sudo python3 '+os.getcwd()+'/motorManager.py --left')
                lastReco = time.time()
            else:
                print('Other object')
                time.sleep(1)
                ledController.endLed()
                os.system('sudo python3 '+os.getcwd()+'/motorManager.py --left')
                lastReco = time.time()
                print(el)

    
                             
       
detector.detectObjectsFromVideo(save_detected_video=False, camera_input=camera, frames_per_second=1,frame_detection_interval=5, log_progress=True, minimum_percentage_probability=30, per_frame_function= forFrame)
            
