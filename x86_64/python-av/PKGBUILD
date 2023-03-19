# Maintainer: peippo <christoph+aur@christophfink.com>

pkgname=python-av
_name=${pkgname#python-}
pkgdesc="Pythonic bindings for FFmpeg"
url="https://docs.mikeboers.com/pyav/"

pkgver=10.0.0
pkgrel=2

arch=("x86_64" "i686")
license=("BSD")

depends=(
    "ffmpeg4.4"
    "python"
    "python-numpy"
    "python-pillow"
)
makedepends=(
    "cython"
    "python-google-api-core"
    "python-setuptools"
    "python-wheel"
    "pkgconf"
)
checkdepends=(
    "autopep8"
    "flake8"
    "python-editorconfig"
    "python-isort"
    "python-pytest"
    "python-sphinx"
)

source=( "https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
b2sums=('0771fb37de072b63b8f276a2c3f76461af52910433793c7261f8216ab0af58ca46d8da871352d419c231a41fdb73b7e65f8d9eb71373f540cd3407148605ea74')

build() {
    export PKG_CONFIG_PATH="/usr/lib/ffmpeg4.4/pkgconfig"

    cd "${srcdir}"/${_name}-${pkgver}
    python setup.py build_ext --inplace
    python setup.py build
}

check() {
    cd "${srcdir}"/${_name}-${pkgver}
    export PYTHONPATH="${srcdir}/${_name}-${pkgver}/build/lib.linux-$CARCH-${python_version}"
    python -m pytest
}

package() {
    cd "${srcdir}/${_name}-${pkgver}"
    python setup.py install --root="${pkgdir}" --optimize=1
    install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/python-av/LICENSE"
}
