from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kimi',
    maintainer_email='kimimi.nyan@gmail.com',
    description='a package for practice',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = mypkg.talker:main',
            'listener = mypkg.listener:main',

            'talker_rand = mypkg.talker_rand:main',
            'talker_data = mypkg.talker_data:talker_data',
            'listener_log = mypkg.listener_log:main',
            'converter_tobinary = mypkg.converter_tobinary:main',
            'converter_tohex = mypkg.converter_tohex:main',
        ],
    },
)
