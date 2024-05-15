# Maintainer: Kartik Mohta <kartikmohta@gmail.com>

pkgname=('python-rosdistro')
pkgver='0.9.1'
pkgrel=1
pkgdesc='A tool to work with rosdistro files'
arch=('any')
url='https://github.com/ros-infrastructure/rosdistro'
license=('BSD')
depends=('python' 'python-catkin_pkg' 'python-rospkg' 'python-setuptools' 'python-yaml')
makedepends=('python-setuptools')

conflicts=('python2-rosdistro')
source=("https://github.com/ros-infrastructure/rosdistro/archive/${pkgver}.tar.gz")
sha256sums=('1ab7ce5e09432b0d4c00ffd2405101bb9b168e13181b4779f5d0c6935806e904')

_module='rosdistro'

build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
