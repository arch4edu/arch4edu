# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_bcname=BiocParallel
_bcver=1.36.0
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
    "r-codetools"
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
b2sums=('40c18ff52c75ff0626b3d6a7ed39a495c907b76d10833a7f4b84c3f6d0a0a7eee507741c609fd9be8d5c3e4c6dc92008a96c90184884840786462b8f2e60bb49')

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
