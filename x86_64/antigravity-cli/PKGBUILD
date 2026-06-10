# Maintainer: Coraline Shuryn <coraline.shuryn@gmail.com>
pkgname=antigravity-cli
pkgver=1.0.7_5436940900761600
pkgrel=1
pkgdesc="Google's agentic development platform (CLI companion)"
arch=('x86_64' 'aarch64')
url="https://antigravity.google/"
license=('custom:proprietary')
provides=('agy')
conflicts=('agy')
depends=('glibc')
optdepends=('antigravity: to authenticate and share session state from the desktop application')
options=('!strip')
install=antigravity-cli.install

source=("LICENSE")
sha256sums=('7bcdb3cf53451b33c75e04f1f0e623e8aa8b7943a72f54f4781a7ad545a7d1ce')
sha256sums_x86_64=('f5bb465edb938212eb0a185d68c420ff5b78f08c72de5a6d88dfefaf7af17074')
sha256sums_aarch64=('400a48e67723e41f1ff2c84705fc8866c5822c4fab21d4b72fe7dbaf120b2114')

source_x86_64=("${pkgname}-${pkgver}-x86_64.tar.gz::https://storage.googleapis.com/antigravity-public/antigravity-cli/${pkgver//_/-}/linux-x64/cli_linux_x64.tar.gz")
source_aarch64=("${pkgname}-${pkgver}-aarch64.tar.gz::https://storage.googleapis.com/antigravity-public/antigravity-cli/${pkgver//_/-}/linux-arm/cli_linux_arm64.tar.gz")


package() {
    install -Dm755 "${srcdir}/antigravity" "${pkgdir}/usr/bin/agy"
    install -Dm644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
