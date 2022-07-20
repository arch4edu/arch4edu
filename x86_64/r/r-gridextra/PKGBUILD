# Maintainer: portaloffreedom

_cranname=gridExtra
_cranver=2.3
pkgname=r-gridextra
pkgver=${_cranver}
pkgrel=1
pkgdesc='Provides a number of user-level functions to work with "grid" graphics, notably to arrange multiple grid-based plots on a page, and draw tables.'
url="http://cran.r-project.org/web/packages/${_cranname}/index.html"
arch=('i686' 'x86_64')
license=('GPL3')
depends=('r>=3.0.0' 'r-gtable')
provides=("r-cran-gridextra")
conflicts=("r-cran-gridextra")
replaces=("r-cran-gridextra")
source=("http://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
md5sums=('01e0ea88610756a0fd3b260e83c9bd43')

package() {
    mkdir -p ${pkgdir}/usr/lib/R/library
    cd ${srcdir}
    R CMD INSTALL ${_cranname} -l ${pkgdir}/usr/lib/R/library
}
