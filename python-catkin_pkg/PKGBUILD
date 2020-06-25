# Maintainer: Kartik Mohta <kartikmohta@gmail.com>

pkgname=('python-catkin_pkg')
pkgver='0.4.22'
pkgrel=1
pkgdesc='Standalone Python library for the catkin package system'
arch=('any')
url='https://github.com/ros-infrastructure/catkin_pkg'
license=('BSD')
depends=('python' 'python-argparse' 'python-dateutil' 'python-docutils' 'python-pyparsing')
makedepends=('python-setuptools')
provides=('python-catkin-pkg')
conflicts=('python2-catkin_pkg' 'python-catkin-pkg')
source=("https://github.com/ros-infrastructure/catkin_pkg/archive/${pkgver}.tar.gz")
sha256sums=('0b84e304ffbc829ce800f14ab71b67594ae9027ef80dd145583273ffe861e2be')

_module='catkin_pkg'

build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
