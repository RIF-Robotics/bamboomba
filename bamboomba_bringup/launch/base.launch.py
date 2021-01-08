from os import path
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from launch.launch_description_sources import FrontendLaunchDescriptionSource, PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, Command
from nav2_common.launch import RewrittenYaml

def generate_launch_description():
    create_bringup_dir = get_package_share_directory('create_bringup')

    original_params_file = path.join(
        create_bringup_dir, 'config', 'default.yaml')

    create_1_launch_file = path.join(
        create_bringup_dir, 'launch', 'create_1.launch')

    param_substitutions = {'dev': '/dev/create_serial',}

    configured_params = RewrittenYaml(
        source_file=original_params_file,
        param_rewrites=param_substitutions,
        convert_types=True)

    xacro_path = path.join(get_package_share_directory('bamboomba_description'),
                              'urdf', 'bamboomba.urdf.xacro')
    robot_description = {'robot_description' : Command(['xacro', ' ', xacro_path])}

    return LaunchDescription([
        IncludeLaunchDescription(
            FrontendLaunchDescriptionSource(create_1_launch_file),
            launch_arguments={'config': configured_params,
                              'desc': 'false'}.items()),
        Node(package='robot_state_publisher',
             name='robot_state_publisher',
             executable='robot_state_publisher',
             output='screen',
             parameters=[robot_description]
        ),
    ])
