#!/bin/bash

set -e

if [ -z "$3" ]; then
    echo "Usage: $0 <distro> <stack> <version>"
    exit 1
fi

DISTRO=$1
STACK=$2
PACKAGE=$(echo $STACK | sed 's/_/-/g')
VERSION=$3
URL=https://code.ros.org/svn/release/download/stacks/$STACK/$STACK-$VERSION/$STACK-$VERSION.tar.bz2

PACKAGE_DIRECTORY=$(pwd)/$STACK

if [ -d $PACKAGE_DIRECTORY ]; then
    read -p "Directory $STACK already exists. Overwrite? (y/n) "
    if ! [ "$REPLY" == "y" ]; then
        exit 0
    fi
fi

mkdir -p $PACKAGE_DIRECTORY
cd $PACKAGE_DIRECTORY

[ -f ${STACK}-${VERSION}.tar.bz2 ] || wget "$URL"
if ! [ -f "${STACK}-${VERSION}.tar.bz2" ]; then
    echo "Invalid stack name or version. Downloaded file does not match ${STACK}-${VERSION}.tar.bz2"
    exit 1
fi
MD5=$(md5sum ${STACK}-${VERSION}.tar.bz2 | awk '{print $1}')

cp /usr/share/ros-build-tools/PKGBUILD.rostemplate $PACKAGE_DIRECTORY/PKGBUILD

mkdir $PACKAGE_DIRECTORY/tmp
cd $PACKAGE_DIRECTORY/tmp
tar xvjf $PACKAGE_DIRECTORY/${STACK}-${VERSION}.tar.bz2
cp -r $PACKAGE_DIRECTORY/tmp/${STACK}-${VERSION} $PACKAGE_DIRECTORY/tmp/$STACK
/usr/share/ros-build-tools/fix-python-scripts.sh $PACKAGE_DIRECTORY/tmp/$STACK
diff -Naur ${STACK}-${VERSION} $STACK > $PACKAGE_DIRECTORY/$STACK.patch || true
STACK_DEPENDENCIES=$(/usr/share/ros-build-tools/get-stack-dependencies.py $STACK/stack.xml \
    | sed 's/_/-/g' | sed 's/^/ros-electric-/g' | sed 's/ / ros-electric-/g')
cd $PACKAGE_DIRECTORY
rm -r $PACKAGE_DIRECTORY/tmp

PATCH_MD5=$(md5sum ${STACK}.patch | awk '{print $1}')

sed -i "s/@PACKAGE_NAME@/$PACKAGE/g" $PACKAGE_DIRECTORY/PKGBUILD
sed -i "s/@STACK_NAME@/$STACK/g" $PACKAGE_DIRECTORY/PKGBUILD
sed -i "s/@STACK_VERSION@/$VERSION/g" $PACKAGE_DIRECTORY/PKGBUILD
sed -i "s?@STACK_URL@?$URL?g" $PACKAGE_DIRECTORY/PKGBUILD
sed -i "s/@STACK_MD5@/$MD5/g" $PACKAGE_DIRECTORY/PKGBUILD
sed -i "s/@STACK_PATCH_MD5@/$PATCH_MD5/g" $PACKAGE_DIRECTORY/PKGBUILD
sed -i "s/@ROS_DISTRO@/$DISTRO/g" $PACKAGE_DIRECTORY/PKGBUILD
sed -i "s/@ROS_STACK_DEPENDENCIES@/$STACK_DEPENDENCIES/g" $PACKAGE_DIRECTORY/PKGBUILD

echo ""
echo "PKGBUILD and patch created for stack $STACK."
echo ""
echo "Fill in dependencies and the stack description."
