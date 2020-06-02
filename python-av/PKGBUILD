# Maintainer: peippo <christoph+aur@christophfink.com>

pkgname="python-av"
_name=${pkgname#python-}
pkgdesc="Pythonic bindings for FFmpeg"
url="https://docs.mikeboers.com/pyav/"

pkgver=8.0.2
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
sha256sums=("a3bba6bf68766b8a1a057f28869c7078cf0a1ec3207c7788c2ce8fe6f6bd8267")

build() {
    cd "${srcdir}"/${_name}-${pkgver}
    python setup.py build
}

package() {
    cd "${srcdir}/${_name}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1

    install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/python-av/LICENSE"
}
