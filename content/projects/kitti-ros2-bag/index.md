---
title: KITTI to ROS2 Bag
description: Python package that converts the KITTI Synced Dataset into a ROS2 bag file for replay and development.
date: 2025-05-27
github: https://github.com/IndraReddy5/KITTI-ROS2-Bag
tags: [Python, ROS2, LiDAR, KITTI]
showDate: false
---

The KITTI dataset is one of the most widely used benchmarks in autonomous driving research, but working with it in a ROS2 development environment requires tedious manual conversion. This package automates the full conversion — reading synced camera images, LiDAR point clouds, IMU, and GPS data from the KITTI directory structure and writing them into a ROS2 bag file with correct timestamps and topic names.

**What it does**

- Reads the KITTI Synced & Rectified dataset (camera, Velodyne, oxts)
- Publishes `sensor_msgs/Image`, `sensor_msgs/PointCloud2`, `sensor_msgs/Imu`, and `sensor_msgs/NavSatFix` messages
- Preserves original KITTI timestamps across all topics
- Outputs a valid ROS2 bag playable with `ros2 bag play`

**Stack:** Python 3, rclpy, rosbag2_py, sensor_msgs
