# Maintainer: Kartik Mohta <kartikmohta@gmail.com>

pkgname=('python-rospkg')
pkgver='1.5.1'
pkgrel=1
pkgdesc='Standalone Python library for the ROS package system'
arch=('any')
url='https://github.com/ros-infrastructure/rospkg'
license=('BSD')
depends=('python' 'python-catkin_pkg' 'python-distro' 'python-yaml')
makedepends=('python-setuptools')

conflicts=('python2-rospkg')
source=("https://github.com/ros-infrastructure/rospkg/archive/${pkgver}.tar.gz")
sha256sums=('2ad2065ce60dcbdf8c6bec4fc907d05c5a9ce194692ca348e7476dc5c9229270')

_module='rospkg'

build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
