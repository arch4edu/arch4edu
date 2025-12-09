# Maintainer: Alejandro Quisbert <alejandropqc at protonmail dot com>
# Maintainer: Ali Molaei <ali dot molaei at protonmail dot com>

pkgname=mongosh-bin
_pkgname=mongosh
pkgver=2.5.10
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

sha256sums_x86_64=('b9c003d80dbf20d2bb2ad097abe7997a5e2a6a349af96b8510c741570116fc79')
sha256sums_aarch64=('00e44c504eccbcfd467b6160b18efbe7eb7fcc0632cac6149efc94193ce3465e')

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
