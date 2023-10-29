# Maintainer: Jingbei Li <i@jingbei.li>
# Contributer: Jose Riha <jose1711 gmail com>

pkgname=python-audioread
_pkgname=audioread
pkgver=3.0.1
pkgrel=1
pkgdesc="cross-library (GStreamer + Core Audio + MAD + FFmpeg) audio decoding for Python"
arch=('any')
url="https://github.com/beetbox/audioread"
license=(MIT)
depends=(python)
makedepends=(python-build python-flit-core python-installer python-setuptools python-wheel)
source=("$url/archive/v${pkgver}.tar.gz")
sha256sums=('98367fc46c436922e5c5b6aae59606c60c7ced36a0336cb8845fe85d0b2de383')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl
}

# vim:set ts=2 sw=2 et:
