# Maintainer : kastik <kastik69420@gmail.com>
# Contributor : Jingbei Li <i@jingbei.li>
# Contributor : Immae <ismael.bouya@normalesup.org>
# Contributor : Martin Wimpress <code@flexion.org>
pkgname=anaconda
pkgver=2021.11
pkgrel=1
pkgdesc="Completely free enterprise-ready Python distribution for large-scale data processing, predictive analytics, and scientific computing."
arch=('x86_64')
url='https://www.anaconda.com/'
license=("BSD")
source=("https://repo.anaconda.com/archive/Anaconda3-${pkgver}-Linux-x86_64.sh")
options=(!strip libtool staticlibs)
sha256sums=('fedf9e340039557f7b5e8a8a86affa9d299f5e9820144bd7b92ae9f7ee08ac60')
install="$pkgname.install"

package() {
	prefix=${pkgdir}/opt/${pkgname}
	LD_PRELOAD="/usr/lib/libfakeroot/libfakeroot.so"

	msg2 "Installing ${pkgname} to /opt/${pkgname}"
	bash ${srcdir}/Anaconda3-${pkgver}-Linux-${CARCH}.sh -b -p $prefix -f
	[ "$BREAK_EARLY" = 1 ] && exit 1
	cd $prefix

	msg2 "Correcting permissions"
	chmod a+r -R pkgs

	msg2 "Stripping \$pkgdir"
	sed -e "s|${pkgdir}||g" -i $(grep "${pkgdir}" . -rIl 2>/dev/null)

	msg2 "Installing license"
	install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
