#! /usr/bin/python3
#Author https://www.youtube.com/@Age.of.Robotics

#This code is modified based on the spawn_models.py script from the below package:
#https://github.com/pal-robotics/gazebo_ros_link_attacher

import rospy
from gazebo_msgs.srv import SpawnModel, SpawnModelRequest, SpawnModelResponse
from copy import deepcopy
from tf.transformations import quaternion_from_euler

#https://classic.gazebosim.org/tutorials?tut=build_model

#sdf documentation
#http://sdformat.org/spec

cylinder_sdf_model = """<?xml version="1.0" ?>
<sdf version="1.4">
  <model name="MODELNAME">
    <static>0</static>
    <link name="link">
      <inertial>
        <mass>1.0</mass>
        <inertia>
          <ixx>0.01</ixx>
          <ixy>0.0</ixy>
          <ixz>0.0</ixz>
          <iyy>0.01</iyy>
          <iyz>0.0</iyz>
          <izz>0.01</izz>
        </inertia>
      </inertial>
      <collision name="cylinder_collision">
        <pose>0 0 0 0 0 0</pose>
        <geometry>
          <cylinder>
            <radius>RADIUS</radius>
            <length>LENGTH</length>
          </cylinder>
        </geometry>
        <surface>
          <bounce />
          <friction>
            <ode>
              <mu>1.0</mu>
              <mu2>1.0</mu2>
            </ode>
          </friction>
          <contact>
            <ode>
              <kp>10000000.0</kp>
              <kd>1.0</kd>
              <min_depth>0.0</min_depth>
              <max_vel>0.0</max_vel>
            </ode>
          </contact>
        </surface>
      </collision>
      <visual name="cylinder_visual">
        <pose>0 0 0 0 0 0</pose>
        <geometry>
          <cylinder>
            <radius>RADIUS</radius>
            <length>LENGTH</length>
          </cylinder>
        </geometry>
        <material>
          <script>
            <uri>file://media/materials/scripts/gazebo.material</uri>
            <name>Gazebo/Blue</name>
          </script>
        </material>
      </visual>
      <velocity_decay>
        <linear>0.000000</linear>
        <angular>0.000000</angular>
      </velocity_decay>
      <self_collide>0</self_collide>
      <kinematic>0</kinematic>
      <gravity>1</gravity>
    </link>
  </model>
</sdf>
"""

def create_cylinder_request(sdf_model, modelname, px, py, pz, rr, rp, ry, radius, length):
    """Create a SpawnModelRequest with the parameters of the cylinder given.
    modelname: name of the model for gazebo
    px py pz: position of the cylinder
    rr rp ry: rotation (roll, pitch, yaw) of the model
    radius: radius of the cylinder
    length: length of the cylinder"""
    cylinder = deepcopy(sdf_model)
    # Replace radius and length of model
    cylinder = cylinder.replace('RADIUS', str(round(radius, 3)))
    cylinder = cylinder.replace('LENGTH', str(round(length, 3)))
    # Replace modelname
    cylinder = cylinder.replace('MODELNAME', str(modelname))

    req = SpawnModelRequest()
    req.model_name = modelname
    req.model_xml = cylinder
    req.initial_pose.position.x = px
    req.initial_pose.position.y = py
    req.initial_pose.position.z = pz

    q = quaternion_from_euler(rr, rp, ry)
    req.initial_pose.orientation.x = q[0]
    req.initial_pose.orientation.y = q[1]
    req.initial_pose.orientation.z = q[2]
    req.initial_pose.orientation.w = q[3]

    return req


if __name__ == '__main__':
    #Initialize the spawn_box_models node
    rospy.init_node('spawn_cylinder_models')
    
    #https://wiki.ros.org/ROS/Tutorials/UnderstandingServicesParams
    
    #Create a coallable object or serivce client for the service /gazebo/spawn_sdf_model
    spawn_srv = rospy.ServiceProxy('/gazebo/spawn_sdf_model', SpawnModel)
    rospy.loginfo("Waiting for /gazebo/spawn_sdf_model service...")
    #Wait for the service to get available
    spawn_srv.wait_for_service()
    rospy.loginfo("Connected to service!")

    task = input("Enter add to add object (or add1 add2 add3): ")

    # Define cylinder dimensions
    radius = 0.01  # Radius in meters
    length = 0.08  # Length in meters
    
    if task == "add1":
      # Spawn Cylinder
      rospy.loginfo("Spawning package$1 with task add1")

      # By default cylinders are oriented along the z-axis
      # To make it stand upright, no rotation needed (0,0,0)
      request = create_cylinder_request(cylinder_sdf_model, "package$1",
                                    0.18, -0.25, 0.04,  # position (z adjusted for length)
                                    1.57, 0.0, 0.0,      # rotation
                                    radius, length)      # radius, length
    elif task == "add2":
      # Spawn Cylinder
      rospy.loginfo("Spawning package$1 with task add2")

      request = create_cylinder_request(cylinder_sdf_model, "package$1",
                                    0.35, -0.26, 0.04,  # position
                                    0.0, 0.0, 0.0,      # rotation
                                    radius, length)      # radius, length
    elif task == "add3":
      # Spawn Cylinder
      rospy.loginfo("Spawning package$1 with task add3")

      request = create_cylinder_request(cylinder_sdf_model, "package$1",
                                    -0.91, 0.36, 0.04,  # position
                                    0.0, 0.0, 0.0,      # rotation
                                    radius, length)      # radius, length
    else: 
      # Spawn Cylinder (default)
      rospy.loginfo("Spawning package$1 with task add")

      request = create_cylinder_request(cylinder_sdf_model, "package$1",
                                    0.00, 0.6318, 0.04,  # position
                                    0.0, 0.0, 0.0,       # rotation
                                    radius, length)       # radius, length

    #Call the service to spawn the cylinder
    spawn_srv.call(request)

    rospy.sleep(1.0)