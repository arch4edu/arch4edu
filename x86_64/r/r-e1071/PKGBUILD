# Maintainer: Ward Segers <w@rdsegers.be>
# Maintainer: Alex Hirzel <alex@hirzel.us>

# Contributor: Alex Branham <alex.branham@gmail.com>
# Contributor: Robert Greener <me@r0bert.dev>

_cranver=1.7-14
pkgname=r-e1071
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc='Functions for latent class analysis, short time Fourier transform, fuzzy clustering, support vector machines, shortest path computation, bagged clustering, naive Bayes classifier, ...'
arch=('x86_64')
url='https://cran.r-project.org/web/packages/e1071'
license=('GPL')
depends=('r' 'r-proxy')
replaces=('r-cran-e1071')
source=("https://cran.r-project.org/src/contrib/e1071_"$_cranver".tar.gz")
sha512sums=('24919f1de63439f0533cc6d3f65289d47fee0e3ca63b29ea2531e087cb5b8bd27d4b8405902e69cac9ffcec6d17fe10e9635c66423cbdfeebce7c5579bb52728')

build(){
    R CMD INSTALL e1071_"$_cranver".tar.gz -l "$srcdir"
}

package() {
    install -dm0755 "$pkgdir"/usr/lib/R/library
    cp -a --no-preserve=ownership e1071 "$pkgdir"/usr/lib/R/library
}

