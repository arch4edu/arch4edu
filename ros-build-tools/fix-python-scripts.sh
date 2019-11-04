#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 [-v/--version PYTHON_VERSION] <directory>"
    echo ""
    echo "Makes sure that all Python scripts use the right python command."
    echo "PYTHON_VERSION: either 2 or 3 (default = 2)."
    echo "
Note that according to PEP 394, developers should use \"python\" in
the shebang line for code compatible with both Python 2 and 3, but
since this may not be the case, we always overwrite the shebang line.
For more information: http://legacy.python.org/dev/peps/pep-0394/"
    exit 1
fi

# Default Python version: 2
PYTHON_VERSION=2

while [[ $# > 1 ]]
do
  key="$1"
  shift

  case $key in
    -v|--version)
      PYTHON_VERSION="$1"
      shift
      ;;
    *)
      # unknown option
      ;;
  esac
done

# Check user input
if [[ "$PYTHON_VERSION" != "2" && "$PYTHON_VERSION" != "3" ]]; then
  echo "Error: invalid Python version given: $PYTHON_VERSION"
  exit 2
fi

for file in $(grep -rl -e 'env python *$' -e 'bin/python *$' $1); do
    if [ -z "$file" ]; then
        echo "Error finding files."
        exit 1
    fi
    sed -i "s,env python *$,env python${PYTHON_VERSION},g" $file
    sed -i "s,/usr/bin/python *$,/usr/bin/env python${PYTHON_VERSION},g" $file
done

