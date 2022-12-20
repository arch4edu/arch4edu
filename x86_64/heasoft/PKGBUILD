# Maintainer:  Yigit Dallilar <yigit.dallilar@gmail.com>

pkgname=heasoft
pkgver=6.31.1
pkgrel=1
# _mod should be '', '_no_xspec_modeldata' or '_plus_older_xspec_modeldata'
_mod=''
pkgdesc='NASA high energy astrophysics library'
depends=('libxpm' 'libidn' 'ncurses' 'readline')
makedepends=('glibc' 'gcc-fortran' 'inetutils' 'perl' 'python-astropy' 'python-pip' 'python-scipy' 'python-setuptools')
optdepends=(
  "python-astropy: python binding"
  "python-numpy: python binding"
)
url="https://heasarc.gsfc.nasa.gov/docs/software/lheasoft/"
arch=('x86_64')
license=('NASA' 'GPL')
source=("https://heasarc.gsfc.nasa.gov/FTP/software/lheasoft/lheasoft${pkgver}/heasoft-${pkgver}src${_mod}.tar.gz")

# You could use below to get offical md5
# curl -s ${source}.md5  | awk '{print "md5sums=(", $1, ")"}'
md5sums=('06d374d96b0f4ee707b2d32baea3b5a8')

install="$pkgname.install"

build() {
  cd "heasoft-$pkgver/BUILD_DIR"

  LDFLAGS='-lm' \
  CFLAGS="$CFLAGS -Wno-error=format-security" \
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
