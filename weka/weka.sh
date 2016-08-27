#! /bin/sh

# Note: the '-Xmx1g' flag is used to set the maximum memory that the java
# program is allowed. When working with large data sets, this number may need
# to be increased based on how much memory you wish to allow weka to have.
# Specifying command line arguments will override the defaults shown here.
# Example: '-Xmx2g'
DEFAULT_ARGS='-Xms32m -Xmx1g'

if [ $# -gt 0 ]; then
	ARGS="$@"
else
	ARGS="$DEFAULT_ARGS"
fi

java $ARGS -jar /usr/share/java/weka/weka.jar
