# Author: Kevin DeMarco

from os import path
import yaml
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')

    rviz_config = path.join(get_package_share_directory('bamboomba_description'),
                              'rviz', 'bamboomba.rviz')

    robot_state_publisher = path.join(
        get_package_share_directory('bamboomba_description'),
        'launch',
        'robot_state_publisher.launch.py')

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='False',
            description='Use simulation (Gazebo) clock if true'),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(robot_state_publisher),
            launch_arguments={'use_sim_time': use_sim_time}.items()
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config],
            parameters=[{'use_sim_time': use_sim_time}],
            output='screen'),
    ])
