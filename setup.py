from setuptools import find_packages, setup

package_name = 'hi_ros2world_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cchung',
    maintainer_email='cchung@ltu.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [ # node name does not need .py extension
	        'hi_ros2world_node_exe = hi_ros2world_pkg.hi_ros2world_node:main',
        ],
    },
)
