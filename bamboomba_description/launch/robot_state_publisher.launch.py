from os import path
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')

    xacro_path = path.join(get_package_share_directory('bamboomba_description'),
                           'urdf', 'bamboomba.urdf.xacro')

    robot_description = {'robot_description' : Command(['xacro', ' ', xacro_path])}

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='False',
            description='Use simulation clock if true'),

        Node(package='robot_state_publisher',
             name='robot_state_publisher',
             executable='robot_state_publisher',
             output='screen',
             parameters=[{'use_sim_time': use_sim_time},
                          robot_description]
             ),
    ])
