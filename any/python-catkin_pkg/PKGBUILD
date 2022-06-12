# Maintainer: Kartik Mohta <kartikmohta@gmail.com>

pkgname=('python-catkin_pkg')
pkgver='0.4.24'
pkgrel=2
pkgdesc='Standalone Python library for the catkin package system'
arch=('any')
url='https://github.com/ros-infrastructure/catkin_pkg'
license=('BSD')
depends=('python' 'python-argparse' 'python-dateutil' 'python-docutils' 'python-pyparsing')
makedepends=('python-setuptools')
provides=('python-catkin-pkg')
conflicts=('python2-catkin_pkg' 'python-catkin-pkg')
source=("https://github.com/ros-infrastructure/catkin_pkg/archive/${pkgver}.tar.gz"
        "setuptools-replace-newlines-in-description.patch")
sha256sums=('57ea09fd51d9a67ccf5a0660a8f84794304182c4f644f27ad835a979567893b1'
            '0575506c2b25f44e6900f30c320b3dbdd6726174ab1ff45b22d8445b5a42f331')

_module='catkin_pkg'

prepare() {
    cd "${srcdir}/${_module}-${pkgver}"
    patch --forward --strip=1 -i "${srcdir}/setuptools-replace-newlines-in-description.patch"
}

build() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_module}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
