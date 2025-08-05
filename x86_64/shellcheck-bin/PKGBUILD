# Maintainer: Silvio <s.i.l.v.io..f.r.i.c.k.e@gmail.com>
# Contribute via: https://github.com/silvio/archlinux-package--shellcheck-bin

# Contributor: katt <magunasu.b97@gmail.com>

pkgname=shellcheck-bin
pkgver=0.11.0
pkgrel=1
url='https://shellcheck.net'
pkgdesc='Shell script analysis tool (binary release, static)'
license=(GPL-3.0-only)
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

sha512sums_x86_64=('25df28923d7d89cfdb9fa8aeef762a887f2bd4ebfbcd43ae71068c60e9458d66250b0f8d6fd66b4bc03723e6cdd47983c547e3ab4f3ea2cbc4bc4028842cc7b9')
sha512sums_armv6h=('4f3530149b9ef5a145af5ed3d2efdb6195cc2910cccdc6e1b47efaeef4b5d5958e234f428000adeb4b2aec4c6b1f9adb050af65dd0b53866aa871b035d4cde3c')
sha512sums_aarch64=('de5e49175861ce567b98ec7ae0dd25f679c169d15b015bbad8f92ca22d07bb17c0fb906f7d80857e8450945f6a185d4de45e5883514e9aeb3cc155306060225e')


package() {
    install -Dm755 "${pkgname%-bin}-v${pkgver}/${pkgname%-bin}" -t "${pkgdir}/usr/bin"
}
