# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_bcname=BiocGenerics
_bcver=0.48.0
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
b2sums=("36194816c349b10aad7aa5f8acd558cc8365057b89a50868bdfd8068f55d02ca32eb6f103c723e605199a2050d013f79f909a74ec6104deef0457a7323edd329")

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
