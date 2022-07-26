#Maintainer: sukanka <su975853527 AT gmail.com>
_pkgname=conting
_pkgver=1.7.9999
pkgname=r-${_pkgname,,}
pkgver=1.7.9999
pkgrel=1
pkgdesc="Bayesian Analysis of Contingency Tables"
arch=('any')
url="https://github.com/vandenman/${_pkgname}"
license=('GPL2')
depends=(r
  r-mvtnorm
	r-gtools
 	r-tseries
 	r-coda
)
makedepends=('git')
optdepends=()
source=("git+https://github.com/vandenman/${_pkgname}.git")
sha256sums=('SKIP')


build() {
  mkdir -p ${srcdir}/usr/lib/R/library
  R -e "install.packages('${srcdir}/${_pkgname}',\
     type='source', repos=NULL,lib='${srcdir}/usr/lib/R/library', INSTALL_opts='--no-multiarch --no-docs --no-test-load')"
}

package() {

  cp -a --no-preserve=ownership "${srcdir}/usr" "${pkgdir}"
}
