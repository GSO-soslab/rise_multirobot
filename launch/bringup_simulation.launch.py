import os
import yaml
import pathlib
from launch import LaunchDescription
import launch.actions
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch.substitutions import EnvironmentVariable
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument

def generate_launch_description():

    #ALPHA_RISE
    alpha_rise_bringup_launch_file = os.path.join(get_package_share_directory('alpha_rise_bringup'), 
                                                  'launch', 'bringup_simulation.launch.py')
    alpha_rise_bringup = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(alpha_rise_bringup_launch_file)
    )

    #MSIS_PCL
    msis_pcl_launch_file = os.path.join(get_package_share_directory('pcl_proc'), 
                                                  'launch', 'msis_pcl.launch.py')
    msis_pcl_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(msis_pcl_launch_file)
    )

    #PCL_FILTER 
    pcl_filter_launch_file = os.path.join(get_package_share_directory('pcl_proc'), 
                                                  'launch', 'filter.launch.py')
    pcl_filter_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(pcl_filter_launch_file)
    )

    #FLS_PCL
    fls_pcl_launch_file = os.path.join(get_package_share_directory('fls_pcl'), 
                                                  'launch', 'fls_pcl.launch.py')
    fls_pcl_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(fls_pcl_launch_file)
    )

    #Costmap
    costmap_launch_file = os.path.join(get_package_share_directory('pcl_proc'), 
                                                  'launch', 'costmap.launch.py')
    costmap_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(costmap_launch_file)
    )

    #Path Gen
    path_gen_launch_file = os.path.join(get_package_share_directory('pcl_proc'), 
                                                  'launch', 'path_gen.launch.py')
    path_gen_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(path_gen_launch_file)
    )

    return LaunchDescription([
        SetEnvironmentVariable('RCUTILS_COLORIZED_OUTPUT', '1'),
        alpha_rise_bringup,
        msis_pcl_launch,
        pcl_filter_launch,
        fls_pcl_launch,
        costmap_launch,
        path_gen_launch
    ])