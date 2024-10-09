# Maintainer: Alejandro Quisbert <alejandropqc at protonmail dot com>
# Maintainer: Ali Molaei <ali dot molaei at protonmail dot com>

pkgname=mongosh-bin
_pkgname=mongosh
pkgver=2.3.2
pkgrel=1
pkgdesc='An interactive shell to connect with MongoDB with syntax highlighting, autocomplete, contextual help and error messages.'
arch=('x86_64' 'aarch64')
depends=('krb5')
conflicts=('mongosh')
provides=('mongosh')
url='https://github.com/mongodb-js/mongosh.git'
license=('Apache')
_mongosh_folder=mongosh-${pkgver}-linux

source_x86_64=("https://downloads.mongodb.com/compass/${_pkgname}-${pkgver}-linux-x64.tgz")
source_aarch64=("https://downloads.mongodb.com/compass/${_pkgname}-${pkgver}-linux-arm64.tgz")

sha256sums_x86_64=('2711b71082897535dd2302f51c8c93233aac1dfe466b6982a70df25187a50933')
sha256sums_aarch64=('565619f504f8d79589ca37b20209ee91ab0c7d0ce7981f340f72d2b527a297b6')

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
