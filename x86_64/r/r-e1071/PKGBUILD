# Maintainer: Ward Segers <w@rdsegers.be>
# Maintainer: Alex Hirzel <alex@hirzel.us>

# Contributor: Alex Branham <alex.branham@gmail.com>
# Contributor: Robert Greener <me@r0bert.dev>

_cranver=1.7-12
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
sha512sums=('04fb95fdec9f1f2c6224db79e678beb6bf74c8f66fd3a8400390307ba3de8024b598eab61bf678044b1543997716893ee0fd720bbebd6b4749caabf3ebb158ee')

build(){
    R CMD INSTALL e1071_"$_cranver".tar.gz -l "$srcdir"
}

package() {
    install -dm0755 "$pkgdir"/usr/lib/R/library
    cp -a --no-preserve=ownership e1071 "$pkgdir"/usr/lib/R/library
}

