# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix
# Contributor: txtsd <aur.archlinux@ihavea.quest>
# Contributor: Marcel Korpel <marcel[dot]korpel[at]gmail>
# Contributor: Olaf Bauer <hydro@freenet.de>

pkgname=makemkv
pkgver=1.18.2
pkgrel=1
pkgdesc="DVD and Blu-ray to MKV converter"
arch=(x86_64 i686 aarch64)
url="https://www.makemkv.com"
license=('LicenseRef-GuinpinSoft-inc-EULA' LGPL-2.1-or-later)
depends=(qt5-base ffmpeg libavcodec.so)
optdepends=('java-runtime: bdjava https://www.makemkv.com/bdjava/')
install=makemkv.install
source=(${url}/download/${pkgname}-bin-${pkgver}.tar.gz
        ${url}/download/${pkgname}-oss-${pkgver}.tar.gz
        makemkv.1
        makemkvcon.1
        )
sha256sums=('bfc4c7cebc0f00497671ffd56e6a34f0770a9e6af7eff2f0127efa143f28636e'
            'b9497f5555c257f5d3c7f18b6ab03c74cff3ea4437e80349d618d115bf5fa445'
            '5573b2e4bade10d8cd258a7c235eb46f66ef8c8c97e5d5eb090c38fa0f94389b'
            'f12c0facf2f0071a9f728b138986f0a4c2b4ff6ace2dfb2e96364e215e9fda6f')

build() {
  cd "${srcdir}/${pkgname}-oss-${pkgver}"
  ./configure --prefix=/usr
  make
}

package() {
  cd "${srcdir}/${pkgname}-oss-${pkgver}"
  make DESTDIR="${pkgdir}" install

  cd "${srcdir}/${pkgname}-bin-${pkgver}"
  install -d tmp
  echo accepted > tmp/eula_accepted
  make DESTDIR="${pkgdir}" install

  install -Dm 644 src/eula_en_linux.txt "${pkgdir}/usr/share/licenses/${pkgname}/eula_en_linux.txt"

  cd "${srcdir}/"
  install -d "${pkgdir}/usr/share/man/man1/"
  install -m 644 -t "${pkgdir}/usr/share/man/man1/" makemkv.1 makemkvcon.1
}
