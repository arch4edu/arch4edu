# Maintainer  : George Eleftheriou <eleftg>
# Contributor : Martin Wimpress <code@flexion.org>
# Contributor : Nick Pope
# Contributor : Bryce Nordgren <bnordgren at gmail dot com>

pkgname=hdfview-beta
_pkgname=HDFView
__pkgname=${pkgname%-beta}
pkgver=3.0.0
pkgrel=2
pkgdesc="a GUI browser for reading hdf5 files (created with versions up to 1.10)"
arch=('i686' 'x86_64')
url="https://support.hdfgroup.org/products/java/release/hdfview3.html"
license=('custom')
depends=('hdf5-openmpi-java' 'hdf4-java')
makedepends=('apache-ant' 'java-environment')
options=(!strip)
source=("https://support.hdfgroup.org/ftp/HDF5/releases/HDF-JAVA/${__pkgname}-${pkgver}/src/${__pkgname}-${pkgver}.tar.gz"
        license
        ${_pkgname}-beta.desktop
        ${_pkgname}-beta.ico)
md5sums=('0a05625e78c01f4603d03b1fbf0a84cd'
         'db0de6079dd881781768d05de29c50e0'
         '0d10b620f2debd0d73be53873d4bf347'
         'b86542f80203ea9f93f447fa7c20d25a')

prepare() {
  cd "${__pkgname}-${pkgver}"
}

build() {
  cd "${__pkgname}-${pkgver}"
  HDFLIBS=/opt/hdf4 HDF5LIBS=/usr ant package
}

package() {
  cd "${__pkgname}-${pkgver}"
  mkdir "${pkgdir}/opt"
  cp -a "build/dist/${_pkgname}-${pkgver}-Linux.sh" "${pkgdir}/opt"
  cd "${pkgdir}/opt"

  # Make extraction non interactive
  sed -i 's/interactive=TRUE/interactive=FALSE/' ${_pkgname}-${pkgver}-Linux.sh
  sed -i 's/cpack_skip_license=FALSE/cpack_skip_license=TRUE/' ${_pkgname}-${pkgver}-Linux.sh

  ./${_pkgname}-${pkgver}-Linux.sh
  rm "${_pkgname}-${pkgver}-Linux.sh"
  mkdir -p "${pkgdir}/usr/bin"

  sed -i "s:JAVABIN=${pkgdir}/opt/${_pkgname}/${pkgver}/jre/bin:JAVABIN=/opt/${_pkgname}/${pkgver}/jre/bin:" "${_pkgname}/${pkgver}/hdfview.sh"
  sed -i "s:INSTALLDIR=${pkgdir}/opt/${_pkgname}/${pkgver}:INSTALLDIR=/opt/${_pkgname}/${pkgver}:" "${_pkgname}/${pkgver}/hdfview.sh"

  # Desktop files, icons, wrappers and license
  install -D -m 755 "${_pkgname}/${pkgver}/hdfview.sh" "${pkgdir}/usr/bin/hdfview-beta.sh"
  install -D -m 644 "${srcdir}/${_pkgname}-beta.desktop" "${pkgdir}/usr/share/applications/${_pkgname}-beta.desktop"
  install -D -m 644 "${srcdir}/${_pkgname}-beta.ico" "${pkgdir}/usr/share/pixmaps/${_pkgname}-beta.ico"
  install -D -m 644 "${srcdir}/license" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
