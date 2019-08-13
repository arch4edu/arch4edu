# Maintainer: peippo <christoph.fink@gmail.com>

pkgbase=python-av
pkgname=(
    "python-av"
    "python2-av"
)
pkgdesc="Pythonic bindings for FFmpeg"
url="https://docs.mikeboers.com/pyav/"

pkgver=6.2.0
pkgrel=0

arch=("any")
license=("BSD")

makedepends=(
    "python-setuptools"
    "python2-setuptools"
    "cython"
    "cython2"
)
depends=(
    "python"
    "python2"
    "ffmpeg"
)

source=("https://github.com/mikeboers/PyAV/archive/v${pkgver}.tar.gz")
sha256sums=("312dbcd3efa5bc060ce6003f2579a65b1e8c017473fb55755e8e148b87dcf696")

prepare() {
    cd "${srcdir}/PyAV-${pkgver}"
}

build() {
    cp -r "${srcdir}/PyAV-${pkgver}" "${srcdir}/PyAV-${pkgver}-py2"

    cd "${srcdir}"/PyAV-${pkgver}
    python setup.py build

    cd "${srcdir}"/PyAV-${pkgver}-py2
    python2 setup.py build
}

package_python-av() {
    cd "${srcdir}/PyAV-${pkgver}"
    python setup.py install --root=${pkgdir} --optimize=1

    install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/python-av/LICENSE"
}

package_python2-av() {
    cd "${srcdir}/PyAV-${pkgver}-py2"
    python2 setup.py install --root=${pkgdir} --optimize=1

    # rename /usr/bin/pyav to avoid filename conflict
    mv "${pkgdir}/usr/bin/pyav" "${pkgdir}/usr/bin/pyav2"

    install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/python2-av/LICENSE"
}
