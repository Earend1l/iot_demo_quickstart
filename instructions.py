# This script will display launch instructions for each specific package that needs to be started for the demonstration.
# The name of the set of instructions should be passed as an argument for this script as well as the name of the robot (bob or max) using this syntax:
#
# python path/to/script/instructions.py 'set of instructions name' 'robot name'
#
# This script will also try to establish a secure shell connexion to the robot. For this functionnality to work, you need to have set up SSH Keys properly before hand.


import sys
import os


class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if len(sys.argv) != 3:
    print colors.FAIL + "Package name required, please use 'python instructions.py 'set of instructions name' 'robot name'\n Exiting..." + colors.ENDC
    sys.exit()

# BOB / MAX
robot_name = sys.argv[2]

# LAUNCH STEPS
def launch_steps():
    print colors.BOLD + colors.GREEN + ' - LAUNCH STEPS -\n' + colors.ENDC
    print 'Link to redmine (copy paste it):\n' + colors.UNDERLINE + 'https://redmine.laas.fr/projects/demo2018/wiki/DEMO2017_How_to_launch_the_demo' + colors.ENDC
    print '''
 01* robot
 02* map_server
 03* navigation
 04* iot_bridge
 05* toaster
 06* rviz
 07* acapela
 08* optitrack
 09* furniture
 10* iot_demo

Inside each terminal you will find the different commands that you can copy paste to easily launch the packages that you need. Before you start, it is advised to have your shell initialize your working directory, and source the setup for you, using the following commands on the robot (replace 'your-directory' accordingly, you might also want to change the name of the setup file, depending on how you named it):
'''
    print colors.BOLD + colors.BLUE + 'ssh -A -X ' + robot_name + 'c1\necho -e "cd your-directory\\nsource setup-env.sh" >> ~/.bashrc\n' + colors.ENDC

# ROBOT launch instructions
def robot():
    print colors.BOLD + colors.GREEN + ' - ROBOT -\n' + colors.ENDC
    print colors.BOLD + colors.BLUE + 'roslaunch /etc/ros/robot.launch\n' + colors.ENDC
    os.system('ssh -A -X ' + robot_name + 'c1')

# MAP_SERVER launch instructions
def map_server():
    print colors.BOLD + colors.GREEN + ' - MAP_SERVER -\n' + colors.ENDC
    print 'If the adream_apartment.yaml file is not located directly inside the openrobot_ws/data directory, please provide the complete path to it when executing this command.\n'
    print colors.BOLD + colors.BLUE + 'rosrun map_server map_server $ROBOTPKG_BASE/data/adream_apartment.yaml\n' + colors.ENDC
    os.system('ssh -A -X ' + robot_name + 'c1')

# NAVIGATION launch instructions
def navigation():
    print colors.BOLD + colors.GREEN + ' - NAVIGATION -\n' + colors.ENDC
    print colors.BOLD + colors.BLUE + 'roslaunch pr2_2dnav pr2_2dnav.launch\n' + colors.ENDC
    os.system('ssh -A -X ' + robot_name + 'c2')

# IOT_BRIDGE launch instructions
def iot_bridge():
    print colors.BOLD  + colors.GREEN + ' - IOT_BRIDGE -\n' + colors.ENDC
    print '(Don\'t forget to modifiy the config/conf.yaml file with the name of your machine or the robot.)\n'
    print colors.BOLD + colors.BLUE + 'roslaunch iot_bridge bridge.launch\n' + colors.ENDC

# TOASTER launch instructions
def toaster():
    print colors.BOLD + colors.GREEN + ' - TOASTER -\n' + colors.ENDC
    print colors.BOLD + colors.BLUE + 'cd catkin_ws/src/toaster/tools/toaster_scripts/roslaunch\nroslaunch toaster_real.launch\n' + colors.ENDC

# RVIZ launch instructions
def rviz():
    print colors.BOLD + colors.GREEN + ' - RVIZ -\n' + colors.ENDC
    print colors.BOLD + colors.BLUE + 'rosrun rviz rviz' + colors.ENDC
    print '''
This command should launch RViz. If you have no RViz configuration file saved, you can simply enable the following topics for vizualisation:

- Robotmodel
- MarkerObjects (/marker_objects topic)
- MarkerArea shows the areas
- MarkerHuman shows the position of the mocap helmet (/marker_human topic)
- Laserscan
- Map (/map topic)

You will then need to place the robot in its environment using 2D pose estimate.
'''

# ACAPELA launch instructions
def acapela():
    print colors.BOLD + colors.GREEN + ' - ACAPELA -\n' + colors.ENDC
    print colors.BOLD + colors.BLUE + 'unset DISPLAY; acapela-ros -b\n' + colors.ENDC
    os.system('ssh -A -X ' + robot_name + 'c1')

# OPTITRACK launch instructions
def optitrack():
    print colors.BOLD + colors.GREEN + ' - OPTITRACK -\n' + colors.ENDC
    print 'First check that optitrack-ros is not already running:\n'
    print colors.BOLD + colors.BLUE + 'ps -aef | grep optitrack\n' + colors.ENDC
    print 'If there is an optitrack-ros node running, kill it:\n'
    print colors.BOLD + colors.BLUE + 'kill -9 [process ID]\n' + colors.ENDC
    print 'Then execute these commands to launch your own node:\n'
    print colors.BOLD + colors.BLUE + 'optitrack-ros -b\nrosaction call /optitrack/connect \'{host: "marey", host_port: "1510", mcast: "239.192.168.30", mcast_port: "1511"}\'\n' + colors.ENDC

# FURNITURE launch instructions
def furniture():
    print colors.BOLD + colors.GREEN + ' - FURNITURE -\n' + colors.ENDC
    print colors.BOLD + colors.BLUE + 'cd catkin_ws/src/toaster/tools/toaster_scripts/shell/iot_demo\n./area_init_demo_real.sh\n' + colors.ENDC

# IOT_DEMO launch instructions
def iot_demo():
    print colors.BOLD + colors.GREEN + ' - IOT_DEMO -\n' + colors.ENDC
    print colors.BOLD + colors.BLUE + 'roslaunch pr2_teleop teleop_joystick.launch\nroslaunch iot_demo demo.launch\n' + colors.ENDC
    os.system('ssh -A -X ' + robot_name + 'c1')

if sys.argv[1] == 'launch_steps':
    launch_steps()

if sys.argv[1] == 'robot':
    robot()

if sys.argv[1] == 'map_server':
    map_server()

if sys.argv[1] == 'navigation':
    navigation()

if sys.argv[1] == 'iot_bridge':
    iot_bridge()

if sys.argv[1] == 'toaster':
    toaster()

if sys.argv[1] == 'rviz':
    rviz()

if sys.argv[1] == 'acapela':
    acapela()

if sys.argv[1] == 'optitrack':
    optitrack()

if sys.argv[1] == 'furniture':
    furniture()

if sys.argv[1] == 'iot_demo':
    iot_demo()

