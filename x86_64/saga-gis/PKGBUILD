# Maintainer: Justus Spitzmueller <j.spitzmueller at posteo.de>
# Contributor: Luigi Ranghetti <luigi.ranghetti@gmail.com>
# Contributor: Dominik Fuchs <dominik.fuchs@wur.nl>
# Contributor: Marcelo Avalos Tejeda <marcelo.avalos@gmail.com>
# Contributor: Samuel Fernando Mesa Giraldo <samuelmesa@linuxmail.org>
# Contributor: SaultDon <sault.don gmail>

pkgname=saga-gis
_pkgname=saga
pkgver=9.9.1
pkgrel=1
pkgdesc="A Geographic Information System (GIS) software with immense capabilities for geodata processing and analysis."
url="http://www.saga-gis.org"
license=('GPL-2.0-only' 'LGPL-2.0-only')
arch=('i686' 'x86_64')
depends=('wxwidgets-gtk3' 'wxwidgets-common' 'hicolor-icon-theme' 'proj' 'gdal' 'curl' 'libtiff' 'unixodbc' 'opencv' 'pdal' 'arrow')
optdepends=('postgresql' 'vigra' 'liblas' 'libharu' 'libsvm' 'swig' 'python' 'exiv2')
makedepends=('cmake')
source=("https://download.sourceforge.net/saga-gis/saga-${pkgver}.tar.gz") 
sha256sums=('227ca9c950a4d3cb6c07229a2014455a5770473d4090d0a0143dc32f8386f38c')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"

  [[ -d build ]] || mkdir build

  cd "${srcdir}/${_pkgname}-${pkgver}/build"

  cmake -G "Unix Makefiles" ../saga-gis \
  -DCMAKE_INSTALL_PREFIX:PATH=/usr/ \
  -DwxWidgets_CONFIG_EXECUTABLE=/usr/bin/wx-config   \
  -DWITH_CLIPPER_ONE:BOOL=OFF

  cmake --build . --verbose
}


package () {
  cd "${srcdir}/${_pkgname}-${pkgver}/build"

  make DESTDIR="${pkgdir}" install

  install -Dm644 "${srcdir}/${_pkgname}-${pkgver}/${pkgname}/src/saga_core/saga_gui/res/saga.png" \
                   "${pkgdir}/usr/share/pixmaps/${_pkgname}.png"
}
