#!/usr/bin/env python3

import rospy
import math
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
from std_msgs.msg import String


def pub():
	rospy.init_node('pub', anonymous=True) 
	pub=rospy.Publisher('/mobile/cmd_vel', Twist, queue_size=100)
	rate = rospy.Rate(60)
	move=Twist()
	move1=Twist()
	move1.linear.x=1;
	#move2.linear.y;
	move.angular.z=5;
	
	while not rospy.is_shutdown():
		pub.publish(move)
		#pub.publish(move1)
		rate.sleep()
	
	
		
if __name__ == '__main__':
	try:
 	 pub()
	except rospy.ROSInterruptException:
	 pass
