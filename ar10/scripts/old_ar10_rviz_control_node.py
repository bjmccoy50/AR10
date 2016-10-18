#!/usr/bin/env python
#Active8 Robots, AR10 Rviz control node
#Beta release 1.1
#Written by Nick Hornsey
#Last edited on 6/10/16

#The following program subscribes to the rostopic "joint_states" and then sends equivalent commands to the AR10 hand.
#The program can be run in the ros workspace using the following command:
#rosrun ar10 ar10_rviz_control_node.py

#"joint_states" are published by joint_state_publisher in Rviz.
#A URDF representation of the hand can be published using the following command from the ros workspace:
#roslaunch src/ar10_description/launch/xacrodisplay.launch model:=src/ar10_description/urdf/ar10.urdf.xacro

 
from ros_ar10_class import ar10
import time
import sys
import os
import random
import serial
import subprocess

import rospy
from sensor_msgs.msg import JointState

def main():

	def listener():


	    rospy.init_node('listener', anonymous=True) # defines anonymous listener node
	    rospy.Subscriber('joint_states',JointState,callback)
	    rospy.spin()  # spin() simply keeps python from exiting until this node is stopped

	def callback(msg): # callback is executed when a message is published to 'joint_states'
	    pos = [1,1,1,1,1,1,1,1,1,1] # creates an array of 10 to store joint_states
	    for i in range (0,10):      # for all servos ...
	      pos[i]=msg.position[i+14]  #stores joint states to pos[] while bypassing the initial 14 passive revolute joints
	      pos[i]=converter(pos[i])   #converts servo posisitons into commands for the AR10 hand
	      print int(pos[i])
	    hand.move(0,int(pos[0]))     #sends commands to the AR10
  	    hand.move(1,int(pos[1]))
	    hand.move(2,int(pos[2]))
  	    hand.move(3,int(pos[3]))
	    hand.move(4,int(pos[4]))
            hand.move(5,int(pos[5]))
      	    hand.move(6,int(pos[6]))
      	    hand.move(7,int(pos[7]))
     	    hand.move(8,int(pos[8]))
     	    hand.move(9,int(pos[9]))
	    return pos


	def converter(pos):              #Converter that is executed when called in callback
	    command_value = (((pos*-3500)/0.02)+8000)
	    return command_value

	
	hand = ar10() # create hand object
	listener() # start subscriber

if __name__ == "__main__":
        main()


