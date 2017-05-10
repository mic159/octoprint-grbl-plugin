from setuptools import setup, find_packages

setup(
    name='octoprint-grbl-plugin',
    version='1.0.0',
    packages=find_packages(),
    license='MIT',
    author='mic159@gmail.com',
    description='Support GRBL type CNC machines',

    entry_points={
        'octoprint.plugin': [
            'octoprint-grbl-plugin = octoprint_grbl_plugin'
        ]
    }
)
