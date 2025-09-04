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



    return LaunchDescription([
        simulation,
 
    ])
