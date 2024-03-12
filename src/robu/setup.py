from setuptools import find_packages, setup
import os
from glob import glob
package_name = 'robu'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robu',
    maintainer_email='robu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'wallfollower = robu.ex10_wallfollower:main',
            'mypublisher = robu.publisher_member_function:main',
            'mysubscriber = robu.subscriber_member_function:main',
            'myparameter = robu.ex11_parameter:main',
            'testparameter = robu.test_parameter:main',
            'testparameter_get = robu.test_parameter_get:main',
            'fibonacci_server = robu.ex12_fibonacci_server:main',
            'fibonacci_client = robu.ex12_fibonacci_client:main'
        ],
    },
)
