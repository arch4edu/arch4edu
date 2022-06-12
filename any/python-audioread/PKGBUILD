# Maintainer: Jingbei Li <i@jingbei.li>
# Contributer: Jose Riha <jose1711 gmail com>
pkgname=python-audioread
_pkgname=audioread
pkgver=2.1.9
pkgrel=1
pkgdesc="cross-library (GStreamer + Core Audio + MAD + FFmpeg) audio decoding for Python"
arch=('any')
url="https://github.com/beetbox/audioread"
license=('MIT')
makedepends=('python-setuptools')
source=("$url/archive/v${pkgver}.tar.gz")
sha256sums=('f379b0015791cc81a5a2c24f6b77a1f08dc885145f33a800db2ec69ce9e4df4e')

build() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py build
}

package_python-audioread() {
  depends=('python')
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir"/ --optimize=1
}

# vim:set ts=2 sw=2 et:
