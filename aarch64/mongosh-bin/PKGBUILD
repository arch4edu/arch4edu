# Maintainer: Alejandro Quisbert <alejandropqc at protonmail dot com>
# Maintainer: Ali Molaei <ali dot molaei at protonmail dot com>

pkgname=mongosh-bin
_pkgname=mongosh
pkgver=1.6.0
pkgrel=1
pkgdesc='An interactive shell to connect with MongoDB with syntax highlighting, autocomplete, contextual help and error messages.'
arch=('x86_64' 'aarch64')
depends=('krb5')
url='https://github.com/mongodb-js/mongosh.git'
license=('Apache')
_mongosh_folder=mongosh-${pkgver}-linux

source_x86_64=("https://downloads.mongodb.com/compass/${_pkgname}-${pkgver}-linux-x64.tgz")
sha256sums_x86_64=('cc6271d9e6bbe052c6a6017c4b10ecbf28a2ff6320537e3bb9b7aea2f83fbeb7')
source_aarch64=("https://downloads.mongodb.com/compass/${_pkgname}-${pkgver}-linux-arm64.tgz")
sha256sums_aarch64=('bf5edc8ee822f1f5c6f7a7d52643cb57416a08fb99943b04c51df69d259e0eef')

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
