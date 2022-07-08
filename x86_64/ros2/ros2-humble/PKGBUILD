# Maintainer: Mohammad Mostafa Farzan <m2_farzan@yahoo.com>
# Contributor: mjbogusz <mjbogusz+github@gmail.com>
# Contributor: yuanyuyuan <az6980522@gmail.com>
# Contributor: Rémy B. (github.com/KirrimK)
# Contributor: Renato Caldas (github.com/rmsc)
# Contributor: goekce (github.com/goekce)
# Contributor: David Castellon (github.com/bobosito000)
# Acknowledgment: This work is hugely based on `ros2-arch-deps` AUR
# package, maintained by T. Borgert.

pkgname=ros2-humble
pkgver=2022.05.23
pkgrel=1
pkgdesc="A set of software libraries and tools for building robot applications"
url="https://docs.ros.org/en/humble/"
arch=('any')
license=('Apache')
depends=(
    'ros2-arch-deps'
    'ros2-pyqt5-sip-compat'
    'assimp'
    'gmock'
    'sip4'
)
source=(
    "ros2::git+https://github.com/ros2/ros2#tag=release-humble-20220523"
)
sha256sums=(
    'SKIP'
)
install=ros2-humble.install

prepare() {
    # Check locale according to
    # https://docs.ros.org/en/rolling/Installation/Ubuntu-Development-Setup.html#set-locale
    if ! locale | grep LANG | grep UTF-8 > /dev/null; then
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
    ## osrf_testing_tools_cpp
    git -C $srcdir/ros2/src/osrf/osrf_testing_tools_cpp cherry-pick 869da204dd829308380df5a33e432670e474e54a
    ## performance_test_fixture
    git -C $srcdir/ros2/src/ros2/performance_test_fixture cherry-pick d736c276d292a78f9750aba39108d5222bf9629e
    ## rmw_cyclonedds_cpp
    git -C $srcdir/ros2/src/ros2/rmw_cyclonedds cherry-pick f57732d15be53796d518e12352866124efcaa939
}

build() {
    # Disable parallel build if RAM is low
    if [[ $(free | grep -Po "Mem:\s+\K\d+") -lt 16000000 ]]; then
        printf "\nRAM is smaller than 16 GB. Parallel build will be disabled for stability.\n\n"
        export COLCON_EXTRA_ARGS="${COLCON_EXTRA_ARGS} --executor sequential"
    fi

    ## For people with the old version of makepkg.conf
    unset CPPFLAGS
    ## For people with the new version of makepkg.conf
    CFLAGS=$(sed "s/-Wp,-D_FORTIFY_SOURCE=2\s//g" <(echo $CFLAGS))
    CXXFLAGS=$(sed "s/-Wp,-D_FORTIFY_SOURCE=2\s//g" <(echo $CXXFLAGS))

    # Build
    colcon build --merge-install ${COLCON_EXTRA_ARGS}
}

package() {
    mkdir -p $pkgdir/opt/ros/humble
    cp -r $srcdir/install/* $pkgdir/opt/ros/humble/
}
