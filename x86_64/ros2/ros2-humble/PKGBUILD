# Maintainer: Mohammad Mostafa Farzan <m2_farzan@yahoo.com>
# Contributor: mjbogusz <mjbogusz+github@gmail.com>
# Contributor: yuanyuyuan <az6980522@gmail.com>
# Contributor: Rémy B. (github.com/KirrimK)
# Contributor: Renato Caldas (github.com/rmsc)
# Contributor: goekce (github.com/goekce)
# Contributor: David Castellon (github.com/bobosito000)
# Contributor: Yannic Wehner <yannic.wehner@gmail.com> (github.com/ElCap1tan)
# Contributor: Kino <github.com/cybaol>
# Contributor: Zijian <github.com/zijian-x>
# Contributor: Jingbei Li <github.com/petronny>
# Contributor: Levi Tempfli <github.com/levtempfli>
# Acknowledgment: This work is hugely based on `ros2-arch-deps` AUR
# package, maintained by T. Borgert.

pkgname=ros2-humble
pkgver=2025.03.31
pkgrel=2
pkgdesc="A set of software libraries and tools for building robot applications"
url="https://docs.ros.org/en/humble/"
arch=('x86_64')
license=('Apache')
depends=(
    'ros2-arch-deps'
    'qt6-base'
    'nvidia-cg-toolkit'
    'assimp'
    'gmock'
)
makedepends=('cmake3' 'git' 'gcc13')
provides=('ros2-humble-base')
conflicts=('ros2-humble-base')
source=(
    "ros2::git+https://github.com/ros2/ros2#tag=humble-${pkgver//.}"
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

    cd $srcdir/ros2/src/eProsima/Fast-DDS
    git submodule update --init thirdparty/asio

    # pybind11_vendor: Use jazzy branch to make compatible with Python 3.11 and later.
    git -C $srcdir/ros2/src/ros2/pybind11_vendor checkout 3.1.3
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
    CFLAGS=$(sed "s/-Wp,-D_FORTIFY_SOURCE=[23]\s//g" <(echo $CFLAGS))
    CXXFLAGS=$(sed "s/-Wp,-D_FORTIFY_SOURCE=[23]\s//g" <(echo $CXXFLAGS))

    # Build
    ## Downgrade gcc to fix missing cstdint headers in many packages.
    export CC=$(command -v gcc-13) CXX=$(command -v g++-13)
    ## To resolve the io_service removal in Asio 1.33.0, build FastRTPS against third-party Asio.
    colcon build --merge-install --packages-up-to fastrtps --cmake-args " -DTHIRDPARTY_Asio=FORCE"
    colcon build --merge-install ${COLCON_EXTRA_ARGS} --cmake-args " -DBUILD_TESTING=OFF -Wno-dev" --packages-ignore qt_gui_cpp rqt_gui_cpp
}

package() {
    mkdir -p $pkgdir/opt/ros/humble
    cp -r $srcdir/install/* $pkgdir/opt/ros/humble/
}
