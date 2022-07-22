# Maintainer: dhn <neilson+aur@sent.com>

_pkgname=httr
pkgname=r-$_pkgname
pkgver=1.4.3
pkgrel=1
pkgdesc='Useful tools for working with HTTP organised by HTTP verbs (GET(), POST(), etc). Configuration functions make it easy to control additional request components'
arch=('any')
url="https://cran.r-project.org/web/packages/$_pkgname/"
license=('GPL')
depends=('r' 'r-curl' 'r-jsonlite' 'r-mime' 'r-openssl' 'r-r6')
makedepends=('r-testthat')
optdepends=('r-covr' 'r-httpuv' 'r-jpeg' 'r-knitr' 'r-png' 'r-readr' 'r-xml2' 'r-rmarkdown')
source=("https://cran.r-project.org/src/contrib/${_pkgname}_$pkgver.tar.gz")
sha512sums=('5cfda5677c1602b37ef1a7161db90b0d1ac2bffb0c34a7b80b14e3ec9a426b6b31cb7ec780e90df202db61a4934a2ce2049d24b39838de71d13290c375210efb')

build(){
    R CMD INSTALL ${_pkgname}_$pkgver.tar.gz -l "$srcdir"
}

package() {
    install -dm 755 "$pkgdir"/usr/lib/R/library
    cp -a --no-preserve=ownership httr "$pkgdir"/usr/lib/R/library
}
