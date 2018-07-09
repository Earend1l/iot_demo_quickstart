# iot_demo_quickstart
GNOME Terminator configuration

## Getting Started

It is advised to clone this repository into your iot_demo catkin/src directory, since this module is only useful for this particular package. You can rename it 'quickstart':

```
roscd iot_demo
git clone [URL] quickstart
```

Replace [URL] by this repository's git URL.

### Prerequisites

This module should be used with the IoT demonstration 2018 version. It is not mandatory though it can help increase productivity. You will need to install GNOME Terminator to use this module. Terminator is a tool similar to tmux and screen with an easy-to-use user interface, and additional functionalities such as the possibility to create premade profiles and layouts, with the execution of custom commands when the different terminals are launched. Custom layouts have been created for the demo, to speed up the starting process. Here is a guide to install Terminator.

Version 0.97 is fine though 0.98 is better as it provides a GUI to choose between layouts:

```
sudo add-apt-repository ppa:gnome-terminator
sudo apt-get update
sudo apt-get install terminator
```

You can check the version of terminator:

```
terminator --version
```

Before deploying the module, you will also need to create SSH keys for your machine and the robot. Run these commands on your machine, so that the python script (instructions.py) launched by terminator can automatically connect to the robot:

```
ssh-keygen -t rsa
ssh-copy-id [user]@[robot]c1
```

Replace [user] with your username. Replace [robot] by max or bob. This command will ask for a password.

## Deployment

Move to your iot_demo/quickstart/ directory and set your workspace (which should be the directory that contains /catkin_ws, /openrobot_ws and setup-env.sh) using setworkspace.sh:

```
sh setworkspace.sh '~/example/path'
```
Please note that the path you provide must be absolute (using ~ to get your home directory for example).
Copy the premade terminator configuration file (if you have not already, please source setup-env.sh for the roscd command to work):

```
roscd iot_demo
cp quickstart/terminator_config ~/.config/terminator/config
```

Use terminator layout launcher to choose the appropriate layout (if you are using terminator version 0.98):

```
terminator -s
```

If you are using terminator version 0.97, then launch it with the layout name (for example iot_demo_max):

```
terminator -l iot_demo_max
```
