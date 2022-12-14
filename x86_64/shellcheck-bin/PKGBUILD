# Maintainer: Silvio <s.i.l.v.io..f.r.i.c.k.e@gmail.com>
# Contribute via: https://github.com/silvio/archlinux-package--shellcheck-bin

# Contributor: katt <magunasu.b97@gmail.com>

pkgname=shellcheck-bin
pkgver=0.9.0
pkgrel=1
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

sha512sums_x86_64=('157fd8b2c18a257f3876e23015580ea63d27b12c4f13f87d625a180e8ca042e7501271d15edeb36e7b5780da73815b45386a33e063ab1c891d838f35c778a8ac')
sha512sums_armv6h=('ac495f5bcf358b5de9f2cbb275b30050e586218458c97c01444076947d22e9cb7acc817e361599290e22bf25996deb8006240e0350ef864372a29db3032c1388')
sha512sums_aarch64=('3c11bc1901d470ba7f95334fcd4d8ea9c39c73ebb15655cd0cc478826279b02413409fa3f7b011c7ecdba98530953be54906b4a99b898b064c236f146f3ec749')


package() {
    install -Dm755 "${pkgname%-bin}-v${pkgver}/${pkgname%-bin}" -t "${pkgdir}/usr/bin"
}
