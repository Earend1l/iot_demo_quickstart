#!/bin/bash

# Get current workspace
old_ws=`sed -n '2p' workspace.txt`
echo "Old workspace - quickstart/workspace.txt:2: $old_ws\n"

# Set new workspace
sed -i "s,$old_ws,${1},g" workspace.txt
sed -i "s,$old_ws,${1},g" terminator_config
echo "New workspace: $1\n"

# Done
echo "Replaced every occurrence of $old_ws with $1 in files workspace.txt and terminator_config.\n\nDon't forget to copy terminator_config into terminator config directory using the following commands:\n\nroscd iot_demo\ncp quickstart/terminator_config ~/.config/terminator/config\n"
