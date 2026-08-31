from setuptools import setup

package_name = 'example'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    entry_points={
        'console_scripts': [
            'talker = example.talker:main',
            'listener = example.listener:main',
        ],
    },
)
