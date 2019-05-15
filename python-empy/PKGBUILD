# Maintainer: Kartik Mohta <kartikmohta@gmail.com>
# Contributor: Benjamin Chretien <chretien at lirmm dot fr>
# Contributor: Andrew Conkling <andrewski@fr.st>
pkgname=python-empy
pkgver=3.3.4
pkgrel=1
pkgdesc="A powerful and robust templating system for Python."
arch=('any')
url="http://www.alcyone.com/software/empy"
depends=('python')
license=('LGPL')
source=("http://www.alcyone.com/software/empy/empy-${pkgver}.tar.gz")
sha256sums=('9126211471fc7ff83fdd40beca93eb6de5681758fbe68b4cf8af6326259df1b1')

build() {
    cd "${srcdir}/empy-${pkgver}"
    python3 setup.py build
}

package() {
    cd "${srcdir}/empy-${pkgver}"
    python3 setup.py install -O2 --skip-build --prefix=/usr --root="${pkgdir}"
}
