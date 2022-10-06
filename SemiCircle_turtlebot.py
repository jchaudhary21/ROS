#!/usr/bin/env python       

#            ^_^
# 
# Author - Jayesh Chaudhary 
# Github - https://github.com/jchaudhary21
#  
                                                  
import rospy                                                                               # importing important Libraries 
from geometry_msgs.msg import Twist                                               
from turtlesim.msg import Pose                                                    
     
class Turtle():                                                                            # Defining Class structure for better code flow 
    rospy.init_node('turtlebot',anonymous=True) 
      
    def __init__(self):                                                                    # initializing constructor 
                                                                                    
        self.pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size =100)               #  -- Publishing @ topic turtle1/cmd_vel  --
        										      # |                                         |
         										      # |     TO CHECK ACTIVE TOPICS RUN          |
											      # |         " rostopic list "               |
											      # |                                         |        
        self.subs = rospy.Subscriber('/turtle1/pose',Pose, self.callback)                  #  -- Subscribing @ topic turtle1/pose    --
        
        self.pose = Pose()                                                                 # Creating object    
        self.twist = Twist()                                                               # Creating object 
        
        
    def callback(self,data):                                                               # a callback function whenever new data arrives @ /turtle1/pose                              
      self.pose = data
      
      
    def position(self):                                                                    # through this we can get linear pose i.e x and y 
       linear_pose = [self.pose.x,self.pose.y]
       return (linear_pose)
       
    def orientation(self):                                                                 # through this we can get angular pose i.e θ 
       angular_pose = [self.pose.theta]
       return (angular_pose)
         
    
call_class = Turtle()                                                                     #  --
											     #    | -- creating object 
call_pose = call_class.twist								     #  --

r = rospy.Rate(1000)                        

call_pose.linear.x = 1                                                                   # Setting up linear velocity in x direction 
call_pose.angular.z = 0.5                                                                # Setting up angular velocity 

final_theta = -3.1 
initial_theta = -0.4                                                                     # initial theta of turtle 
v = 10.0 										    # assigning random number to v which shouldn't be equal to initial theta

print ("#########################")                                                         
print ("#    MOVING IN CIRCLE   #")
print ("#########################")
while (round(call_class.orientation()[0],1) != v):                                       # run this loop till v and inital theta become equal 

    call_class.pub.publish(call_class.twist)   
    print(" ")                 
    print ("Current Angular Position θ : {}".format(round(call_class.orientation()[0],1)))    # -- 
    print ("Current Linear Position x : {}".format(round(call_class.position()[0],1)))        #    | printing some important stuff 
    print ("Current Linear Position y : {}".format(round(call_class.position()[1],1)))        # -- 
    v = final_theta
    r.sleep()


call_pose.angular.z = 0.0 									# -----
call_pose.linear.x = 0										#      | - assigning new velocities 
call_pose.linear.y = 1										# -----

print ("#################################")                                                       
print ("#    MOVING IN STRAIGHT LINE    #")
print ("#################################")
while ( round(call_class.position()[1],1) != 6.3 ) :

	call_class.pub.publish(call_class.twist) 
	print(" ")
	print ("Current Linear Position y : {}".format(round(call_class.position()[1],1)))
	r.sleep()

	
 
    
print("")
print("Semi - Circle completed ")
    
