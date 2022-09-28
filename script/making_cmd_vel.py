#!/usr/bin/python3.6

''' This code is a tutolial for creating a simple ros node.
It was created by Takagi, who is a member of Ji Lab.
'''

import rospy
from geometry_msgs.msg import Twist

def main():
    ''' main関数
    '''
    rospy.init_node('My_hello_node_san', anonymous=True)

    rate = rospy.Rate(10) # 10 Hz

    my_hello_node = MyHelloNode()

    while not rospy.is_shutdown():
        my_hello_node.is_publishing_a_ros_message_of_geoTwi_here()

        rate.sleep()


class MyHelloNode:
    ''' Classでノードを作成しました．
        （プログラムの可読性を高めるために）
    '''
    
    def __init__(self):
        rospy.loginfo('hello! I\'m \"Hello Node\".')

        sukina_topic_name = '/jackal_velocity_controller/cmd_vel' # /cmd_velなど．
        self.as_rospub_instance = rospy.Publisher(sukina_topic_name, Twist, queue_size=1)

    def is_publishing_a_ros_message_of_geoTwi_here(self):
        ''' トピックをパブリッシュするための関数．
        '''
        __twist = Twist()

        __twist.linear.x = 1.0
        __twist.linear.y = 1.0
        __twist.linear.z = 1.0

        __twist.angular.x = 0.0
        __twist.angular.y = 0.0
        __twist.angular.z = 0.0

        self.as_rospub_instance.publish(__twist)

        rospy.loginfo('I\'m publishing a message naw.')
        print('*** demo message dasuno tukaremasita.\n***')



''' Main関数の実行
'''
if __name__ == '__main__':
    main()