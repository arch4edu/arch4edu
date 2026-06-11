# Maintainer: Serene-Arc <https://aur.archlinux.org/account/serene-arc>

_cranname=keyring
_cranver=1.4.1
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Platform independent 'API' to access the operating system's credential store."
arch=('any')
url="https://cran.r-project.org/package=${_cranname}"
license=('MIT')
depends=(
    r
    r-askpass
    r-filelock
    r-utils
    r-tools
    r-yaml
)
makedepends=(gcc)
optdepends=(
    r-callr
    r-covr
    r-openssl
    r-testthat
    r-withr
    )
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
sha256sums=('fba2451fc8cd4494fc0025264b67be49a58e020e01c65e5d5d2c43f84f53ce84')

build() {
  R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "${_cranname}" "${pkgdir}/usr/lib/R/library"
}
