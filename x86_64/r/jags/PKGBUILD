# Maintainer: Joona P <jonppep at gmail dot com>
# Contributor: Miguel de Val-Borro <miguel at archlinux dot net>
# Contributor: miggy <jkomdl at gmail dot com>

pkgname=jags
pkgver=4.3.2
pkgrel=1
pkgdesc="Bayesian hierarchical models using Markov Chain Monte Carlo (MCMC) simulation"
arch=('any')
url="https://mcmc-jags.sourceforge.io/"
license=('GPL')
depends=('lapack' 'libtool')
options=('!libtool')
makedepends=('gcc-fortran' 'lapack')
source=(https://downloads.sourceforge.net/project/mcmc-jags/JAGS/4.x/Source/JAGS-$pkgver.tar.gz)
sha1sums=('1659156ee49a81e5b2c84d6c9815f82379dce3e8')

build () {
	cd "$srcdir/JAGS-$pkgver"
	./configure --prefix=/usr --libexecdir=/usr/lib/${pkgname}
	make
}

package() {
	cd "$srcdir/JAGS-$pkgver"
	make DESTDIR="$pkgdir/" install
}
