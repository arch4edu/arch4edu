# Maintainer: Kartik Mohta <kartikmohta@gmail.com>

pkgname=('python-rospkg')
pkgver='1.6.0'
pkgrel=1
pkgdesc='Standalone Python library for the ROS package system'
arch=('any')
url='https://github.com/ros-infrastructure/rospkg'
license=('BSD')
depends=('python' 'python-catkin_pkg' 'python-distro' 'python-yaml')
makedepends=('python-setuptools')

conflicts=('python2-rospkg')
source=("https://github.com/ros-infrastructure/rospkg/archive/${pkgver}.tar.gz")
sha256sums=('9341c8af5f547888ab484ee61b53d8447b6a52081222d2d5257757ab374c657f')

_module='rospkg'

build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
