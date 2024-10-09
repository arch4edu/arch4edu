# Maintainer: Ward Segers <w@rdsegers.be>
# Maintainer: Alex Hirzel <alex@hirzel.us>

# Contributor: Alex Branham <alex.branham@gmail.com>
# Contributor: Robert Greener <me@r0bert.dev>

_cranver=1.7-16
pkgname=r-e1071
pkgver=${_cranver//[:-]/.}
pkgrel=2
pkgdesc='Functions for latent class analysis, short time Fourier transform, fuzzy clustering, support vector machines, shortest path computation, bagged clustering, naive Bayes classifier, ...'
arch=('x86_64')
url='https://cran.r-project.org/web/packages/e1071'
license=('GPL-2.0-or-later')
depends=('r' 'r-proxy')
replaces=('r-cran-e1071')
source=("https://cran.r-project.org/src/contrib/e1071_"$_cranver".tar.gz")
sha512sums=('a4aa7e5ae60dfff06d4370a85ff585d60f14fef0a6c1ea0497c7a168c93cf4c2157a063b1f645d6804940126b329e8672b9e3f9d19109da0b5a5a1aa3791a895')

build(){
    R CMD INSTALL e1071_"$_cranver".tar.gz -l "$srcdir"
}

package() {
    install -dm0755 "$pkgdir"/usr/lib/R/library
    cp -a --no-preserve=ownership e1071 "$pkgdir"/usr/lib/R/library
}

