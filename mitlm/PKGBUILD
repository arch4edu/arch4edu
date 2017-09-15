# Maintainer: Benoit Favre <benoit.favre@lif.univ-mrs.fr>
pkgname="mitlm"
pkgver=0.4.1
pkgrel=4
pkgdesc="Tools for efficient iterative estimation of statistical n-gram language models"
arch=('i686' 'x86_64')
url="https://code.google.com/p/mitlm/"
license=('MIT')
depends=()
makedepends=('gcc' 'gcc-fortran')
source=("https://github.com/mitlm/mitlm/releases/download/v${pkgver}/mitlm_${pkgver}.tar.gz")
md5sums=(f4b07068df48445bfc21800086a549c2)

build() {
    cd "$srcdir/$pkgname-$pkgver"
    ./configure --prefix=/usr
    make
}

check() {
    cd "$srcdir/$pkgname-$pkgver"
    make -k check
}

package() {
    cd "$srcdir/$pkgname-$pkgver"
    make DESTDIR="$pkgdir/" install
}
