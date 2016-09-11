import RPi.GPIO as GPIO
import picamera 
import time
import datetime as dt

GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)
#----------------------------------#
# motion function to capture video #
#----------------------------------#
def MOTION(PIR_PIN):
                print ('Motion Detected')
                global counter
                counter = counter +1
                # put video capture code here
                
                with picamera.PiCamera() as camera:
                    camera.resolution = (640, 480)                                                                   
                    camera.annotate_text = dt.datetime.now().strftime('%d-%m-%Y %H:%M:%S')                    
                    filename = 'my_video' + str(counter) + '.h264'
                    print (filename)
                    camera.start_recording(filename)
                    # camera.shutter_speed = 20
                    # camera.ISO = 3000
                    camera.exposure_mode = 'night'
                    camera.awb_mode = 'auto'     
                    camera.wait_recording(30)                   
                    camera.stop_recording()
                    
#------------------#                    
# prog starts here #
#------------------#
time.sleep(2)
print ('Ready')
counter = 0
#--------------------#
# exception handling #
#--------------------#
try:
        GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
        while 1:
                print ('Sleeping/Recording - CTRL+C to exit')
                time.sleep(20)
                
except KeyboardInterrupt:
        print ('Quit')
        GPIO.cleanup()
