#!/bin/sh
export PATH=/usr/lib/jvm/java-8-openjdk/bin/:"$PATH"
exec /usr/share/arduino/arduino "$@"
