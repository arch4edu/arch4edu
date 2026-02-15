# Maintainer: Ruben Di Battista <rubendibattista@gmail.com>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
## Based on mambaforge aur package by Ashwin Vishn Immae, Martin Wimpress and Jingbei Li
pkgname=miniforge
pkgver=26.1.0.0
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
sha256sums_x86_64=('127b5e14cfe6c83b787f624487cdc2168645ed82fdca1b0c1937caa086aed6d5')
sha256sums_aarch64=('8baf8844ecf13e1458f81659ea286251d04b2d5ed90040efb77f158adedb2d95')
sha256sums_powerpc64le=('902190ad825b74b78a6a2816364453bb4d6989a599172aa3785d4afd0ebeb917')
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
