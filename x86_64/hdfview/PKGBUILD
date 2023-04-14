# Maintainer  : Grey Christoforo <first name at last name dot net>

pkgname=hdfview
_pkgname=HDFView
pkgver=3.3.0
pkgrel=1
pkgdesc="A visual tool for browsing and editing HDF4 and HDF5 files."
arch=('x86_64')
url="https://portal.hdfgroup.org/display/HDFVIEW/HDFView"
license=('custom')
depends=(hdf5 java-runtime)
makedepends=(ant gendesk hdf4 inetutils 'java-environment>=15')
optdepends=(hdf4)
source=("https://support.hdfgroup.org/ftp/HDF5/releases/HDF-JAVA/hdfview-${pkgver}/src/hdfview-${pkgver}.tar.gz")
sha256sums=('0916161861c21fa8dd354b445b48eff5a53d80a5c0b383e79eb64b7b108e2430')

#check() {
#  cd "${srcdir}/${pkgname}-${pkgver}"
#
#  export HDFLIBS=/opt/hdf4
#  export HDF5LIBS=/usr
#  ant junit
#}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  export HDFLIBS=/opt/hdf4
  export HDF5LIBS=/usr
  ant createJPackage

  gendesk -n --pkgname "$pkgname" --pkgdesc "$pkgdesc" --name ${_pkgname}
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  mkdir -p "${pkgdir}/opt/"
  mkdir -p "${pkgdir}/usr/bin"

  cp -a build/dist/${_pkgname} "${pkgdir}/opt/${pkgname}"
  ln -s /opt/${pkgname}/bin/${_pkgname} "${pkgdir}/usr/bin/${pkgname}"

  install -Dm644 "$pkgname.desktop" "$pkgdir/usr/share/applications/$pkgname.desktop"
  install -Dm644 "src/HDFView.png" "$pkgdir/usr/share/pixmaps/$pkgname.png"

  install -Dm644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
