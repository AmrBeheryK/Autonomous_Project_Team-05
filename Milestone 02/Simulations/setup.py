import os
from glob import glob

from setuptools import find_packages, setup

package_name = 'autonomous_systems_project_team_5'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # This line is mandatory for ROS 2 to see your launch files
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dynames',
    maintainer_email='dynames@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            # Your Milestone 1 validation node
            'Validation_Printing_Node_Team_5 = autonomous_systems_project_team_5.validation_printing_node_team_5:main',
            # Your new Milestone 2 nodes
            'Autonomous_Systems_MS_2_OLR_Team_5 = autonomous_systems_project_team_5.Autonomous_Systems_MS_2_OLR_Team_5:main',
            'Autonomous_Systems_MS_2_Teleop_Team_5 = autonomous_systems_project_team_5.Autonomous_Systems_MS_2_Teleop_Team_5:main',
        ],
    },
)
