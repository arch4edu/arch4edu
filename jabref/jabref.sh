#!/bin/sh

/usr/bin/archlinux-java-run --min 8 --max 8 --feature javafx -- -jar /usr/share/java/jabref/JabRef-VERSION.jar "$@"
