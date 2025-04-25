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

### Running the demo scripts

The repository includes several demo scripts:

#### 1. Object manipulation in Rviz

```bash
rosrun moveit_robot_arm_sim node_add_attach_detach_objects_in_Rviz.py
```
This interactive script allows you to:
- Add cylinders of different sizes at various positions
- Attach objects to the robot's end effector
- Detach objects from the robot
- Remove objects from the scene

Follow the prompt instructions to perform different operations.

#### 2. Object manipulation in Gazebo

```bash
rosrun moveit_robot_arm_sim node_attach_detach_objects_in_Gazebo.py
```
This script enables physical object interaction in the Gazebo simulation:
- Attach objects to the robot's gripper
- Detach objects from the gripper

## Acknowledgments

This project builds on various ROS and MoveIt tutorials, with thanks to the ROS and MoveIt communities.