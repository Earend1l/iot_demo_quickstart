# iot_demo_quickstart
GNOME Terminator configuration

## Getting Started

First you need to clone this repository inside your workspace on your computer (the folder that contains both the catkin_ws and the openrobots_ws directories):

```
roscd
cd ../..
git clone [URL]
```

Replace [URL] by this repository's git URL and do not rename the created folder.

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
```

This will generate a public key, and a private key. You can specify a name for the files in which these keys will be saved. By default, the private key will be saved as /home/[user]/.ssh/id_rsa and the public key will be saved as /home/[user]/.ssh/id_rsa.pub. Leave blank the passphrase, otherwise instead of a login and password, you will have to enter your passphrase at each SSH connexion. The next step is to copy your public key inside the /home/[user]/.ssh/authorized_keys file on the distant machine to which you wish to connect:

```
ssh-copy-id [user]@[robot]c1
```

Replace [user] with your username. Replace [robot] by max or bob. This command will ask for a password.

## Deployment

Move to your iot_demo/quickstart/ directory and set your workspace (which should be the directory that contains /catkin_ws, /openrobot_ws and setup-env.sh) using setworkspace.sh:

```
sh setworkspace.sh '~/example/path'
```
Please note that the path you provide must be absolute (using ~ to get your home directory for example) and must not end with the character '/' (for example ~/manip_iot_2018 is correct, whereas ~/manip_iot_2018/ will not work). Then copy the premade terminator configuration file (if you have not already, please source setup-env.sh for the roscd command to work): 

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
