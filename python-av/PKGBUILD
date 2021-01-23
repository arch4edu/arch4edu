# Maintainer: peippo <christoph+aur@christophfink.com>

pkgname="python-av"
_name=${pkgname#python-}
pkgdesc="Pythonic bindings for FFmpeg"
url="https://docs.mikeboers.com/pyav/"

pkgver=8.0.3
pkgrel=1

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
sha256sums=("521814309c91d526b6b5c9517018aef2dd12bc3d86351037db69aa67730692b8")

build() {
    cd "${srcdir}"/${_name}-${pkgver}
    python setup.py build
}

package() {
    cd "${srcdir}/${_name}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1

    install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/python-av/LICENSE"
}
