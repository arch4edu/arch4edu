# Maintainer: Ward Segers <w@rdsegers.be>
# Maintainer: Alex Hirzel <alex@hirzel.us>

# Contributor: Alex Branham <alex.branham@gmail.com>
# Contributor: Robert Greener <me@r0bert.dev>

_cranver=1.7-17
pkgname=r-e1071
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc='Functions for latent class analysis, short time Fourier transform, fuzzy clustering, support vector machines, shortest path computation, bagged clustering, naive Bayes classifier, ...'
arch=('x86_64')
url='https://cran.r-project.org/web/packages/e1071'
license=('GPL-2.0-or-later')
depends=('r' 'r-proxy')
replaces=('r-cran-e1071')
source=("https://cran.r-project.org/src/contrib/e1071_"$_cranver".tar.gz")
sha512sums=('32a7a7b31e3881130051ab41ca577ab582f5161f2492bde7d7b22d3f3734144b29b28eb25897987e51d44c9c977a719986117971103f1e0442669153ae4f4763')

build() {
  R CMD INSTALL e1071_"$_cranver".tar.gz -l "$srcdir"
}

package() {
  install -dm0755 "$pkgdir"/usr/lib/R/library
  cp -a --no-preserve=ownership e1071 "$pkgdir"/usr/lib/R/library
}
