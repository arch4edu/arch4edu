# Maintainer: Mohammad Mostafa Farzan <m2_farzan@yahoo.com>
# Contributor: mjbogusz <mjbogusz+github@gmail.com>
# Contributor: yuanyuyuan <az6980522@gmail.com>
# Contributor: Rémy B. (github.com/KirrimK)
# Contributor: Renato Caldas (github.com/rmsc)
# Contributor: goekce (github.com/goekce)
# Contributor: David Castellon (github.com/bobosito000)
# Contributor: Yannic Wehner <yannic.wehner@gmail.com> (github.com/ElCap1tan)
# Acknowledgment: This work is hugely based on `ros2-arch-deps` AUR
# package, maintained by T. Borgert.

pkgname=ros2-humble
pkgver=2023.09.25
pkgrel=2
pkgdesc="A set of software libraries and tools for building robot applications"
url="https://docs.ros.org/en/humble/"
arch=('any')
license=('Apache')
depends=(
    'ros2-arch-deps'
    'qt6-base'
    'nvidia-cg-toolkit'
    'assimp'
    'gmock'
)
makedepends=('git')
source=(
    "ros2::git+https://github.com/ros2/ros2#tag=release-humble-${pkgver//.}"
)
sha256sums=('SKIP')
install=ros2-humble.install

prepare() {
    # Check locale according to
    # https://docs.ros.org/en/rolling/Installation/Ubuntu-Development-Setup.html#set-locale
        if ! locale | grep LANG | grep 'UTF-8\|utf8' > /dev/null; then
        echo 'Your locale must support UTF-8. See ' \
             'https://wiki.archlinux.org/index.php/locale and ' \
             'https://docs.ros.org/en/rolling/Installation/Ubuntu-Development-Setup.html#set-locale'
        exit 1
    fi

    # Clone the repos
    mkdir -p $srcdir/ros2/src
    vcs import $srcdir/ros2/src < $srcdir/ros2/ros2.repos

    # Setup git (required for the cherry-pick commands)
    export GIT_COMMITTER_NAME="PKGBUILD"
    export GIT_COMMITTER_EMAIL="pkgbuild@example.com"
    export GIT_AUTHOR_NAME="PKGBUILD"
    export GIT_AUTHOR_EMAIL="pkgbuild@example.com"

    # Fix some issues in the code (TODO: Gradually move to upstream)
    ## rcpputils: fix missing cstdint include
    git -C $srcdir/ros2/src/ros2/rcpputils cherry-pick f96811a9047fa6a084a885219c88b415bc544487
    ## libstatistics_collector: Fix missing cstdint include
    git -C $srcdir/ros2/src/ros-tooling/libstatistics_collector cherry-pick 1c340c97c731019d0c7b40f8c167b0ef666bcf75
    ## rclcpp: Fix missing stdexcept includes
    git -C $srcdir/ros2/src/ros2/rclcpp cherry-pick 86c77143c96d85711a87f2a5adcc4d7f0fb0dbeb
    ## pybind11_vendor: Support for python 3.11
    git -C $srcdir/ros2/src/ros2/pybind11_vendor checkout 3.0.3
    ## rosbag2_compression: cherry pick to fix missing cstdint include
    git -C $srcdir/ros2/src/ros2/rosbag2 cherry-pick 65c889e1fa55dd85a148b27b8c27dadc73238e67
}

build() {
    # Disable parallel build if RAM is low
    MIN_PARALLEL_BUILD_RAM_KB=16000000
    if [[ $(free | grep -Po "Mem:\s+\K\d+") -lt $MIN_PARALLEL_BUILD_RAM_KB && $(grep MemTotal /proc/meminfo | grep -Po "MemTotal:\s+\K\d+") -lt $MIN_PARALLEL_BUILD_RAM_KB ]]; then
        printf "\nRAM is smaller than 16 GB. Parallel build will be disabled for stability.\n\n"
        export COLCON_EXTRA_ARGS="${COLCON_EXTRA_ARGS} --executor sequential"
    fi

    ## For people with the old version of makepkg.conf
    unset CPPFLAGS
    ## For people with the new version of makepkg.conf
    CFLAGS=$(sed "s/-Wp,-D_FORTIFY_SOURCE=2\s//g" <(echo $CFLAGS))
    CXXFLAGS=$(sed "s/-Wp,-D_FORTIFY_SOURCE=2\s//g" <(echo $CXXFLAGS))

    # Build
    colcon build --merge-install ${COLCON_EXTRA_ARGS} --cmake-args -Wno-dev
}

package() {
    mkdir -p $pkgdir/opt/ros/humble
    cp -r $srcdir/install/* $pkgdir/opt/ros/humble/
}
