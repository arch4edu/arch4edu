# Maintainer: Silvio <s.i.l.v.io..f.r.i.c.k.e@gmail.com>
# Contribute via: https://github.com/silvio/archlinux-package--shellcheck-bin

# Contributor: katt <magunasu.b97@gmail.com>

pkgname=shellcheck-bin
pkgver=0.8.0
pkgrel=3
url='https://shellcheck.net'
pkgdesc='Shell script analysis tool (binary release, static)'
license=(AGPL3)
arch=(x86_64 armv6h aarch64)
conflicts=(
	"shellcheck"
	"shellcheck-git"
	"shellcheck-git-static"
)
provides=("shellcheck")

source_x86_64=(https://github.com/koalaman/"${pkgname%-bin}"/releases/download/v"$pkgver"/"${pkgname%-bin}"-v"${pkgver}".linux.x86_64.tar.xz)
source_armv6h=(https://github.com/koalaman/"${pkgname%-bin}"/releases/download/v"$pkgver"/"${pkgname%-bin}"-v"${pkgver}".linux.armv6hf.tar.xz)
source_aarch64=(https://github.com/koalaman/"${pkgname%-bin}"/releases/download/v"$pkgver"/"${pkgname%-bin}"-v"${pkgver}".linux.aarch64.tar.xz)

sha512sums_x86_64=('89317d97adb341e627b709e86477734ce236e9fb290de8a8c41cdc62769a3225622fa609deffebeabe9edb71f5639a086f61b677947e3ec4bc07c540fcbd0973')
sha512sums_armv6h=('a00a00a58d00d0879fbd9f601902eb96105da0b9ac5220a4176dce73d22c1ba8108435fb6f8c0ae0b450e32a207f49ecaf84d7830feb512359f27e8eae2ec190')
sha512sums_aarch64=('7082a5002a1ea2403cd6c24665149a0444960a66dc2002f2e38726a6ed4f7f0499a051679cef8de619e401e8754b13a65624fdb108d7225cb486219184c44c12')


package() {
    install -Dm755 "${pkgname%-bin}-v${pkgver}/${pkgname%-bin}" -t "${pkgdir}/usr/bin"
}
