#!/usr/bin/sh

# Note: the '-Xmx2g' flag is used to set the maximum memory that the java
# program is allowed. When working with large data sets, this number may need
# to be increased based on how much memory you wish to allow weka to have.
# Specifying command line arguments will override the defaults shown here.
# Example: '-Xmx4g'

_runtime11=$(/usr/bin/archlinux-java status | grep -m1 11 | cut -d' ' -f3)

exec /usr/lib/jvm/$_runtime11/bin/java -Xms32m -Xmx2g "$@" -jar /usr/share/weka/weka.jar
