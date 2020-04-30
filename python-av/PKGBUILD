# Maintainer: peippo <christoph+aur@christophfink.com>

pkgname="python-av"
_name=${pkgname#python-}
pkgdesc="Pythonic bindings for FFmpeg"
url="https://docs.mikeboers.com/pyav/"

pkgver=8.0.1
pkgrel=0

arch=("x86_64" "i686")
license=("BSD")

makedepends=(
    "cython"
    "python-setuptools"
    "pkgconf"
)
depends=(
    "python"
    "ffmpeg"
)

source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha256sums=("27939405a78dbbb6b06e452fe505e12f30c32c6967ef164abbefa9525384dad3")

build() {
    cd "${srcdir}"/${_name}-${pkgver}
    python setup.py build
}

package() {
    cd "${srcdir}/${_name}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1

    install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/python-av/LICENSE"
}
