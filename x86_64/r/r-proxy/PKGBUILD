# Maintainer: Ward Segers <w@rdsegers.be>

_cranver=0.4-29
pkgname=r-proxy
pkgver=${_cranver//[:-]/.}
pkgrel=1
pkgdesc='An extensible framework for auto- and cross-proximities'
arch=('x86_64')
url='https://cran.r-project.org/web/packages/proxy'
license=('GPL')
depends=('r')
source=("https://cran.r-project.org/src/contrib/proxy_"$_cranver".tar.gz")
sha512sums=('51496ac2b4551bbca49c0c53b8ab955ff99f8e977addbf7bacc0ec3bf01fa0d1f39053ad516c70b8de8b710f00c3f32f6d5db6546a39fef180259deb32251cbf')

build() {
  R CMD INSTALL proxy_"$_cranver".tar.gz -l "$srcdir"
}

package() {
  install -dm0755 "$pkgdir"/usr/lib/R/library
  cp -a --no-preserve=ownership proxy "$pkgdir"/usr/lib/R/library
}
