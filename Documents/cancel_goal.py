#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from actionlib_msgs.msg import GoalID

class cancel_goal():
    def __init__(self):

        self.is_cancel = False
        self.goal = GoalID()

        self.sub_yolo = rospy.Subscriber('/yolov5', String, self.cbyolo, queue_size = 1)

        self.pub_cancel_goal = rospy.Publisher('/move_base/cancel', GoalID, queue_size = 1)
        
        rospy.loginfo('Waiting for yolo data.....')

        loop_rate = rospy.Rate(15)

        while not rospy.is_shutdown():
            if self.is_cancel:
                self.cancel()
            
            loop_rate.sleep()

    def cbyolo(self, msg):
        # rospy.loginfo(rospy.get_caller_id() + ' %s', msg.data)
        self.is_cancel = True

    def cancel(self):
        rospy.loginfo("Cancel Goal.....")
        self.pub_cancel_goal.publish(GoalID())
        self.is_cancel = False

if __name__ == '__main__':
    rospy.init_node('cancel_goal')
    node = cancel_goal()
    node.main()