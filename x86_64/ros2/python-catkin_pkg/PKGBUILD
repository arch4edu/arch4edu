# Maintainer: Kartik Mohta <kartikmohta@gmail.com>

pkgname=('python-catkin_pkg')
pkgver='1.0.0'
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
sha256sums=('48e88c995838807165bb70c6272abab2d6dda5efc210f62db8ac714d4c96a0c6')

_module='catkin_pkg'

build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
