# Maintainer: Kartik Mohta <kartikmohta@gmail.com>

pkgname=('python-catkin_pkg')
pkgver='1.1.0'
pkgrel=1
pkgdesc='Standalone Python library for the catkin package system'
arch=('any')
url='https://github.com/ros-infrastructure/catkin_pkg'
license=('BSD')
depends=('python' 'python-dateutil' 'python-docutils' 'python-pyparsing' 'python-setuptools')
makedepends=('python-setuptools')
provides=('python-catkin-pkg')
conflicts=('python2-catkin_pkg' 'python-catkin-pkg')
source=("https://github.com/ros-infrastructure/catkin_pkg/archive/${pkgver}.tar.gz")
sha256sums=('32c0410cb815497a0253838ca8f7d222d345a3bbd189fa4e61374a8f77c42709')

_module='catkin_pkg'

build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
