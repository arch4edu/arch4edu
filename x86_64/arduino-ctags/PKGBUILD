# Maintainer: Andreas Baumann <mail@andreasbauman.cc>
# Contributor: NicoHood <archlinux {cat} nicohood {dog} de>
# PGP ID: 97312D5EB9D7AE7D0BD4307351DAE9B7C1AE9161

pkgname=arduino-ctags
_pkgname=ctags
pkgver=5.8_arduino11
_pkgver=5.8-arduino11
pkgrel=5
pkgdesc="A mix of ctags and anjuta-tags for the perfect C++ ctags"
arch=('x86_64')
license=('GPL')
depends=('glibc')
url="https://github.com/arduino/ctags"
source=("${pkgname}-${_pkgver}.tar.gz::https://github.com/arduino/${_pkgname}/archive/${_pkgver}.tar.gz"
        "CVE-2014-7204.patch"
        "ctags-5.8-arduino11-unused.patch")
sha512sums=('6375077dfd983e98862773dfe6213bd41cd17d99260e39e97f99eff7d7f363f6d6a61582994382c69f0e3dfa7da88c1640a5bc037adbcc526e07f86dbd4f3646'
            '212ec5d3daec5ffadc3ffe60406fc1f6b76356f2c56f99e999f8bf0646891c0067144e5de8ccbbe9391a803cd4005fe94a5973911274928dd7c1414d1ec68477'
            '7cdae823f9230217a009b5f5b4399a4be7206dcd2571e7fb4623354660c794bdce359074472a9ef4a79f744956c997675af209f2fc79ae77c5f62599d57c29fe')
validpgpkeys=('326567C1C6B288DF32CB061A95FA6F43E21188C4') # Arduino Packages <support@arduino.cc>

prepare() {
  cd "${srcdir}/${_pkgname}-${_pkgver}"

  patch -Np1 <../CVE-2014-7204.patch
  patch -Np1 <../ctags-5.8-arduino11-unused.patch

  sed -i 's/^CTAGS_PROG =.*/CTAGS_PROG = arduino-ctags/' Makefile.in
  sed -i 's/^MANPAGE =.*/MANPAGE = arduino-ctags.1/' Makefile.in
}

build() {
  cd "${srcdir}/${_pkgname}-${_pkgver}"

  ./configure --prefix=/usr \
              --disable-external-sort
  make
}

package() {
  cd "${srcdir}/${_pkgname}-${_pkgver}"

  make prefix="${pkgdir}"/usr install
}
