# Maintainer: Silvio <s.i.l.v.io..f.r.i.c.k.e@gmail.com>
# Contribute via: https://github.com/silvio/archlinux-package--shellcheck-bin

# Contributor: katt <magunasu.b97@gmail.com>

pkgname=shellcheck-bin
pkgver=0.10.0
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

sha512sums_x86_64=('31006830087c2b9ffe9fa36c1ab4a8b11c85078cac8203265d0cfd630c70a4a506e66dd9d7ccde964360ad95045894149de457db34f10cad76708c7a4aa544ca')
sha512sums_armv6h=('466acfbd956d6a90f7e66c852b62fc0b9c236c1315ee58b0658780549f1b73c9a13cf203574de5969cf665f99046c4cff234813ffa45732eb7b0ea083350b4d1')
sha512sums_aarch64=('77abeaa8bee293264ebfd94a2021bd490695ed5518f2da7c0f9ec4b402cd1e5da6642a0e9f953961510cef7351cc9afae7c7a528a597d1befd1867b8c69e15b1')


package() {
    install -Dm755 "${pkgname%-bin}-v${pkgver}/${pkgname%-bin}" -t "${pkgdir}/usr/bin"
}
