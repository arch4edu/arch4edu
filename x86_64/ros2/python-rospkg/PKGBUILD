# Maintainer: Kartik Mohta <kartikmohta@gmail.com>

pkgname=('python-rospkg')
pkgver='1.6.1'
pkgrel=1
pkgdesc='Standalone Python library for the ROS package system'
arch=('any')
url='https://github.com/ros-infrastructure/rospkg'
license=('BSD')
depends=('python' 'python-catkin_pkg' 'python-distro' 'python-yaml')
makedepends=('python-setuptools')

conflicts=('python2-rospkg')
source=("https://github.com/ros-infrastructure/rospkg/archive/${pkgver}.tar.gz")
sha256sums=('2c4109a02367d56b1e4ceeb86c6faed4bb423643580b3274fcaa2a22a1a3380a')

_module='rospkg'

build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
