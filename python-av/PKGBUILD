# Maintainer: peippo <christoph.fink@gmail.com>

pkgname="python-av"
pkgdesc="Pythonic bindings for FFmpeg"
url="https://docs.mikeboers.com/pyav/"

pkgver=6.2.0
pkgrel=3

arch=("any")
license=("BSD")

makedepends=(
    "python-setuptools"
    "cython"
)
depends=(
    "python"
    "ffmpeg"
)

source=("https://github.com/mikeboers/PyAV/archive/v${pkgver}.tar.gz")
sha256sums=("312dbcd3efa5bc060ce6003f2579a65b1e8c017473fb55755e8e148b87dcf696")

prepare() {
    cd "${srcdir}/PyAV-${pkgver}"
}

build() {
    cd "${srcdir}"/PyAV-${pkgver}
    python setup.py build
}

package() {
    cd "${srcdir}/PyAV-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1

    install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/python-av/LICENSE"
}
