from os import path
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    bamboomba_bringup_dir = get_package_share_directory('bamboomba_bringup')

    teleop_config = path.join(bamboomba_bringup_dir, 'config', 'thrustmaster.yaml')

    rviz_config = path.join(get_package_share_directory('bamboomba_bringup'),
                               'rviz', 'teleop.rviz')

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),

        Node(package='joy',
             name='joy_node',
             executable='joy_node',
             output='screen',
             parameters=[{'dev': '/dev/input/js0',
                          'deadzone': 0.2,
                          'autorepeat_rate': 20.0,
                          'use_sim_time': use_sim_time}]
        ),
        Node(package='joy_teleop',
             name='joy_teleop',
             executable='joy_teleop',
             output='screen',
             parameters=[teleop_config,
                         {'use_sim_time': use_sim_time}]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config],
            parameters=[{'use_sim_time': use_sim_time}],
            output='screen'),
    ])
