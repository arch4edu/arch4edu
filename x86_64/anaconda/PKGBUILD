# Maintainer: Jingbei Li <i@jingbei.li>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: kastik <kastik69420@gmail.com>
# Contributor: Ismaël Bouya <ismael.bouya@normalesup.org>
# Contributor: Martin Wimpress <code@flexion.org>
pkgname=anaconda
pkgver=2025.06.1
_pkgver=${pkgver%.*}-${pkgver##*.}
pkgrel=1
pkgdesc="Simplifies package management and deployment of Anaconda"
arch=(x86_64 aarch64)
url="https://${pkgname}.com"
license=('custom')
provides=('conda')
optdepends=('libxau: for Anaconda Navigator support'
  'libxi: for Anaconda Navigator support'
  'libxss: for Anaconda Navigator support'
  'libxtst: for Anaconda Navigator support'
  'libxcursor: for Anaconda Navigator support'
  'libxcomposite: for Anaconda Navigator support'
  'libxdamage: for Anaconda Navigator support'
  'libxfixes: for Anaconda Navigator support'
  'libxrandr: for Anaconda Navigator support'
  'libxrender: for Anaconda Navigator support'
  'mesa: for Anaconda Navigator support'
  'alsa-lib: for Anaconda Navigator support'
  'libglvnd: for Anaconda Navigator support'
  'xdg-utils: for ')
source=(${pkgname}-navigator.desktop)
source_x86_64=(https://repo.${pkgname}.com/archive/Anaconda3-${_pkgver}-Linux-x86_64.sh)
source_aarch64=(https://repo.${pkgname}.com/archive/Anaconda3-${_pkgver}-Linux-aarch64.sh)
options=(!strip libtool staticlibs)
sha512sums=('5822dd55b1668b166134ec6dc414b3ad13f34c4271e9dba8d2d4adb34440c8b664ce5b6f2b6bb9752f5ec115d8671015fca035f2f94c92d5ce8aba2a1782a9d5')
sha512sums_x86_64=('dbdffcf50539386c7a853fe386b0b10a34d93c8d78d1b370585e192d885f7e2e49e1ee2315dc899156cb47b1070b175744c78a85465ebbc0fe43d0fafd8db307')
sha512sums_aarch64=('7909645554dcedab4820f7758d81795e090091a93b62ba0a76d32bac4b9ea4f3e8cf9d9325bc07c47d3d81ebae6c9cf2c5620067a38618564ba77391710a23d1')
install="${pkgname}.install"

package() {
  prefix="${pkgdir}"/opt/${pkgname}
  LD_PRELOAD="/usr/lib/libfakeroot/libfakeroot.so"

  # Packaging anaconda for installation to /opt/anaconda
  bash "${srcdir}"/Anaconda3-${_pkgver}-Linux-${CARCH}.sh -b -p $prefix -f
  [ "$BREAK_EARLY" = 1 ] && exit 1
  cd $prefix

  # Correcting permissions
  chmod a+r -R pkgs

  # Stripping $pkgdir
  sed -e "s|${pkgdir}||g" -i $(grep "${pkgdir}" . -rIl 2>/dev/null)

  # Installing license
  install -Dm 644 LICENSE.txt -t "${pkgdir}/usr/share/licenses/${pkgname}"

  # Installing .desktop for anaconda navigator
  install -Dm 644 "${srcdir}/${pkgname}-navigator.desktop" -t "${pkgdir}"/usr/share/applications/
}
