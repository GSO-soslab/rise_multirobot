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
    msis_pcl_launch_file = os.path.join(get_package_share_directory('iceberg_nav'), 
                                                  'launch', 'msis_pcl.launch.py')
    msis_pcl_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(msis_pcl_launch_file)
    )

    msis_prob_launch_file = os.path.join(get_package_share_directory('iceberg_nav'), 
                                                  'launch', 'msis_voxels.launch.py')
    msis_prob_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(msis_prob_launch_file)
    )

    #PCL_FILTER 
    pcl_filter_launch_file = os.path.join(get_package_share_directory('iceberg_nav'), 
                                                  'launch', 'filter.launch.py')
    pcl_filter_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(pcl_filter_launch_file)
    )

    #FLS_PCL
    fls_voxel_prob = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('fls_ism'),
                'launch',
                'fls_ism.launch.py'
            )
        ),
        launch_arguments={
            'use_sim_time': 'true'
        }.items()
    )

    mbes_inv = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('mbes_ism'),
                'launch',
                'mbes_ism.launch.py'
            )
        ),
        launch_arguments={'use_sim_time': 'true'}.items()
    )

    #Voxels
    voxel_log_odds = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory('iceberg_nav'),
                'launch',
                'voxel_log_odds.launch.py'
            )
        ),
        launch_arguments={
            'use_sim_time': 'true'
        }.items()
    )
    #Costmap
    costmap_launch_file = os.path.join(get_package_share_directory('iceberg_nav'), 
                                                  'launch', 'costmap.launch.py')
    costmap_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(costmap_launch_file)
    )

    #Path Gen
    path_gen_launch_file = os.path.join(get_package_share_directory('iceberg_nav'), 
                                                  'launch', 'path_gen.launch.py')
    path_gen_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(path_gen_launch_file)
    )
    
    #Waypoint Administrator
    wp_admin_launch_file = os.path.join(get_package_share_directory('iceberg_nav'),
                                        'launch', 'wp_admin.launch.py')
    
    wp_admin_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(wp_admin_launch_file)
    )

    return LaunchDescription([
        SetEnvironmentVariable('RCUTILS_COLORIZED_OUTPUT', '1'),
        alpha_rise_bringup,
        msis_pcl_launch,
        # pcl_filter_launch,
        msis_prob_launch,
        fls_voxel_prob,
        mbes_inv,
        voxel_log_odds,
        # costmap_launch,
        path_gen_launch,
        wp_admin_launch
    ])