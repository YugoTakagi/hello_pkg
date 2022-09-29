#!/usr/bin/python3.6
##!/usr/bin/python3

''' This code is a tutolial for creating a simple ros node.
It was created by Takagi, who is a member of Ji Lab.
'''

from time import sleep
import rospy
from sensor_msgs.msg import Image

import cv2

import sys
sys.path.remove('/opt/ros/melodic/lib/python2.7/dist-packages')
from cv_bridge import CvBridge


def main():
    rospy.init_node('My_recode_camera_node_san', anonymous=True)

    rate = rospy.Rate(10) # 10 Hz

    my_recode_image_node = MyRecodesan()

    sleep(2)
    while not rospy.is_shutdown():
        my_recode_image_node.is_recoding_images()
        rate.sleep()

class MyRecodesan:
    def __init__(self):
        self.sukina_topic_name = '/usb_cam/image_raw'        
        self.image_subscriber_san = rospy.Subscriber(self.sukina_topic_name, Image, self.callbackFunctionForRecodingImages)
        self.cv_bridge = CvBridge()
        self.i = 0

    def callbackFunctionForRecodingImages(self, msg):
        try:
            self.image = self.cv_bridge.imgmsg_to_cv2(msg, "bgr8")
        except Exception as e:
            rospy.logerr(e)
            rospy.logerr('error!!!')
    
    def is_recoding_images(self):
        image = self.image

        cv2.imshow('rgb image', self.image)
        cv2.waitKey(3)
        
        cv2.imwrite('./imgs/{0}_image.png'.format(self.i), image)
        self.i += 1


''' Main関数の実行
'''
if __name__ == '__main__':
    main()