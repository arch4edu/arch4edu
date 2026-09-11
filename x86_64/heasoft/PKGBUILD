# Maintainer:  Yigit Dallilar <yigit.dallilar@gmail.com>

pkgname=heasoft
pkgver=6.37.1
pkgrel=1
# _mod should be '', '_no_xspec_modeldata' or '_plus_older_xspec_modeldata'
_mod=''
pkgdesc='NASA high energy astrophysics library'
depends=('inetutils' 'libxpm' 'libidn' 'ncurses' 'readline')
makedepends=('gcc14-fortran' 'glibc' 'perl' 'python-astropy' 'python-matplotlib' 'python-pip' 'python-scipy' 'python-setuptools')
optdepends=(
  "python-astropy: python binding"
  "python-numpy: python binding"
)
url="https://heasarc.gsfc.nasa.gov/docs/software/lheasoft/"
arch=('x86_64')
license=('NASA' 'GPL')
options=('!lto')
source=("https://heasarc.gsfc.nasa.gov/FTP/software/lheasoft/lheasoft${pkgver}/heasoft-${pkgver}src${_mod}.tar.gz")

# You could use below to get offical md5
# curl -s ${source}.md5  | awk '{print "md5sums=(", $1, ")"}'
md5sums=('b012d7b5ee7604ed712eca8d5d146f47')
sha256sums=('e9877b4933743ad2f53328b4034e25694431bbcb6016f50b0328bbfa84a25662')

install="$pkgname.install"

build() {
  cd "heasoft-$pkgver/BUILD_DIR"

  LDFLAGS='-lm' CC='gcc-14' CXX='g++-14' FC='gfortran-14' \
  CFLAGS="$CFLAGS -Wno-error=format-security" \
  ./configure --prefix="/opt/heasoft" --build="$CHOST"

  # parallel builds may fail
  make -j1
}

package(){
  local glibcver HEADAS hdhost components component

  glibcver=$(ldd --version | sed -n 's/ldd (GNU libc) //p')
  hdhost="${CHOST}-libc${glibcver}"
  HEADAS="/opt/heasoft/${hdhost}"
  components=$(sed -n 's/^HD_SELECTED[[:space:]]*=[[:space:]]*//p' "heasoft-$pkgver/BUILD_DIR/Makefile")

  set -a
  . "heasoft-$pkgver/heacore/BUILD_DIR/hmakerc"

  cd "heasoft-$pkgver/BUILD_DIR"

  for component in $components; do
    HD_PREFIX="/opt/heasoft/${component}"
    HD_EXEC_PFX="/opt/heasoft/${component}/${hdhost}"
    HD_TOP_PFX="/opt/heasoft"
    HD_TOP_EXEC_PFX="${HEADAS}"
  done
  set +a

  make -j1 DESTDIR="$pkgdir" HD_EXEC_PFX="$pkgdir/opt/heasoft/heacore/${hdhost}" install

  install -d "$pkgdir/etc/profile.d"
  cat > "$pkgdir/etc/profile.d/heasoft.sh" <<EOF
export HEADAS="${HEADAS}"
alias heainit='. "${HEADAS}/headas-init.sh"'
EOF
}
