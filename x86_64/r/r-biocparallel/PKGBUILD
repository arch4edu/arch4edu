# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_bcname=BiocParallel
_bcver=1.34.2
pkgname=r-${_bcname,,}
pkgdesc="Bioconductor facilities for parallel evaluation"
url="https://bioconductor.org/packages/release/bioc/html/${_bcname}.html"
pkgver=${_bcver//[:-]/.}
pkgrel=1

arch=("i686" "x86_64")
license=("GPL2" "GPL3")

depends=(
    "r>=3.5.0"
    "r-bh"
    "r-cpp11"
    "r-futile.logger"
    "r-snow"
)
optdepends=(
    "r-batchtools"
    "r-bbmisc"
    "r-biocgenerics"
    "r-biocstyle"
    "r-data.table"
    "r-doparallel"
    "r-foreach"
    "r-genomicalignments"
    "r-genomicranges"
    "r-knitr"
    "r-rnaseqdata.hnrnpc.bam.chr14"
    "r-rsamtools"
    "r-runit"
    "r-shortread"
    "r-txdb.hsapiens.ucsc.hg19.knowngene"
    "r-variantannotation"
)

source=("https://bioconductor.org/packages/release/bioc/src/contrib/${_bcname}_${_bcver}.tar.gz")
b2sums=("752b3c1173b1c71ae6f2644b5836640ab30aecba99585629452e9b4fc9a921dffdd299046ca335f7117c177b3ff782d69388dc4ee8117d68f55e2f5fdfc562b2")

build() {
  R CMD INSTALL ${_bcname}_${_bcver}.tar.gz -l "${srcdir}"
}

package() {
  install -dm0755 "${pkgdir}/usr/lib/R/library"
  cp -a --no-preserve=ownership "${_bcname}" "${pkgdir}/usr/lib/R/library"

  if [[ -f "${_bcname}/LICENSE" ]]; then
    install -Dm0644 "${_bcname}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  fi

}
