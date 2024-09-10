# Maintainer: Kartik Mohta <kartikmohta@gmail.com>

pkgname=('python-rosdep')
pkgver='0.25.1'
pkgrel=1
pkgdesc='rosdep package manager abstraction tool for ROS'
arch=('any')
url='https://github.com/ros-infrastructure/rosdep'
license=('BSD')
depends=('python' 'python-catkin_pkg' 'python-rosdistro' 'python-rospkg' 'python-setuptools' 'python-yaml')
makedepends=('python-setuptools')

conflicts=('python2-rosdep')
source=("https://github.com/ros-infrastructure/rosdep/archive/${pkgver}.tar.gz")
sha256sums=('1806643fe873716f72756bb690633b1e3087e7516e203439fbbb97494bf1e66e')

_module='rosdep'

build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
