# Maintainer: Benoit Favre <benoit.favre@lif.univ-mrs.fr>
pkgname="mitlm"
pkgver=0.4.2
pkgrel=1
pkgdesc="Tools for efficient iterative estimation of statistical n-gram language models"
arch=('i686' 'x86_64')
url="https://github.com/mitlm/mitlm"
license=('MIT')
depends=()
makedepends=('gcc' 'gcc-fortran')
source=("https://github.com/mitlm/mitlm/releases/download/v${pkgver}/mitlm-${pkgver}.tar.xz")
sha1sums=(07d82c1b6cf238e62aae1f37d8f5891c04909851)

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
