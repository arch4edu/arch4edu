# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Michel Zou <xantares09@hotmail.com>
_base=scipy
pkgname=pypy3-${_base}
pkgver=1.16.2
pkgrel=1
pkgdesc="Fundamental algorithms for scientific computing in Python"
arch=(x86_64)
url="https://${_base}.org"
license=(BSD-3-Clause)
depends=(blas gcc-libs glibc lapack pypy3-numpy) # pypy3-platformdirs pypy3-pooch
makedepends=(boost pypy3-cython gcc-fortran git meson-pypy3
  pypy3-pybind11 pypy3-build pypy3-installer pypy3-pythran)
source=(${_base}-${pkgver}::git+https://github.com/${_base}/${_base}.git?signed#tag=v${pkgver}
  git+https://github.com/data-apis/array-api-compat
  git+https://github.com/boostorg/math
  git+https://github.com/cobyqa/cobyqa
  git+https://github.com/${_base}/pocketfft
  git+https://github.com/${_base}/unuran)
validpgpkeys=('AD0C5067D1DECED72F6245670196A9293365B112') # Tyler Reddy <tyler.je.reddy@gmail.com>
sha512sums=('55403a6eb24369c4be958b3300344d1d5d7490797c44e837561cdc000f55653b7d787fe40d6d920570b17c4337aea746c5eed07648ed5fd9d2fc0261a380a9f8'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')
options=(!lto)

prepare() {
  cd ${_base}-${pkgver}
  git submodule init
  git submodule set-url scipy/_lib/array_api_compat "${srcdir}"/array-api-compat
  git submodule set-url subprojects/boost_math/math "${srcdir}"/math
  git submodule set-url scipy/_lib/cobyqa "${srcdir}"/cobyqa
  git submodule set-url scipy/_lib/pocketfft "${srcdir}"/pocketfft
  git submodule set-url scipy/_lib/unuran "${srcdir}"/unuran
  git -c protocol.file.allow=always submodule update
}

build() {
  cd ${_base}-${pkgver}
  PATH=/opt/pypy3/bin:${PATH} pypy3 -m build --wheel --skip-dependency-check --no-isolation \
    -C setup-args=-Dblas=blas \
    -C setup-args=-Dlapack=lapack
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE.txt -t "$pkgdir"/usr/share/licenses/pypy3-$pkgname
}
