# Maintainer: Kartik Mohta <kartikmohta@gmail.com>

pkgname=('python-rospkg')
pkgver='1.5.0'
pkgrel=1
pkgdesc='Standalone Python library for the ROS package system'
arch=('any')
url='https://github.com/ros-infrastructure/rospkg'
license=('BSD')
depends=('python' 'python-catkin_pkg' 'python-distro' 'python-yaml')
makedepends=('python-setuptools')

conflicts=('python2-rospkg')
source=("https://github.com/ros-infrastructure/rospkg/archive/${pkgver}.tar.gz")
sha256sums=('6290b6ffb69aec9c00178345ddc9036aaecf29ca3bc17ba21eee63d9d4d8ff31')

_module='rospkg'

build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
