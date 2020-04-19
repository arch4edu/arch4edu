# Maintainer: Kartik Mohta <kartikmohta@gmail.com>

pkgbase='python-catkin_pkg'
pkgname=('python-catkin_pkg')
_module='catkin_pkg'
pkgver='0.4.17'
pkgrel=1
pkgdesc="catkin package library"
url="http://wiki.ros.org/catkin_pkg"
depends=('python' 'python-argparse' 'python-dateutil' 'python-docutils')
provides=('python-catkin-pkg')
conflicts=('python2-catkin_pkg' 'python-catkin-pkg')
makedepends=('python-setuptools')
license=('BSD')
arch=('any')
source=("https://files.pythonhosted.org/packages/source/${_module::1}/$_module/$_module-$pkgver.tar.gz")
sha256sums=('8a99a12323f22714193b411753288457a7cfb4bd53ef1e595e92d183b144a639')

build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
