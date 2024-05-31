#Maintainer: sukanka <su975853527 AT gmail.com>
_pkgname=flexplot
_pkgver=0.21.1
pkgname=r-${_pkgname,,}
pkgver=0.21.1
pkgrel=1
pkgdesc="Graphically Based Data Analysis"
arch=('x86_64')
url="https://github.com/dustinfife/${_pkgname}"
license=('GPL2')
depends=(r
  	r-cowplot
	r-tibble
	r-withr
	r-dplyr
	r-magrittr
	r-forcats
	r-purrr
	r-plyr
	r-r6
	r-ggplot2
	r-patchwork
	r-ggsci
	r-lme4
	r-party
	r-rlang
)
makedepends=(r-jmvcore git)
optdepends=(
  	r-jmvcore
	r-vdiffr
	r-knitr
	r-testthat
	r-randomforest
	r-markdown
	r-papaja
	r-tidyverse
)
source=("git+https://github.com/dustinfife/${_pkgname}.git")
sha256sums=('SKIP')


build() {
  mkdir -p ${srcdir}/usr/lib/R/library
  R -e "install.packages('${srcdir}/${_pkgname}',\
     type='source', repos=NULL,lib='${srcdir}/usr/lib/R/library', INSTALL_opts='--no-multiarch --no-docs --no-test-load')"
}

package() {

  cp -a --no-preserve=ownership "${srcdir}/usr" "${pkgdir}"
}
