from os import path
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import FrontendLaunchDescriptionSource, PythonLaunchDescriptionSource
from nav2_common.launch import RewrittenYaml

def generate_launch_description():
    bamboomba_bringup_dir = get_package_share_directory('bamboomba_bringup')

    base_launch_file = path.join(bamboomba_bringup_dir, 'launch', 'base.launch.py')
    rp_lidar_a2_launch_file = path.join(bamboomba_bringup_dir, 'launch', 'rplidar_a2.launch.py')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(base_launch_file)),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(rp_lidar_a2_launch_file))
    ])
