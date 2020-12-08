# Maintainer:  Yigit Dallilar <yigit.dallilar@gmail.com>

pkgname=heasoft
pkgver=6.28
pkgrel=1
# _mod should be '', '_no_xspec_modeldata' or '_plus_older_xspec_modeldata'
_mod=''
pkgdesc='NASA high energy astrophysics library'
makedepends=("glibc" "gcc-fortran" "perl" "python-numpy")
depends=("ncurses" "readline" "libxpm" "libidn")
optdepends=("python-numpy: python binding")
url="https://heasarc.gsfc.nasa.gov/docs/software/lheasoft/"
arch=('x86_64')
license=('NASA' 'GPL')
source=("https://heasarc.gsfc.nasa.gov/FTP/software/lheasoft/lheasoft${pkgver}/heasoft-${pkgver}src${_mod}.tar.gz")

# You could use below to get offical md5
# curl -s ${source}.md5  | awk '{print "md5sums=(", $1, ")"}'
md5sums=( a8ab35fd7da9166b4cd31e7365826251 )

install="$pkgname.install"

build() {
  cd "heasoft-$pkgver/BUILD_DIR"

  ./configure --prefix="/opt/heasoft" --build="$CHOST"

  # parallel builds may fail
  make -j1
}

package(){
  local glibcver HEADAS

  cd "heasoft-$pkgver/BUILD_DIR"

  make -j1 DESTDIR="$pkgdir" install

  glibcver=$(ldd --version | sed -n 's/ldd (GNU libc) //p')
  HEADAS="/opt/heasoft/${CHOST}-libc${glibcver}"

  install -d "$pkgdir/etc/profile.d"
  cat > "$pkgdir/etc/profile.d/heasoft.sh" <<EOF
export HEADAS="${HEADAS}"
alias heainit='. "${HEADAS}/headas-init.sh"'
EOF
}
