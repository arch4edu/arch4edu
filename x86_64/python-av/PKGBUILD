# Maintainer: peippo <christoph+aur@christophfink.com>

pkgname=python-av
_name=${pkgname#python-}
_upstream_name="PyAV"
pkgdesc="Pythonic bindings for FFmpeg"
url="https://pyav.basswood-io.com"

pkgver=12.1.0
pkgrel=2

arch=("x86_64" "i686")
license=("BSD-3-Clause")

depends=(
  "ffmpeg<=2:7"
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
  "python-av-bitstream-const.patch"  # https://github.com/PyAV-Org/PyAV/issues/1412#issuecomment-2141407404
)
b2sums=(
  "d83794a6d5f0137141ffcc1787b407285c98faa83598751171cf5013005d540adf65653d5b79d5ea7ce925523a1956b605339bc99f866d634c28e47794aa5782"
  "aa2e67f007494b424efb51534967c522ecd84eb66ae90428e8d5199fbb256e47a48930657d96fc31b11ec6863f8c9611ec6cb603d41ffb7f232abd9eda5ee067"
)

prepare() {
  cd "${srcdir}"/${_upstream_name}-${pkgver}
  patch --forward --strip=1 --input "${srcdir}/python-av-bitstream-const.patch"
}

build() {
  cd "${srcdir}"/${_upstream_name}-${pkgver}
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
