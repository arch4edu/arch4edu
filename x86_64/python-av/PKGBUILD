# Maintainer: peippo <christoph+aur@christophfink.com>

pkgname=python-av
_name=${pkgname#python-}
_upstream_name="PyAV"
pkgdesc="Pythonic bindings for FFmpeg"
url="https://pyav.basswood-io.com"

pkgver=15.1.0
pkgrel=2

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
b2sums=("eb8fe7e2435a74b58403bd220629a4ab09563d9136b5c00363793ae788bb11410f88fded79d506cc33bfe76d99818c1a8ea6bba8691b8153adbc14694ed74729")


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
