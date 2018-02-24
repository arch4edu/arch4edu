# Maintainer : Immae <ismael.bouya@normalesup.org>
# Contributor : Martin Wimpress <code@flexion.org>
# Contributor : Jingbei Li <i@jingbei.li>
pkgname=anaconda2
pkgver=5.1.0
pkgrel=1
pkgdesc="Completely free enterprise-ready Python distribution for large-scale data processing, predictive analytics, and scientific computing."
arch=('x86_64')
url="https://store.continuum.io/cshop/anaconda/"
license=("custom")
source=("http://repo.continuum.io/archive/Anaconda2-${pkgver}-Linux-x86_64.sh"
"$pkgname.install")
options=(!strip libtool staticlibs)
sha256sums=('5f26ee92860d1dffdcd20910ff2cf75572c39d2892d365f4e867a611cca2af5b'
            'c491735df1753335c6aa5b3b71bd936ccb4ff5622fedbf22d1d6d9da5bd45fbc')
install="$pkgname.install"

prepare() {
	cd ${srcdir}
	msg2 "Patching Anaconda2-${pkgver}-Linux-x86_64.sh"
	sed \
		-e '/wc -c "\$THIS_PATH" | grep/s/!//' \
		-e "/export FORCE/s|$|;sed \"/^def update_prefix/a\\\    new_prefix='/opt/$pkgname'\" -i pkgs/.install.py|" \
		-i Anaconda2-${pkgver}-Linux-x86_64.sh
}

package() {
	prefix=${pkgdir}/opt/${pkgname}
	LD_PRELOAD="/usr/lib/libfakeroot/libfakeroot.so"

	msg2 "Installing ${pkgname} to /opt/${pkgname}"
	bash ${srcdir}/Anaconda2-${pkgver}-Linux-x86_64.sh -b -p $prefix -f
	[ "$BREAK_EARLY" = 1 ] && exit 1
	cd $prefix

	msg2 "Correcting permissions"
	chmod a+r -R pkgs

	msg2 "Stripping \$pkgdir from default meta"
	find conda-meta -name '*.json' -exec sed -e "s/${pkgdir//\//\\\/}//g" -i {} \;

	msg2 "Installing license"
	install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
