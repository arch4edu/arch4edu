# Maintainer: robertfoster
# Contributor: LIN Rs <LinRs[d]users.noreply.github.com>
# Contributor: yochananmarqos <mark.wagie at tutanota dot com>

pkgbase=devilutionx
pkgname=("${pkgbase}" "${pkgbase}-fonts" "${pkgbase}-voices")
pkgver=1.5.2
pkgrel=1
pkgdesc="Diablo devolved for linux"
arch=('armv6h' 'armv7h' 'arm' 'aarch64' 'i686' 'x86_64')
url="https://github.com/diasurgical/devilutionX"
license=('custom:unlicense')
depends=('bzip2' 'fmt' 'libpng' 'libsodium' 'sdl2' 'sdl2_image' 'simpleini' 'zlib')
makedepends=('cmake' 'devilutionx-graphics-tools-git' 'flac' 'gettext' 'git' 'lame' 'ninja' 'smpq')
options=('strip')
source=("${url}/releases/download/${pkgver}/devilutionx-src.tar.xz"
  "${url}-assets/releases/download/v4/fonts.mpq"
  "${url}-assets/releases/download/v4/pl.mpq"
  "${url}-assets/releases/download/v4/ru.mpq"
)

build() {
  cmake -S "${pkgbase}-src-${pkgver}" \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX="/usr" \
    -DBUILD_TESTING=off \
    -DCPACK=ON \
    -Bbuild

  cmake --build build -j $(getconf _NPROCESSORS_ONLN)
}

package_devilutionx() {
  pkgdesc="Diablo devolved for linux (main package)"
  install="${pkgbase}".install
  optdepends=("${pkgbase}-fonts" "${pkgbase}-voices")

  cd build
  DESTDIR="${pkgdir}" \
    cmake --install .
}

package_devilutionx-voices() {
  pkgdesc="Additional voices for DevilutionX"
  depends=("${pkgbase}")

  install -Dm644 pl.mpq \
    "${pkgdir}/usr/share/diasurgical/devilutionx/pl.mpq"
  install -Dm644 ru.mpq \
    "${pkgdir}/usr/share/diasurgical/devilutionx/ru.mpq"
}

package_devilutionx-fonts() {
  pkgdesc="Additional fonts for DevilutionX"
  depends=("${pkgbase}")

  install -Dm644 fonts.mpq \
    "${pkgdir}/usr/share/diasurgical/devilutionx/fonts.mpq"
}

sha256sums=('27dc99cb8b40cb6fccbb5935aac7ce0c906664cc3815bcf9e27195747db46ed3'
  '551ecee2d95b4e7807737a7794a6bacf0b4a03a91634816277b91db35ce1e259'
  '715763a7e35347fd42041b35d961189c932d9d320ee29b6929106e550b0e42de'
  '48bfb5baeed370b565a61db5eab90214700121311a3c40e50d2671d5bac8778b')
