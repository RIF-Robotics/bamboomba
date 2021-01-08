from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import FrontendLaunchDescriptionSource, PythonLaunchDescriptionSource,
from nav2_common.launch import RewrittenYaml

def generate_launch_description():
    create_bringup_dir = get_package_share_directory('create_bringup_dir')

    original_params_file = path.join(
        create_bringup_dir, 'config', 'default.yaml')

    param_substitutions = {'dev': '/dev/create_serial'}

    configured_params = RewrittenYaml(
        source_file=original_params_file,
        param_rewrites=param_substitutions,
        convert_types=True)

    return LaunchDescription([
        IncludeLaunchDescription(
            FrontendLaunchDescriptionSource(ros2_cpp_params_example_launch_file),
            launch_arguments={'config': configured_params}.items())
    ])
