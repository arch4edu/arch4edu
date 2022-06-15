# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Wojciech Szymecki <w.szymecki-at-g;mail-com>

pkgname=python-parsimonious
pkgver=0.9.0
pkgrel=1
pkgdesc="Fast parser based on parsing expression grammars (PEGs)"
arch=('any')
url="https://github.com/erikrose/parsimonious"
license=('MIT')
depends=('python-regex')
makedepends=('python' 'python-build' 'python-installer' 'python-wheel'
             'python-setuptools')
source=("$pkgname-$pkgver::https://github.com/erikrose/parsimonious/archive/$pkgver.tar.gz")
sha256sums=('ed53ea31c9b2461c0ac607c03cdf216229ef33bab324e96ed140d450a3e0bdf9')

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
