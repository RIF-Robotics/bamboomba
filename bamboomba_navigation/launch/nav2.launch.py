import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription, LaunchContext
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')
    build_map = LaunchConfiguration('build_map')

    map_yaml_file = LaunchConfiguration(
        'map',
        default=os.path.join(
            get_package_share_directory('rif_maps'),
            'maps',
            'sim_cafe.yaml'))

    param_yaml_file = LaunchConfiguration(
        'params',
        default=os.path.join(
            get_package_share_directory('bamboomba_navigation'),
            'params',
            'nav2_params.yaml'))

    nav2_bringup_launch = os.path.join(
        get_package_share_directory('nav2_bringup'), 'launch',
        'bringup_launch.py')

    return LaunchDescription([
        DeclareLaunchArgument(
            'map',
            default_value=map_yaml_file,
            description='Full path to map file to load'),

        DeclareLaunchArgument(
            'params',
            default_value=param_yaml_file,
            description='Full path to param file to load'),

        DeclareLaunchArgument(
            'use_sim_time',
            default_value='True',
            description='Use simulation (Gazebo) clock if true'),

        DeclareLaunchArgument(
            'build_map',
            default_value='False',
            description='Run slam toolbox to build a map'),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(nav2_bringup_launch),
            launch_arguments={
                'map': map_yaml_file,
                'use_sim_time': use_sim_time,
                'slam': build_map,
                'params_file': param_yaml_file}.items(),
        ),
    ])
