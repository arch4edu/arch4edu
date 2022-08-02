# Maintainer: Mikuro Kagamine <mikurok@forgecrushing.com>

pkgname=browsh-bin
pkgver=1.8.0
pkgrel=1
pkgdesc='A fully-modern text-based browser, rendering to TTY and browsers'
arch=('x86_64' 'i386' 'i486' 'i586' 'i686' 'armv6h' 'armv7h' 'aarch64')
url='https://www.brow.sh'
license=('LGPL2.1')
optdepends=('upx: compress binary')
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
sha256sums_x86_64=('30a6b4e5220be088bce9b2416164eed7d3d8de76741e6a71d24a35b2fe6f1ae7')
sha256sums_i386=('887c4e0d2679fd0d91c0867f4643771286c5320b1f84966f67a22cced8a90c85')
sha256sums_i486=($sha256sums_i386)
sha256sums_i586=($sha256sums_i386)
sha256sums_i686=($sha256sums_i386)
sha256sums_armv6h=('e799299732d9ebc6885c27e483fe8c43d452f9052f09df1d674600cba5eb2177')
sha256sums_armv7h=('db4c9ac68d527e5cc7f53611db0cd7dcdf59307599b19faad181d15db6d36968')
sha256sums_aarch64=('e5e3ed418e0930d0ec12394894269983f6e6da80ff60d03909e2e5c307971a99')

prepare() {
	cat ${provides[0]}_${pkgver}_linux_* > ${provides[0]}
	if [ $(which upx 2>/dev/null) ]; then
		echo Compressing ${provides[0]} with UPX...
		chmod u+x ${provides[0]}
		upx ${provides[0]}; fi
}

package() {
	depends=('firefox>=63')
	install -Dm755 ${provides[0]} "$pkgdir/usr/bin/${provides[0]}"
}
