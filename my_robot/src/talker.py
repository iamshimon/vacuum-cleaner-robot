#!/usr/bin/env python


# Simple python script which up a node to send forward Twist message
import rospy
from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('/mobile_base_controller/cmd_vel',Twist, queue_size=10)
    rospy.init_node('teleop_node', anonymous=True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        message = Twist()
        message.linear.x =0.9
        rospy.loginfo(message)
        pub.publish(message)
        rate.sleep()

if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass