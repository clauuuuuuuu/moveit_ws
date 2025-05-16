# Robot Arm Simulation with MoveIt

This repository contains a robotic arm simulation that demonstrates pick and place operations with MoveIt in ROS. The robot can grip cylinders and boxes of different sizes in both Rviz and Gazebo environments.

## Features

- Robot arm control using MoveIt motion planning framework
- Pick and place operations with predefined poses
- Object manipulation (add, attach, detach, remove) in Rviz
- Gazebo physics simulation for realistic object interaction
- Support for different object sizes and shapes (cylinders, boxes)

## Prerequisites

- ROS (tested with ROS Noetic)
- Gazebo
- MoveIt
- Python 3
- gazebo_ros_link_attacher package

## Installation

1. Clone this repository into your ROS workspace:
   ```bash
   cd ~/moveit_ws/src
   git clone <repository-url>
   ```

2. Install dependencies:
   ```bash
   rosdep install --from-paths . --ignore-src -r -y
   ```

3. Build the workspace:
   ```bash
   cd ~/moveit_ws
   catkin_make
   ```

4. Source the setup file:
   ```bash
   source devel/setup.bash
   ```

## Usage

### Launch the simulation environment

```bash
roscore
roslaunch moveit_robot_arm_sim full_robot_arm_sim.launch
```

This will:
- Load the robot URDF model
- Start Gazebo with the robot model
- Launch MoveIt's move_group node
- Open Rviz with a preconfigured setup

## Acknowledgments

This project builds on various ROS and MoveIt tutorials, with thanks to the ROS and MoveIt communities.
