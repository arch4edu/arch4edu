# Maintainer: peippo <christoph+aur@christophfink.com>

pkgname=python-av
_name=${pkgname#python-}
_upstream_name="PyAV"
pkgdesc="Pythonic bindings for FFmpeg"
url="https://pyav.basswood-io.com"

pkgver=14.2.0
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
  "python-build"
  "python-installer"
  "python-setuptools"
)
checkdepends=(
  "python-pytest"
)

source=(
  "$_name-$pkgver.tar.gz::https://github.com/${_upstream_name}-Org/${_upstream_name}/archive/refs/tags/v${pkgver}.tar.gz"
)
b2sums=("1905ce65621a7f68bb403a767f1c9e6cc382cf47dd5d31d770bfbc531798ce22df4bad7d93301938991611a00ba9391d04f6147c316ade5e109e3b9aafc6a3d0")

build() {
  cd "${srcdir}"/${_upstream_name}-${pkgver}
  python -m build --wheel --no-isolation
}

check() {
  cd "${srcdir}"/${_upstream_name}-${pkgver}

  local python_version=$(python -c 'import sys; print("".join(map(str, sys.version_info[:2])))')
  export PYTHONPATH="${srcdir}/${_upstream_name}-${pkgver}/build/lib.linux-${CARCH}-cpython-${python_version}"
  mv av _av  # so pytest does not attempt to import from source directory

  python -m pytest
}

package() {
  cd "${srcdir}/${_upstream_name}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/python-av/LICENSE"
}
