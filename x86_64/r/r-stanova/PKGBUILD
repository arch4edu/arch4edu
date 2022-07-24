#Maintainer: sukanka <su975853527 AT gmail.com>
_pkgname=stanova
_pkgver=0.3-0
pkgname=r-${_pkgname,,}
pkgver=0.3.0
pkgrel=1
pkgdesc="Bayesian Models with Categorical Variables"
arch=('x86_64')
url="https://github.com/bayesstuff/${_pkgname}"
license=('LGPL3')
depends=(r
 	  r-lme4
    r-coda
    r-rstan
    r-emmeans
)
makedepends=(git)
optdepends=(
    r-testthat
    r-rstanarm
    r-brms
    r-memss
    r-afex
    r-glmmtmb
    r-bayesplot
    r-tibble
    r-tidybayes
    r-tidyverse
)
source=("git+https://github.com/bayesstuff/${_pkgname}.git")
sha256sums=('SKIP')


build() {
  mkdir -p ${srcdir}/usr/lib/R/library
  R -e "install.packages('${srcdir}/${_pkgname}',\
     type='source', repos=NULL,lib='${srcdir}/usr/lib/R/library', INSTALL_opts='--no-multiarch --no-docs --no-test-load')"
}

package() {
  cp -a --no-preserve=ownership "${srcdir}/usr" "${pkgdir}"
}
