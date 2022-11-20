# Maintainer: Pekka Ristola <pekkarr [at] protonmail [dot] com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com

_cranname=sass
_cranver=0.4.3
pkgname=r-${_cranname,,}
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc="Syntactically Awesome Style Sheets ('Sass')"
arch=(i686 x86_64)
url="https://cran.r-project.org/package=${_cranname}"
license=(MIT)
depends=(
    libsass
    r-fs
    r-rlang
    r-htmltools
    r-r6
    r-rappdirs
)
checkdepends=(r-curl r-testthat r-withr)
optdepends=(
    r-testthat
    r-knitr
    r-rmarkdown
    r-withr
    r-shiny
    r-curl
)
source=("https://cran.r-project.org/src/contrib/${_cranname}_${_cranver}.tar.gz"
        "CRAN-MIT-TEMPLATE::https://cran.r-project.org/web/licenses/MIT")
sha256sums=('94883c9e8219ca9609a704690c98d5dd9a0af52dfc9c98b0f7d8655b5a1365c0'
            'e76e4aad5d3d9d606db6f8c460311b6424ebadfce13f5322e9bae9d49cc6090b')

prepare() {
  # build against system libsass
  sed -e 's|PKG_LIBS = ./libsass/lib/libsass.a|PKG_LIBS = -lsass|' \
      -e '/PKG_CPPFLAGS = -I/d' \
      -e 's|$(SHLIB): libsass/lib/libsass.a|$(SHLIB):|' \
      -i "${_cranname}/src/Makevars"
}

build() {
  mkdir -p build
  R CMD INSTALL "${_cranname}" -l "${srcdir}/build"
}

check() {
  cd "${_cranname}/tests"
  R_LIBS="${srcdir}/build" NOT_CRAN=true Rscript --vanilla testthat.R
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"

  cp -a --no-preserve=ownership "build/${_cranname}" "${pkgdir}/usr/lib/R/library"

  install -Dm644 CRAN-MIT-TEMPLATE "${pkgdir}/usr/share/licenses/${pkgname}/MIT"
  install -Dm644 "${_cranname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
