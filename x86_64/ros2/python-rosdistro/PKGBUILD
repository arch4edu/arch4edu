# Maintainer: Kartik Mohta <kartikmohta@gmail.com>

pkgname=('python-rosdistro')
pkgver='1.1.0'
pkgrel=1
pkgdesc='A tool to work with rosdistro files'
arch=('any')
url='https://github.com/ros-infrastructure/rosdistro'
license=('BSD')
depends=('python' 'python-catkin_pkg' 'python-rospkg' 'python-setuptools' 'python-yaml')
makedepends=('python-setuptools')

conflicts=('python2-rosdistro')
source=("https://github.com/ros-infrastructure/rosdistro/archive/${pkgver}.tar.gz")
sha256sums=('4b30eb3d7b81ea1e4c4978c716a838856d0f39b33450724dd2189e8b46692e25')

_module='rosdistro'

build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
