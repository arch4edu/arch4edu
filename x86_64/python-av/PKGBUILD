# Maintainer: peippo <christoph+aur@christophfink.com>

pkgname=python-av
_name=${pkgname#python-}
_upstream_name="PyAV"
pkgdesc="Pythonic bindings for FFmpeg"
url="https://pyav.basswood-io.com"

pkgver=13.1.0
pkgrel=1

arch=("x86_64" "i686")
license=("BSD-3-Clause")

depends=(
  "ffmpeg"
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

source=(
  "$_name-$pkgver.tar.gz::https://github.com/${_upstream_name}-Org/${_upstream_name}/archive/refs/tags/v${pkgver}.tar.gz"
)
b2sums=("0c34d65a23998af1b61c7ac4610891f3e38dfa8cf6f5eadaf123eea61c4cf010a7a48de8ef26db195b48edc06e256cb5a94794212f0d7c6ae4a3e82ae5725b3e")

build() {
  cd "${srcdir}"/${_upstream_name}-${pkgver}

  export PKG_CONFIG_PATH="/usr/lib/ffmpeg6.1/pkgconfig/"

  python setup.py build_ext --inplace
  python setup.py build
}

check() {
  cd "${srcdir}"/${_upstream_name}-${pkgver}

  local python_version=$(python -c 'import sys; print("".join(map(str, sys.version_info[:2])))')
  export PYTHONPATH="${srcdir}/${_upstream_name}-${pkgver}/build/lib.linux-${CARCH}-cpython-${python_version}"

  python -m pytest
}

package() {
  cd "${srcdir}/${_upstream_name}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/python-av/LICENSE"
}
