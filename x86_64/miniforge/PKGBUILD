# Maintainer: Ruben Di Battista <rubendibattista@gmail.com>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
## Based on mambaforge aur package by Ashwin Vishn Immae, Martin Wimpress and Jingbei Li
pkgname=miniforge
pkgver=24.11.0.0
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
sha256sums_x86_64=('5fa69e4294be07229a94a1c1e8073fbf63894c757c2136f98c87b48f9d458793')
sha256sums_aarch64=('47cfd3caf3a0a6f56ebbfc7da775306fe076b8e49b14d3fd88b5463ab324c185')
sha256sums_powerpc64le=('877e3992041e36f49ce16681e5b24e23617ad044d1a077cf21b5cce90896e244')
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
