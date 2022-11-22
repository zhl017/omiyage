#!/usr/bin/env python3

import sys
import rospy
import moveit_commander

class manipulator():
    def __init__(self):

        moveit_commander.roscpp_initialize(sys.argv)
        
        self.group = moveit_commander.MoveGroupCommander("arm")
        self.group1 = moveit_commander.MoveGroupCommander("gripper")

        rate = rospy.Rate(10)

        while not rospy.is_shutdown():
            self.process()
            rate.sleep()

    def control_gripper(self, onoff):
        joint = self.group1.get_current_joint_values()
        # rospy.loginfo(joint)

        if onoff:
            joint[0] = 0.01 # open
        else:
            joint[0] = 0    # close

        self.group1.go(joint, wait=True)
        self.group1.stop()

    def control_arm(self, j1, j2, j3, j4):
        joint = self.group.get_current_joint_values()
        # rospy.loginfo(joint)

        # rad
        joint[0] = j1
        joint[1] = j2
        joint[2] = j3
        joint[3] = j4

        self.group.go(joint, wait=True)
        self.group.stop()

    def process(self):

        # pose 1
        self.control_arm(0.0, -1.0, 0.3, 0.7)

        # pose 2
        self.control_arm(0.0, 0.6, 0.1, -0.7)

        # tool close
        self.control_gripper(False)

        # pose 1
        self.control_arm(0.0, -1.0, 0.3, 0.7)

        # pose 2
        self.control_arm(0.7, 0.6, 0.1, -0.7)

        # tool close
        self.control_gripper(True)



if __name__ == '__main__':
    rospy.init_node('turtlebot3_manipulator_demo')
    node = manipulator()
    node.main()
