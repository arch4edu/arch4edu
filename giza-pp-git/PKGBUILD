# Maintainer: Panos Kanavos <panoskanavos@gmail.coml>
_pkgname=giza-pp
pkgname=giza-pp-git
pkgver=r21.228a39b
pkgrel=1
pkgdesc='A statistical machine translation toolkit used to train word alignment models'
arch=('i686' 'x86_64')
url='https://github.com/moses-smt/giza-pp'
license=('GPL2')
makedepends=(gcc make git)
depends=(tcsh)
conflicts=(mgiza-git mgiza)
provides=(giza)
install=
source=("git+https://github.com/moses-smt/$_pkgname.git")
md5sums=("SKIP")

pkgver() {
    cd "$srcdir/$_pkgname"
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  cd "$srcdir/$_pkgname"
  make
}

package() {
  cd "$srcdir/$_pkgname"
  install_dir="$pkgdir/opt/$_pkgname/bin"
  mkdir -p $install_dir
  install -D "GIZA++-v2/GIZA++" "$install_dir"
  install -D "GIZA++-v2/plain2snt.out" "$install_dir"
  install -D "GIZA++-v2/snt2cooc.out" "$install_dir"
  install -D "GIZA++-v2/trainGIZA++.sh" "$install_dir"
  install -D "mkcls-v2/mkcls" "$install_dir"
}
