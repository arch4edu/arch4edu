# Maintainer: Joona P <jonppep at gmail dot com>
# Contributor: Miguel de Val-Borro <miguel at archlinux dot net>
# Contributor: miggy <jkomdl at gmail dot com>

pkgname=jags
pkgver=4.3.1
pkgrel=1
pkgdesc="Bayesian hierarchical models using Markov Chain Monte Carlo (MCMC) simulation"
arch=('x86_64' 'i686')
url="https://mcmc-jags.sourceforge.io/"
license=('GPL')
depends=('lapack' 'libtool')
options=('!libtool')
makedepends=('gcc-fortran' 'lapack')
source=(https://downloads.sourceforge.net/project/mcmc-jags/JAGS/4.x/Source/JAGS-$pkgver.tar.gz)
md5sums=('3b311562c2be7965072709f488600e5a')
build () {
	cd "$srcdir/JAGS-$pkgver"
	./configure --prefix=/usr --libexecdir=/usr/lib/${pkgname}
	make
}
package() {
	cd "$srcdir/JAGS-$pkgver"
	make DESTDIR="$pkgdir/" install
}
