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
    
    foxglove = IncludeLaunchDescription(
    XMLLaunchDescriptionSource(
        os.path.join(
            get_package_share_directory('foxglove_bridge'),
            'launch/foxglove_bridge_launch.xml')),
    )

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

    alpha_sim_drivers = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory("alpha_rise_bringup"), 'launch','include','simulation_drivers.launch.py')]),
    )

    alpha_localization_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory("alpha_rise_bringup"), 'launch','include', 'localization_sim.launch.py')]),
    )

    alpha_description = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory("alpha_rise_bringup"), 'launch','include', 'description.launch.py')]),
    )


    alpha_mvp_control_sim = IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('alpha_rise_bringup'), 'launch','include','mvp_control_sim.launch.py')]),
            launch_arguments = {'arg_robot_name': 'alpha_rise'}.items()  
    )

    #mvp_mission
    alpha_mvp_mission = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('alpha_rise_bringup'), 'launch','include','mvp_mission.launch.py')]),
        launch_arguments = {'arg_robot_name': 'alpha_rise'}.items()  
    )
    return LaunchDescription([
        foxglove,
        simulation,
        wamv_sim_drivers,
        wamv_localization,
        wamv_mvp,
        alpha_sim_drivers,
        alpha_localization_sim,
        alpha_description,
        alpha_mvp_control_sim,
        alpha_mvp_mission
    ])
