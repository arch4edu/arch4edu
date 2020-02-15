# Maintainer: Dobroslaw Kijowski [dobo] <dobo90_at_gmail.com>

pkgname=lief
pkgver=0.10.1
pkgrel=1
pkgdesc='Library to instrument executable formats'
arch=(i686  x86_64)
url='https://lief.quarkslab.com/'
license=(APACHE)
depends=(python)
makedepends=(git cmake python-setuptools)
source=("git+git://github.com/lief-project/LIEF#tag=${pkgver}")
md5sums=(SKIP)

build() {
  cd "${srcdir}/LIEF"
  python setup.py build
}

package() {
  cd "${srcdir}/LIEF"
  python setup.py install --root="${pkgdir}" --optimize=1
}
