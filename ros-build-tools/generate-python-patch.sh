#!/bin/bash

set -e

if [ -z "$1" ]; then
    echo "Usage: $0 <stack-archive.tar.bz2>"
    exit 1
fi

SCRIPT_DIR=$(readlink -f `dirname $0`)
STACK_ARCHIVE_FILE_NAME=$(basename $1)
STACK_ARCHIVE_DIR_NAME=$(readlink -f `dirname $1`)

STACK_NAME=${1%.tar.bz2}
TMP_DIRECTORY_NAME=$(mktemp -d /tmp/${STACK_NAME}.XXXXXXXXXX)
cd $TMP_DIRECTORY_NAME
tar xjf ${STACK_ARCHIVE_DIR_NAME}/${STACK_ARCHIVE_FILE_NAME}
cp -r ${STACK_NAME} ${STACK_NAME}-orig
$SCRIPT_DIR/fix-python-scripts.sh ${TMP_DIRECTORY_NAME}/${STACK_NAME}
diff -Naur ${STACK_NAME}-orig ${STACK_NAME}
