# Maintainer: peippo <christoph+aur@christophfink.com>

pkgname=python-av
_name=${pkgname#python-}
_upstream_name="PyAV"
pkgdesc="Pythonic bindings for FFmpeg"
url="https://pyav.basswood-io.com"

pkgver=15.0.0
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
  "${pkgname}-${pkgver}.tar.gz::https://github.com/${_upstream_name}-Org/${_upstream_name}/archive/refs/tags/v${pkgver}.tar.gz"
  "venv.patch"
)
b2sums=(
    "21a13a9d8b742f340ad763fb8bd27274727f6122d7e524a2e4fdb2ed61e31809b926a161ca73fb36b8d6564780dd2c34d21c3ec383c2c1c20486717702b587b5"
    "e4b3ef842fad3125cda283ea4cb49aa0687f8ca8b516016dbdc978551793d8320e0ebe31d14ac5f46cb5eaca8e583ca19aa5304c2671b36c3a31872f495301ed"
)

prepare() {
  cd "${srcdir}"/${_upstream_name}-${pkgver}
  patch --forward --strip=1 --input "${srcdir}/venv.patch"
    
}

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
