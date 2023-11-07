# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_bcname=BiocGenerics
_bcver=0.48.1
pkgname=r-${_bcname,,}
pkgver=${_bcver//[:-]/.}
pkgrel=1
pkgdesc="S4 generic functions used in Bioconductor"
arch=(any)
url="https://bioconductor.org/packages/release/bioc/html/${_bcname}.html"
license=("Artistic2.0")

depends=("r>=4.0.0")
optdepends=(
    "r-biobase"
    "r-s4vectors"
    "r-iranges"
    "r-genomicranges"
    "r-delayedarray"
    "r-biostrings"
    "r-rsamtools"
    "r-annotationdbi"
    "r-affy"
    "r-affyplm"
    "r-deseq2"
    "r-flowclust"
    "r-msnbase"
    "r-annotate"
    "r-runit"
)
source=("https://bioconductor.org/packages/release/bioc/src/contrib/${_bcname}_${_bcver}.tar.gz")
b2sums=("e69382abdf5e3699c49f0538b3345d2dd3a88c7d8485bc638603a96ed0be59cc403c8049fcae3cecac3793bacb8e7023da46bd48b8a5ccb509c7e84b59717837")

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
