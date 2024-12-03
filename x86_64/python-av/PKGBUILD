# Maintainer: peippo <christoph+aur@christophfink.com>

pkgname=python-av
_name=${pkgname#python-}
_upstream_name="PyAV"
pkgdesc="Pythonic bindings for FFmpeg"
url="https://pyav.basswood-io.com"

pkgver=14.0.0
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
b2sums=("aa51d78a7f0c5ba73aa9c459b4cfdd30ce77ae835660145d4d40cf212485dfe71e8b4a78d5f910f053c003c5efb530f9055a1ee508ae9007051a52b1b82ecbc3")

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
