# Maintainer: Mikuro Kagamine <mikurok@forgecrushing.com>

pkgname=browsh-bin
pkgver=1.8.2
pkgrel=1
pkgdesc='A fully-modern text-based browser, rendering to TTY and browsers'
arch=('x86_64' 'i386' 'i486' 'i586' 'i686' 'armv6h' 'armv7h' 'aarch64')
url='https://www.brow.sh'
license=('LGPL2.1')
makeoptdepends=('upx: compress binary')
depends=('firefox>=63')
provides=('browsh')
conflicts=('browsh' 'browsh-git')
options=('!strip')
source_x86_64=("https://github.com/${provides[0]}-org/${provides[0]}/releases/download/v${pkgver}/${provides[0]}_${pkgver}_linux_amd64")
source_i386=("https://github.com/${provides[0]}-org/${provides[0]}/releases/download/v${pkgver}/${provides[0]}_${pkgver}_linux_386")
source_i486=($source_i386)
source_i586=($source_i386)
source_i686=($source_i386)
source_armv6h=("https://github.com/${provides[0]}-org/${provides[0]}/releases/download/v${pkgver}/${provides[0]}_${pkgver}_linux_armv6")
source_armv7h=("https://github.com/${provides[0]}-org/${provides[0]}/releases/download/v${pkgver}/${provides[0]}_${pkgver}_linux_armv7")
source_aarch64=("https://github.com/${provides[0]}-org/${provides[0]}/releases/download/v${pkgver}/${provides[0]}_${pkgver}_linux_arm64")
sha256sums_x86_64=('a20aeaad841e41634d5a4ca43845e9bf81a4fd3e8123efcc870668e2091ccb1f')
sha256sums_i386=('eb5518aaba26f1c56787ec18751729337dc7c9b58a2439a814fe3d7c807a8d91')
sha256sums_i486=('eb5518aaba26f1c56787ec18751729337dc7c9b58a2439a814fe3d7c807a8d91')
sha256sums_i586=('eb5518aaba26f1c56787ec18751729337dc7c9b58a2439a814fe3d7c807a8d91')
sha256sums_i686=('eb5518aaba26f1c56787ec18751729337dc7c9b58a2439a814fe3d7c807a8d91')
sha256sums_armv6h=('e8351245f099d50844cb1aa932238082dc71660235795352bfa1b2320c0cd4b7')
sha256sums_armv7h=('49d4f568dd328ad74c9a28f4818d78b26a2841c4824d0d9ee3b7472c364bc97e')
sha256sums_aarch64=('c805136292ba03c5520752819c532909c70411c811a15cd7bc4c0d3d92f9d8e1')

prepare() {
	cat ${provides[0]}_${pkgver}_linux_* > ${provides[0]}
	if [ $(which upx 2>/dev/null) ]; then
		echo Compressing ${provides[0]} with UPX...
		chmod u+x ${provides[0]}
		upx ${provides[0]}; fi
}

package() {
	install -Dm755 ${provides[0]} "$pkgdir/usr/bin/${provides[0]}"
}
