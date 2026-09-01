#!/bin/bash

XDG_CONFIG_HOME=${XDG_CONFIG_HOME:-~/.config}

# Allow users to override command-line options
if [[ -f $XDG_CONFIG_HOME/arduino-flags.conf ]]; then
   ARDUINO_USER_FLAGS="$(sed 's/#.*//' $XDG_CONFIG_HOME/arduino-flags.conf | tr '\n' ' ')"
fi

# Launch
exec /opt/arduino-ide/arduino-ide "$@" $ARDUINO_USER_FLAGS 