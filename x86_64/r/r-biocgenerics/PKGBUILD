# Maintainer: peippo <christoph+aur@christophfink.com>
# Contributor: Viktor Drobot (aka dviktor) linux776 [at] gmail [dot] com
# Contributor: Grey Christoforo <first name at last name dot net>

_bcname=BiocGenerics
_bcver=0.46.0
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
b2sums=("8f1a05c67bbd03d2110e7b5d485fc42d9cccc8d47c79bed6cdee787b3a11ff1ed17f37f5468b1900c1a651536476a2976f6a359e38f26e308a8be9510f2c3bef")

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
