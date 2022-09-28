#!/bin/bash

function usage() {
	echo 'usage:'
	echo '    ./run-docker image [asciiArt parameters]'
	echo ''
	echo 'Program help:'
	echo ''
	docker run --rm ascii-art:1.0 --help
	exit 1
}

[[ -z "$1" ]] && usage # If has a Image
[[ $(ls $1) ]] || usage # If the Image exists

IMAGE_NAME="$(echo $1 | awk -F '/' '{print $(NF)}')" # Get image name
ARGUMENTS="${@:2}" # Program arguments

docker run --rm -it -v "$(ls $1)":/asciiArt/$IMAGE_NAME ascii-art:1.0 $IMAGE_NAME $ARGUMENTS && exit 0
