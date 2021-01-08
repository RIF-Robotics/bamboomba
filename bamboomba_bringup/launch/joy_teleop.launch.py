from os import path
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

def generate_launch_description():
    bamboomba_bringup_dir = get_package_share_directory('bamboomba_bringup')

    teleop_config = path.join(bamboomba_bringup_dir, 'config', 'thrustmaster.yaml')

    return LaunchDescription([
        Node(package='joy',
             name='joy_node',
             executable='joy_node',
             output='screen',
             parameters=['dev': '/dev/input/js0',
                         'deadzone': '0.2',
                         'autorepeat_rate': '20.0']
        ),
        Node(package='joy_telop',
             name='joy_telop',
             executable='joy_telop',
             output='screen',
             parameters=['teleop_config': teleop_config]
        ),
    ])
