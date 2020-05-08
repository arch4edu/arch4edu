# Maintainer: Kartik Mohta <kartikmohta@gmail.com>

pkgbase='python-catkin_pkg'
pkgname=('python-catkin_pkg')
_module='catkin_pkg'
pkgver='0.4.18'
pkgrel=1
pkgdesc="catkin package library"
url="http://wiki.ros.org/catkin_pkg"
depends=('python' 'python-argparse' 'python-dateutil' 'python-docutils' 'python-pyparsing')
provides=('python-catkin-pkg')
conflicts=('python2-catkin_pkg' 'python-catkin-pkg')
makedepends=('python-setuptools')
license=('BSD')
arch=('any')
source=("https://files.pythonhosted.org/packages/source/${_module::1}/$_module/$_module-$pkgver.tar.gz")
sha256sums=('5f885ae05e8655bff897f3f9acd4469801583fcb02bae73ff9ea55b8208e3f9d')

build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
