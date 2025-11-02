# Maintainer: Alejandro Quisbert <alejandropqc at protonmail dot com>
# Maintainer: Ali Molaei <ali dot molaei at protonmail dot com>

pkgname=mongosh-bin
_pkgname=mongosh
pkgver=2.5.9
pkgrel=1
pkgdesc='An interactive shell to connect with MongoDB with syntax highlighting, autocomplete, contextual help and error messages.'
arch=('x86_64' 'aarch64')
depends=('krb5')
conflicts=('mongosh')
provides=('mongosh')
url='https://github.com/mongodb-js/mongosh.git'
license=('Apache')
_mongosh_folder=mongosh-${pkgver}-linux

source_x86_64=("https://github.com/mongodb-js/mongosh/releases/download/v${pkgver}/${_pkgname}-${pkgver}-linux-x64.tgz")
source_aarch64=("https://github.com/mongodb-js/mongosh/releases/download/v${pkgver}/${_pkgname}-${pkgver}-linux-arm64.tgz")

sha256sums_x86_64=('0644b6ac0b99dd52f46bdc4085aae19bb6d51226ef346c51418321769e76363e')
sha256sums_aarch64=('01d6cb109e59769edfa5b44c93cc69bced8f39c216c3d4d1df471ecbc3f2d356')

package() {
	if [ $CARCH = 'x86_64' ]; then
		_arch=x64;
	elif [ $CARCH = 'aarch64' ]; then
		_arch=arm64;
	fi
	install -D $_mongosh_folder-${_arch}/bin/mongosh "$pkgdir/usr/bin/mongosh"
	install -D $_mongosh_folder-${_arch}/bin/mongosh_crypt_v1.so "$pkgdir/usr/lib/mongosh_crypt_v1.so"
	install -Dm644 $_mongosh_folder-${_arch}/mongosh.1.gz "$pkgdir/usr/share/man/man1/mongosh.1.gz" 
}
