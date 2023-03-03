# Maintainer: dhn <neilson+aur@sent.com>
# Co-maintainer: alhirzel

_pkgname=httr
pkgname=r-$_pkgname
pkgver=1.4.5
pkgrel=1
pkgdesc='Useful tools for working with HTTP organised by HTTP verbs (GET(), POST(), etc). Configuration functions make it easy to control additional request components'
arch=('any')
url="https://cran.r-project.org/web/packages/$_pkgname/"
license=('GPL')
depends=('r' 'r-curl' 'r-jsonlite' 'r-mime' 'r-openssl' 'r-r6')
makedepends=('r-testthat')
optdepends=('r-covr' 'r-httpuv' 'r-jpeg' 'r-knitr' 'r-png' 'r-readr' 'r-xml2' 'r-rmarkdown')
source=("https://cran.r-project.org/src/contrib/${_pkgname}_$pkgver.tar.gz")
sha512sums=('e836e9b08edbde1fe05cc25417be1bcaecfaf1ce20f8858b49c22a5c449b8a658511eeb50f10d84881d95fec44d68423305401dfeb7d8ab2fa35c3e1f840a071')

build(){
    R CMD INSTALL ${_pkgname}_$pkgver.tar.gz -l "$srcdir"
}

package() {
    install -dm 755 "$pkgdir"/usr/lib/R/library
    cp -a --no-preserve=ownership httr "$pkgdir"/usr/lib/R/library
}
