#!/bin/sh

#+
#  Name:
#     topcat

#  Purpose:
#     Invokes the TOPCAT application on unix

#  Description:
#     This shell script invokes the TOPCAT application.
#     It's not very complicated, but performs some argument manipulation
#     prior to invoking java with the right classpath and classname.
#
#     1. if a class path is specified using either the CLASSPATH
#        environment variable or the -classpath flag to this script,
#        it will be added to the application classpath
#
#     2. any command-line arguments which look like they are destined
#        for java itself (starting with -D or -X, or prefixed with -J) will
#        be sent to java, and the others will be sent to the application

#  Requisites:
#     - java should be on the path.
#

#  Authors:
#     MBT: Mark Taylor (Starlink)
#-

#  Divide the arguments into two parts: those destined as flags for
#  the java binary, and the rest.
javaArgs=""
appArgs=""
while test "$1"
do
   if echo $1 | grep -- '^-[XD]' >/dev/null; then
      javaArgs="$javaArgs "\'$1\'
   elif echo $1 | grep -- '^-J' >/dev/null; then
      javaArgs="$javaArgs "\'`echo $1 | sed s/^-J//`\'
   elif [ "$1" = "-classpath" -a -n "$2" ]; then
      shift
      export CLASSPATH="$1"
   else
      appArgs="$appArgs "\'$1\'
   fi
   shift
done

appjar=/usr/share/java/topcat-full.jar
CLASSPATH="${appjar}:${CLASSPATH}"

#  Run topcat.
cmd="java \
        $javaArgs0 \
        $javaArgs \
        -Duk.ac.starlink.topcat.cmdname=topcat \
        -classpath \${CLASSPATH} uk.ac.starlink.topcat.Driver \
        $appArgs"
eval "$cmd"
