# Maintainer: peippo <christoph+aur@christophfink.com>

pkgname=python-av
_name=${pkgname#python-}
_upstream_name="PyAV"
pkgdesc="Pythonic bindings for FFmpeg"
url="https://pyav.basswood-io.com"

pkgver=12.3.0
pkgrel=1

arch=("x86_64" "i686")
license=("BSD-3-Clause")

depends=(
  # "ffmpeg<=2:7"
  "ffmpeg6.1"
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
b2sums=("d80f642fddb4112a89540d7b443ae5df0989b61507f18009a651fa311925d5041e2e9bd7f6c68d34abaca9fd33609692dc289e025dc7855c497517da8a92f3f0")

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
