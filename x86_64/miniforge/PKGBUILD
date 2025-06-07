# Maintainer: Ruben Di Battista <rubendibattista@gmail.com>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
## Based on mambaforge aur package by Ashwin Vishn Immae, Martin Wimpress and Jingbei Li
pkgname=miniforge
pkgver=25.3.0.3
_pkgver=${pkgver%.*}-${pkgver##*.}
pkgrel=1
pkgdesc="Conda and Mamba package managers configured to use conda-forge"
arch=(x86_64 aarch64 powerpc64le)
url="https://github.com/conda-forge/miniforge"
license=(BSD-3-Clause)
provides=(conda mamba)
replaces=(mambaforge)
source_x86_64=(${url}/releases/download/${_pkgver}/Miniforge3-${_pkgver}-Linux-x86_64.sh)
source_aarch64=(${url}/releases/download/${_pkgver}/Miniforge3-${_pkgver}-Linux-aarch64.sh)
source_powerpc64le=(${url}/releases/download/${_pkgver}/Miniforge3-${_pkgver}-Linux-ppc64le.sh)
options=(!strip libtool staticlibs)
sha256sums_x86_64=('1b57f8cb991982063f79b56176881093abb1dc76d73fda32102afde60585b5a1')
sha256sums_aarch64=('ac89f17b0eec4e98d38a53d1ae688e0f22c77d8ea5b5f008c2455e90ef095339')
sha256sums_powerpc64le=('1ce4084983b899d2f895bd13085ba20ff787fbcc2f2c865c618bffc97dd877b8')
install="${pkgname}.install"

package() {
  prefix="${pkgdir}/opt/${pkgname}"
  LD_PRELOAD="/usr/lib/libfakeroot/libfakeroot.so"

  # Packaging mambaforge for installation to /opt/mambaforge
  bash "${srcdir}/Miniforge3-${_pkgver}-Linux-${CARCH}.sh" -b -p $prefix -f
  [ "$BREAK_EARLY" = 1 ] && exit 1
  cd "${prefix}"

  # Correcting permissions
  chmod a+r -R pkgs

  # Stripping $pkgdir
  sed "s|${pkgdir}||g" -i $(grep "$pkgdir" . -rIl)

  # Set string path to a certificate SSL connection
  echo "ssl_verify: /opt/${pkgname}/ssl/cacert.pem" >>"${pkgdir}/opt/${pkgname}/.condarc"

  # Installing license
  install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
