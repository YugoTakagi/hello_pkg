# Hello pkg
ROSプログラムを詳解．

## セットアップ
ターミナルを立ち上げて，以下を実行．
``` bash
cd ~/catkin_ws/src # ROSワークスペースに移動
git clone https://github.com/YugoTakagi/hello_pkg.git
catkin build

cd hello_pkg/script
chmod +x making_cmd_vel.py # 実行プログラムに権限を付与
exit
```
ターミナルを立ち上げなおして，以下を実行．
``` bash
rosrun hello_pkg making_cmd_vel.py # cmd_vel: vx = 1.0を出力．
```

## How to use script/recode_camera_iamge.py
カメラを起動します．ここでは，以下のようにusb_camを利用します．
```bash
rosrun usb_cam usb_cam_node
```
次に，以下を実行します．
実行するとimgsディレクトリにカメラ画像を記録していきます．
```bash
roscd hello_pkg/script
mkdir imgs

chmod +x recode_camera_image.py

rosrun hello_pkg recode_camera_image.py
```

## 補足
### Rosパッケージの作り方！

``` bash
cd ~/catkin_ws/src
catkin_create_pkg hello_pkg std_msgs rospy roscpp
catkin build
```

*参考Web
1. https://raspimouse-sim-tutorial.gitbook.io/project/ros_tutorial/how_to_create_pkg 

### Rosプログラムの作り方！

``` bash
cd hello_pkg
mkdir script
cd script

touch making_cmd_vel.py #Pythonプログラムを編集して．

chmod +x making_cmd_vel.py
```



