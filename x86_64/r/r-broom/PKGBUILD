# Maintainer: peippo <christoph+aur@christophfink.com>
# Maintainer: Alad Wenter <alad at archlinux dot org>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: frichtlm <frichtlm@gmail.com>

_cranname=broom
_cranver=1.0.4
pkgname=r-${_cranname,,}
pkgdesc="Convert Statistical Objects into Tidy Tibbles"
url="https://cran.r-project.org/package=${_cranname}"
license=("MIT")
pkgver=${_cranver//[:-]/.}
pkgrel=1

arch=("any")
depends=(
    "r>=3.5"
    "r-backports"
    "r-dplyr>=1.0.0"
    "r-ellipsis"
    "r-generics>=0.0.2"
    "r-glue"
    "r-lifecycle"
    "r-purrr"
    "r-rlang"
    "r-stringr"
    "r-tibble>=3.0.0"
    "r-tidyr>=1.0.0"
)
optdepends=(
    "r-aer"
    "r-auc"
    "r-bbmle"
    "r-betareg"
    "r-biglm"
    "r-bingroup"
    "r-boot"
    "r-btergm>=1.10.6"
    "r-car"
    "r-cardata"
    "r-caret"
    "r-cluster"
    "r-cmprsk"
    "r-coda"
    "r-covr"
    "r-drc"
    "r-e1071"
    "r-emmeans"
    "r-epir"
    "r-ergm>=3.10.4"
    "r-fixest>=0.9.0"
    "r-gam>=1.15"
    "r-gee"
    "r-geepack"
    "r-ggplot2"
    "r-glmnet"
    "r-glmnetutils"
    "r-gmm"
    "r-hmisc"
    "r-irlba"
    "r-interp"
    "r-joinerml"
    "r-kendall"
    "r-knitr"
    "r-ks"
    "r-lahman"
    "r-lavaan"
    "r-leaps"
    "r-lfe"
    "r-lm.beta"
    "r-lme4"
    "r-lmodel2"
    "r-lmtest>=0.9.38"
    "r-lsmeans"
    "r-maps"
    "r-maptools"
    "r-margins"
    "r-mass"
    "r-mclust"
    "r-mediation"
    "r-metafor"
    "r-mfx"
    "r-mgcv"
    "r-mlogit"
    "r-modeldata"
    "r-modeltests"
    "r-muhaz"
    "r-multcomp"
    "r-network"
    "r-nnet"
    "r-orcutt>=2.2"
    "r-ordinal"
    "r-plm"
    "r-polca"
    "r-psych"
    "r-quantreg"
    "r-rgeos"
    "r-rmarkdown"
    "r-robust"
    "r-robustbase"
    "r-rsample"
    "r-sandwich"
    "r-sp"
    "r-spdep>=1.1"
    "r-spatialreg"
    "r-speedglm"
    "r-spelling"
    "r-survey"
    "r-survival"
    "r-systemfit"
    "r-tseries"
    "r-vars"
    "r-zoo"
)

source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz")
b2sums=('05fa38c748a8f6eb37664773fa26e6a5bc5b8caebfe8336b5fc43fb633afacbe91db037b5bd4244def546645c1f5a52d290e1c5b6e72f2728691bbf93313c2c2')

build() {
    mkdir -p "${srcdir}/build/"
    R CMD INSTALL ${_cranname}_${_cranver}.tar.gz -l "${srcdir}/build/"
}

package() {
    install -dm0755 "${pkgdir}/usr/lib/R/library"
    cp -a --no-preserve=ownership "${srcdir}/build/${_cranname}" "${pkgdir}/usr/lib/R/library"
    if [[ -f "${_cranname}/LICENSE" ]]; then
        install -Dm0644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    fi
}
