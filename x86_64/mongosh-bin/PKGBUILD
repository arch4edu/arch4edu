# Maintainer: Alejandro Quisbert <alejandropqc at protonmail dot com>
# Maintainer: Ali Molaei <ali dot molaei at protonmail dot com>

pkgname=mongosh-bin
_pkgname=mongosh
pkgver=2.12.0
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

sha256sums_x86_64=('aa42cb826b7b8e655c5481293f5365ddaf1a23e43af07520326e5bbc957838ad')
sha256sums_aarch64=('99f8d38d41c510e7d4c685b71022ea1db113245968d5d933b5333fb3835e64ae')

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
