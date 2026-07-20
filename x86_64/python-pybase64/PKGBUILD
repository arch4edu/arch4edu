# Maintainer: envolution
# Contributor: irmluity <45vw4yz8g@mozmail.com>
# shellcheck shell=bash disable=SC2034,SC2154

pkgname=python-pybase64
_pkgname=pybase64
pkgver=1.4.2
pkgrel=1
pkgdesc="Fast Base64 encoding/decoding in Python"
arch=(x86_64)
url="https://github.com/mayeut/pybase64"
license=('BSD-2-Clause')
depends=(
  glibc 
  python 
  python-typing_extensions
)
makedepends=(
  git 
  cmake
  python-build
  python-installer
  python-setuptools
  python-wheel
)
provides=(${_pkgname})
source=(
  "${_pkgname}-${pkgver}::git+https://github.com/mayeut/pybase64.git#tag=v${pkgver}"
  git+https://github.com/aklomp/base64.git
)
sha256sums=('f18825091e33a686684d639789d571788bae74ee2871519c8d303991609f093e'
            'SKIP')

prepare() {
  cd "${_pkgname}-${pkgver}"
  git submodule init
  git config submodule.base64.url "$srcdir/base64"
  git -c protocol.file.allow=always submodule update
}
build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t ${pkgdir}/usr/share/licenses/python-${_pkgname}/
}

# vim:set ts=2 sw=2 et:
