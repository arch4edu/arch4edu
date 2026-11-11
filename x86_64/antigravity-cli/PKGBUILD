# Maintainer: Coraline Shuryn <coraline.shuryn@gmail.com>
pkgname=antigravity-cli
pkgver=1.5.5_6740358537805824
pkgrel=1
pkgdesc="Google's agentic development platform (CLI companion)"
arch=('x86_64' 'aarch64')
url="https://antigravity.google/product/antigravity-cli"
license=('custom:proprietary')
provides=('agy')
conflicts=('agy')
depends=('glibc')
optdepends=('antigravity: to authenticate and share session state from the desktop application')
options=('!strip')
install=antigravity-cli.install

source=("LICENSE")
sha256sums=('7bcdb3cf53451b33c75e04f1f0e623e8aa8b7943a72f54f4781a7ad545a7d1ce')
sha256sums_x86_64=('bfe2c25edeadd98c2942417c9972ee0e1faa3f0afdc90711e84d5f3a633b5078')
sha256sums_aarch64=('f6faff7b47ad2d9a60ebca9d774239a1cd23e53a8ca6d812c1e9583909dca655')

source_x86_64=("${pkgname}-${pkgver}-x86_64.tar.gz::https://storage.googleapis.com/antigravity-public/antigravity-cli/${pkgver//_/-}/linux-x64/cli_linux_x64.tar.gz")
source_aarch64=("${pkgname}-${pkgver}-aarch64.tar.gz::https://storage.googleapis.com/antigravity-public/antigravity-cli/${pkgver//_/-}/linux-arm/cli_linux_arm64.tar.gz")


package() {
    install -Dm755 "${srcdir}/antigravity" "${pkgdir}/usr/bin/agy"
    install -Dm644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
