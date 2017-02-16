# Maintainer: Benjamin Chretien <chretien at lirmm dot fr>
# Contributor: Andrew Conkling <andrewski@fr.st>
pkgname=python-empy
pkgver=3.3.3
pkgrel=1
pkgdesc="A powerful and robust templating system for Python."
arch=(i686 x86_64)
url="http://www.alcyone.com/software/empy"
depends=('python')
license=('LGPL')
source=("http://www.alcyone.com/software/empy/empy-${pkgver}.tar.gz")
sha256sums=('9841e36dd26c7f69fe1005f9d9e078e41bdd50dd56fc77837ae390fb6af1aed7')

build() {
    cd "${srcdir}/empy-${pkgver}"
    python3 setup.py build
}

package() {
    cd "${srcdir}/empy-${pkgver}"
    python3 setup.py install -O2 --skip-build --prefix=/usr --root="${pkgdir}"

    # Make em.py executable
    chmod a+x "${pkgdir}/usr/lib/python3.6/site-packages/em.py"
}
