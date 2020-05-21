# mobile
##camera view
	rosrun image_view image_view image:=/lle/camera1/image_raw


	rosrun turtlesim turtle_teleop_key /turtle1/cmd_vel:=/cmd_vel
	rosrun turtlebot_teleop turtlebot_teleop_key /turtlebot_teleop/cmd_vel:=/lle/cmd_vel


## covert Xcro to urdf:
	rosrun xacro xacro.py lle.xacro > lle.urdf

##rviz
	 roslaunch ros_robotics rrbot_rviz.launch model:=lle.xacro

rostopic echo -b file.bag -p /topic > data.txt
rostopic echo -b file.bag -p /topic


#ARDUINO
ls -l /dev/ttyACM0
sudo usermod -a -G dialout mohammad
sudo chmod a+rw /dev/ttyACM0

sudo chmod 666 /dev/ttyACM0
rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0
source /opt/ros/indigo/setup.bash

rostopic pub servo std_msgs/Float64 50 --once
rostopic pub servo std_msgs/UInt16 0

remove a lock file 
sudo rm -rf <path_to_file_folder>

excel output of ROS
rosbag record -O subset  /lle/j_hip_r_position_controller/command
rostopic echo /lle/j_hip_r_position_controller/command -b subset.bag -p> r_hip.csv

rosrun teleop_twist_keyboard teleop_twist_keyboard.py


# added by Anaconda2 installer
export PATH="/home/mohammad/anaconda2/bin:$PATH"

export PATH=~/anaconda2/bin:$PATH
export PYTHONPATH=$PYTHONPATH:/usr/lib/python2.7/dist-packages

rostopic echo -n 1 /gazebo/model_states

echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
