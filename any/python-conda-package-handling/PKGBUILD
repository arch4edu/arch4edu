# Maintainer: Daniel Maslowski <info@orangecms.org>
# Co-Maintainer: Ke Liu <specter119@gmail.com>

pkgname=python-conda-package-handling
pkgver=2.6.0
_srcname="conda-package-handling-${pkgver}"
pkgrel=1
pkgdesc="Create and extract conda package of various formats"
arch=('any')
url="https://github.com/conda/conda-package-handling"
license=('BSD-3-Clause')
depends=(
  python
  'python-conda-package-streaming>=0.13.0'
  python-requests
)
makedepends=(
  python-build
  python-installer
  python-flit-core
  python-wheel
)
options=(!emptydirs)
install=
source=(
  "${_srcname}.tar.gz::$url/archive/$pkgver.tar.gz"
)
sha512sums=(
  '3844a4d6fb7c81c3949ed7f679ec41692b56a55f6d714ae57dfb20b8f10e9f50135a8e4dd3f67653f6a34c1c5c5b1fc92f8cd82f181474f5d34e3ed059a4fa76'
)

prepare() {
  cd "$srcdir/${_srcname}"
  # upstream pins flit_core <4; Arch ships 4.x. Matches upstream conda-package-streaming PR #195.
  sed -i 's/flit_core >=3.2,<4/flit_core >=3.2,<5/' pyproject.toml
}

build() {
  cd "$srcdir/${_srcname}"
  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir/${_srcname}"
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE "$pkgdir/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
