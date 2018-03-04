# Maintainer  : George Eleftheriou <eleftg>
# Contributor : Martin Wimpress <code@flexion.org>
# Contributor : Nick Pope
# Contributor : Bryce Nordgren <bnordgren at gmail dot com>

pkgname=hdfview
_pkgname=HDFView
pkgver=2.14.0
_pkgver=${pkgver%.0}
pkgrel=6
pkgdesc="a GUI browser for reading hdf5 files (created with versions up to 1.8)"
arch=('i686' 'x86_64')
url="https://support.hdfgroup.org/products/java/"
license=('custom')
depends=('hdf-java')
makedepends=('apache-ant' 'java-environment')
options=(!strip)
source=("https://support.hdfgroup.org/ftp/HDF5/hdf-java/current/src/${pkgname}-${_pkgver}.tar.gz"
        "${_pkgname}"
	"${_pkgname}.desktop"
        "${_pkgname}.ico"
        license)
sha256sums=('97a08300bba3f8b799a16d1d08ff9a1b2dd94757717dcf2a09d7c2539d6c6953'
         'ffcd06e84214ebdb67ff46140708c6282558134e4f33146d53f10d67ea0b42bd'
         'ceb3c33a6bf7462722328153903124eb743338e3bedc9255ac1b1251907ced9c'
         '8d3e8e2c070e538f0a8de0d309afa2e11afb49c0889841044294cb2b72cda25b'
         '78aac8e0c7fb92f8ea188dfa101e02c0df5ccaaaace6a52ff411be29c9b2d905')

prepare() {
  cd "${pkgname}-${_pkgver}"
  sed -i '731s;<chmod perm="ugo+rx">;<chmod perm="ugo+rx" maxparallel="10">;' build.xml
}

build() {
  cd "${pkgname}-${_pkgver}"
  HDFLIBS=/opt/hdfjava-3.3.2 ant package
}

package() {
  cd "${pkgname}-${_pkgver}"
  mkdir "${pkgdir}/opt"
  cp -a "build/dist/${_pkgname}-${pkgver}-Linux.sh" "${pkgdir}/opt"
  cd "${pkgdir}/opt"

  # Make extraction non interactive
  sed -i 's/interactive=TRUE/interactive=FALSE/' ${_pkgname}-${pkgver}-Linux.sh
  sed -i 's/cpack_skip_license=FALSE/cpack_skip_license=TRUE/' ${_pkgname}-${pkgver}-Linux.sh

  ./${_pkgname}-${pkgver}-Linux.sh
  rm "${_pkgname}-${pkgver}-Linux.sh"
  mkdir -p "${pkgdir}/usr/bin"

  sed -i "s:JAVABIN=${pkgdir}/opt/${_pkgname}/${pkgver}/jre/bin:JAVABIN=/opt/${_pkgname}/${pkgver}/jre/bin:" "${_pkgname}/${pkgver}/${pkgname}.sh"
  sed -i "s:INSTALLDIR=${pkgdir}/opt/${_pkgname}/${pkgver}:INSTALLDIR=/opt/${_pkgname}/${pkgver}:" "${_pkgname}/${pkgver}/${pkgname}.sh"
  cp -a "${_pkgname}/${pkgver}/${pkgname}.sh" "${pkgdir}/usr/bin"

  # Desktop files, icons, wrappers and license
  install -D -m 755 "${srcdir}/${_pkgname}" "${pkgdir}/usr/bin/HDFView"
  install -D -m 644 "${srcdir}/${_pkgname}.desktop" "${pkgdir}/usr/share/applications/${_pkgname}.desktop"
  install -D -m 644 "${srcdir}/${_pkgname}.ico" "${pkgdir}/usr/share/pixmaps/${_pkgname}.ico"
  install -D -m 644 "${srcdir}/license" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
