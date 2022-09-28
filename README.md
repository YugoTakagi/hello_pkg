# Read Me
--- hello pkg ---

## Rosパッケージの作り方！

cd ~/catkin_ws/src
catkin_create_pkg hello_pkg std_msgs rospy roscpp
catkin build

*参考Web
1. https://raspimouse-sim-tutorial.gitbook.io/project/ros_tutorial/how_to_create_pkg 

## Rosプログラムの作り方！

cd hello_pkg
mkdir script
cd script

touch making_cmd_vel.py #Pythonプログラムを編集して．

chmod +x making_cmd_vel.py



