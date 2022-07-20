# Maintainer: Ward Segers <w@rdsegers.be>

_cranver=0.4-27
pkgname=r-proxy
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc='An extensible framework for auto- and cross-proximities'
arch=('x86_64')
url='https://cran.r-project.org/web/packages/proxy'
license=('GPL')
depends=('r')
source=("https://cran.r-project.org/src/contrib/proxy_"$_cranver".tar.gz")
sha512sums=('32c5245279d8dba8bef33d6a3bcd7a88f8ebf20773ae8929aeac40a37d763a3fce7d4307719b57bc0461e1d144a0cbb035ecd2bd1a68de9126bff5956815b4c2')

build(){
    R CMD INSTALL proxy_"$_cranver".tar.gz -l "$srcdir"
}

package() {
    install -dm0755 "$pkgdir"/usr/lib/R/library
    cp -a --no-preserve=ownership proxy "$pkgdir"/usr/lib/R/library
}


