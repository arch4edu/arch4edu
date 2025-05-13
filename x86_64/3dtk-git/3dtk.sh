#!/usr/bin/bash
## 
## 3DTK helper script for installations of binaries to /opt/3dtk
## 

usage() {
	echo "Usage: $0 TOOL [args...]"
        echo "Use '$0 tools' for a list of tools"
        exit 0
}

if (( $# < 1 ))
then
	usage
fi

case $1 in
	"tools")
		find /opt/3dtk -maxdepth 1 -type f -executable -exec basename {} \;
		exit 0
		;;
	"help" | "--help" | "-h" | "-?")
		usage
		;;
esac

eval /opt/3dtk/$@
