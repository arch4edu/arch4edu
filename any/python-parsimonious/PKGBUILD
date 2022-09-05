# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Wojciech Szymecki <w.szymecki-at-g;mail-com>

pkgname=python-parsimonious
pkgver=0.10.0
pkgrel=1
pkgdesc="Fast parser based on parsing expression grammars (PEGs)"
arch=('any')
url="https://github.com/erikrose/parsimonious"
license=('MIT')
depends=('python-regex')
makedepends=('python' 'python-build' 'python-installer' 'python-wheel'
             'python-setuptools')
source=("$pkgname-$pkgver::https://github.com/erikrose/parsimonious/archive/$pkgver.tar.gz")
sha256sums=('5fb1a5084d603e890d4fad10fd78ae10962a7a60810d18b2d723570dfd827055')

_pkgname="parsimonious"

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
