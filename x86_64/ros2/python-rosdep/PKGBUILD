# Maintainer: Kartik Mohta <kartikmohta@gmail.com>

pkgname=('python-rosdep')
pkgver='0.26.0'
pkgrel=1
pkgdesc='rosdep package manager abstraction tool for ROS'
arch=('any')
url='https://github.com/ros-infrastructure/rosdep'
license=('BSD')
depends=('python' 'python-catkin_pkg' 'python-rosdistro' 'python-rospkg' 'python-setuptools' 'python-yaml')
makedepends=('python-setuptools')

conflicts=('python2-rosdep')
source=("https://github.com/ros-infrastructure/rosdep/archive/${pkgver}.tar.gz")
sha256sums=('ceb6fe4ee6f2f356196506814f4a7d22f7f232fb194e6d3cff91182a9c8480d3')

_module='rosdep'

build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
