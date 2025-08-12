# Maintainer: Ruben Di Battista <rubendibattista@gmail.com>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
## Based on mambaforge aur package by Ashwin Vishn Immae, Martin Wimpress and Jingbei Li
pkgname=miniforge
pkgver=25.3.1.0
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
sha256sums_x86_64=('376b160ed8130820db0ab0f3826ac1fc85923647f75c1b8231166e3d559ab768')
sha256sums_aarch64=('a57c9e3d6c0c449c0283fd07e0bfa30d95eb8d547a14e8dc06c606405d01a7f0')
sha256sums_powerpc64le=('87eb7d349a0ed3ba964c5263d90663e3dff93f252305b7bf24c12e714117bdfe')
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
