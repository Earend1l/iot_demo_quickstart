#!/bin/bash

# Get current workspace
old_ws=`sed -n '2p' workspace.txt`
echo "Old workspace: $old_ws"

# The new workspace is given by the user
echo "New workspace: $1\n"

if [ $1 = $old_ws ]
then
        echo "The workspace is already set to: $old_ws\nExiting...\n"
	exit 1
else
	# Set new workspace
	sed -i "s,$old_ws,${1},g" workspace.txt
	sed -i "s,$old_ws,${1},g" terminator_config

	# Done
	echo "Replaced every occurrence of $old_ws with $1 in files workspace.txt and terminator_config.\n\nDon't forget to copy terminator_config into terminator config directory using the following command:\n\ncp terminator_config ~/.config/terminator/config\n"
fi


