# Maintainer:  Yigit Dallilar <yigit.dallilar@gmail.com>

pkgname=heasoft
pkgver=6.27.1
pkgrel=1
# _mod should be '', '_no_xspec_modeldata' or '_plus_older_xspec_modeldata'
_mod='_no_xspec_modeldata'
pkgdesc="NASA high energy astrophysics library"
makedepends=("glibc" "gcc-fortran" "perl" "python-numpy")
depends=("ncurses" "readline" "libxpm" "libidn")
url="https://heasarc.gsfc.nasa.gov/docs/software/lheasoft/"
arch=('x86_64')
license=('NASA' 'GPL')
source=("https://heasarc.gsfc.nasa.gov/FTP/software/lheasoft/lheasoft${pkgver}/${pkgname}-${pkgver}src${_mod}.tar.gz")
sha256sums=('6186f518a68397a10d3bbd0ecb624e583c213a372b2d9db01f41d8e0ca874c9a')
install="${pkgname}.install"

build() {
  cd "$srcdir/${pkgname}-${pkgver}/BUILD_DIR" || return

  ./configure --prefix="/opt/${pkgname}" --build="${CHOST}"

  # parallel builds may fail
  make -j1
}

package(){
  local glibcver HEADAS

  cd "$srcdir/${pkgname}-${pkgver}/BUILD_DIR" || return

  make -j1 DESTDIR="$pkgdir" install

  glibcver=$(ldd --version | sed -n 's/ldd (GNU libc) //p')
  HEADAS="/opt/${pkgname}/${CHOST}-libc${glibcver}"

  install -d "$pkgdir/etc/profile.d"
  cat > "$pkgdir/etc/profile.d/heasoft.sh" <<EOF
export HEADAS="${HEADAS}"
alias heainit='. "${HEADAS}/headas-init.sh"'
EOF
}
