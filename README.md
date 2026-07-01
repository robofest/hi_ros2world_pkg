#Hello World Package in ROS2

First, clone the package under your ros2_ws/src

```bash
$ cd ~/ros2_ws
$ colcon build --packages-select hi_ros2world_pkg
$ source install/setup.bash
$ ros2 run hi_ros2world_pkg hi_ros2world_node_exe
``` 