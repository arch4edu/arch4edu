# Maintainer: John Boyd <boyd8444@sdf.org>

pkgname=librdata-git
pkgver=r125.33bd276
pkgrel=2
pkgdesc="RData file parser library"
arch=('x86_64')
url="https://github.com/WizardMac/librdata"
license=('MIT')
depends=('gcc-libs')
makedepends=('git' 'autoconf' 'automake' 'libtool' 'gettext')
source=("git+https://github.com/WizardMac/librdata.git")
sha256sums=('SKIP')

pkgver() {
  cd "${srcdir}/librdata"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
  cd "${srcdir}/librdata"
  if [[ ! -f configure ]]; then
    autoreconf -fi
  fi
}

build() {
  cd "${srcdir}/librdata"
  ./configure --prefix=/usr
  make
}

check() {
  cd "${srcdir}/librdata"
  make check || true
}

package() {
  cd "${srcdir}/librdata"
  make DESTDIR="${pkgdir}" install
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

