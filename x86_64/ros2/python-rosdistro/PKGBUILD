# Maintainer: Kartik Mohta <kartikmohta@gmail.com>

pkgname=('python-rosdistro')
pkgver='1.0.1'
pkgrel=1
pkgdesc='A tool to work with rosdistro files'
arch=('any')
url='https://github.com/ros-infrastructure/rosdistro'
license=('BSD')
depends=('python' 'python-catkin_pkg' 'python-rospkg' 'python-setuptools' 'python-yaml')
makedepends=('python-setuptools')

conflicts=('python2-rosdistro')
source=("https://github.com/ros-infrastructure/rosdistro/archive/${pkgver}.tar.gz")
sha256sums=('aeb1b2f5c065b79840df979f2c4e11ee05328eb6e86e8df9111019a4f0e42260')

_module='rosdistro'

build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
