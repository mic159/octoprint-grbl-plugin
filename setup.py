from setuptools import setup, find_packages

setup(
    name='octoprint-grbl-plugin',
    version='1.0.1',
    packages=find_packages(),
    license='MIT',
    author='mic159',
    author_email='mic159@gmail.com',
    url='https://github.com/mic159/octoprint-grbl-plugin',
    description='Support GRBL type CNC & Laser machines',
    keywords=['octoprint', 'grbl', 'gcode', 'cnc', 'laser'],

    entry_points={
        'octoprint.plugin': [
            'octoprint-grbl-plugin = octoprint_grbl_plugin'
        ]
    }
)
