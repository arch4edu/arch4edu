# Maintainer: ikyope at outlook dot com
# Contributor: peippo <christoph+aur@christophfink.com>

_pkgname=classInt
_pkgver=0.4-11
pkgname=r-${_pkgname,,}
pkgver=${_pkgver//[:-]/.}
pkgrel=1
pkgdesc="Choose Univariate Class Intervals"
arch=("x86_64")
url="https://CRAN.R-project.org/package=${_pkgname}"
license=("GPL-2.0-only OR GPL-3.0-only")
depends=(
    "r>=2.2"
    "r-grdevices"
    "r-stats"
    "r-graphics"
    "r-e1071"
    "r-class"
    "r-kernsmooth"
)
optdepends=(
    "r-spdata>=0.2.6.2"
    "r-units"
    "r-knitr"
    "r-rmarkdown"
    "r-tinytest"
)
makedepends=("gcc-fortran")
source=("https://cran.r-project.org/src/contrib/${_pkgname}_${_pkgver}.tar.gz")
b2sums=("fb63690bd9184a2d08140d485c9d522effec7b571c39cf5ee3d98f60878c6bca3e32e85d65df7f7a30d3d074e3a616361981a673ec29a89883f74912dd2496e8")

build() {
    R CMD INSTALL ${_pkgname}_${_pkgver}.tar.gz -l "${srcdir}"
}

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${_pkgname}" "${pkgdir}/usr/lib/R/library"
}
