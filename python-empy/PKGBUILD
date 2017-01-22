# Maintainer: Benjamin Chretien <chretien at lirmm dot fr>
# Contributor: Andrew Conkling <andrewski@fr.st>
pkgname=python-empy
realname=empy
pkgver=3.3.2
pkgrel=5
pkgdesc="A powerful and robust templating system for Python."
arch=(i686 x86_64)
url="http://www.alcyone.com/software/empy"
depends=('python>=3')
license=('LGPL')
source=("http://www.alcyone.com/software/empy/empy-$pkgver.tar.gz")
sha256sums=('99f016af2770c48ab57a65df7aae251360dc69a1514c15851458a71d4ddfea9c')

build() {
    cd ${srcdir}/empy-$pkgver
    python3 setup.py build
}

package() {
    cd ${srcdir}/empy-$pkgver
    python3 setup.py install -O2 --skip-build --prefix=/usr --root=${pkgdir}

    # Make em.py executable
    chmod a+x ${pkgdir}/usr/lib/python3.5/site-packages/em.py
}
