# Maintainer: Alejandro Quisbert <alejandropqc at protonmail dot com>
# Maintainer: Ali Molaei <ali dot molaei at protonmail dot com>

pkgname=mongosh-bin
_pkgname=mongosh
pkgver=1.8.0
pkgrel=1
pkgdesc='An interactive shell to connect with MongoDB with syntax highlighting, autocomplete, contextual help and error messages.'
arch=('x86_64' 'aarch64')
depends=('krb5')
url='https://github.com/mongodb-js/mongosh.git'
license=('Apache')
_mongosh_folder=mongosh-${pkgver}-linux

source_x86_64=("https://downloads.mongodb.com/compass/${_pkgname}-${pkgver}-linux-x64.tgz")
sha256sums_x86_64=('a99c22199056e28a48b632d4635124f48446612723d201853bc0065dfca6bf21')
source_aarch64=("https://downloads.mongodb.com/compass/${_pkgname}-${pkgver}-linux-arm64.tgz")
sha256sums_aarch64=('6b20b776981d296820e55b366ee4aedcb929190cf8be80e12bbca8a11d5f538c')

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
