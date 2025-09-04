import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration, PythonExpression
import time

from launch_xml.launch_description_sources import XMLLaunchDescriptionSource



def generate_launch_description():

    # simulation
    simulation = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory("rise_multirobot"), 'launch','include','simulation.launch.py')]),
    )

    wamv_sim_drivers = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory("wamv_rise_bringup"), 'launch','include','simulation_drivers.launch.py')]),
    )

    wamv_localization = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory("wamv_rise_bringup"), 'launch','bringup_pi_localization.launch.py')]),
    )

    wamv_mvp = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory("wamv_rise_bringup"), 'launch','bringup_pi_mvp.launch.py')]),
    )

    foxglove = IncludeLaunchDescription(
    XMLLaunchDescriptionSource(
        os.path.join(
            get_package_share_directory('foxglove_bridge'),
            'launch/foxglove_bridge_launch.xml')),
    )

    return LaunchDescription([
        foxglove,
        simulation,
        wamv_sim_drivers,
        wamv_localization,
        wamv_mvp
    ])
