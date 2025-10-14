# Maintainer: peippo <christoph+aur@christophfink.com>

pkgname=python-av
_name=${pkgname#python-}
_upstream_name="PyAV"
pkgdesc="Pythonic bindings for FFmpeg"
url="https://pyav.basswood-io.com"

pkgver=16.0.1
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

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/${_upstream_name}-Org/${_upstream_name}/archive/refs/tags/v${pkgver}.tar.gz")
b2sums=("f134286c68f55689f51e0bf2baec3d675e9d0f2af460265294c2bdf868edefac57cecf947b022cbb78774d45b5d5aa8e3a036ade77cdbb7df91105b71c52025c")

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
