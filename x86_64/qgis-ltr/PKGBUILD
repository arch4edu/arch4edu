# Maintainer: Stephan Springer <buzo+arch@Lini.de>
# Contributor: Balló György <ballogyor+arch at gmail dot com>
# Contributor: Bruno Pagani <archange@archlinux.org>
# Contributor: Doug Newgard <scimmia at archlinux dot org>
# Contributor: XavierCLL <xavier.corredor.llano (a) gmail.com>
# Contributor: SaultDon <sault.don gmail>
# Contributor: Lantald < lantald at gmx.com >
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: dibblethewrecker dibblethewrecker.at.jiwe.dot.org
# Contributor: Gerardo Exequiel Pozzi <vmlinuz386@yahoo.com.ar>
# Contributor: Eric Forgeot < http://esclinux.tk >

_pkgname=qgis
pkgname="$_pkgname"-ltr
pkgver=3.40.13
pkgrel=1
pkgdesc='Geographic Information System (GIS); Long Term Release'
arch=(x86_64)
url='https://qgis.org/'
license=('GPL-2.0-or-later')
depends=(ocl-icd proj geos gdal expat #libspatialindex
         qwt libzip sqlite3 protobuf
         zlib exiv2 postgresql-libs libspatialite zstd pdal
         qt5-base qt5-svg qt5-serialport qt5-location qt5-3d qt5-declarative qt5-multimedia
         qscintilla-qt5 qtkeychain-qt5 qca-qt5 gsl python-pyqt5 python-qscintilla-qt5
         hdf5 netcdf libxml2 draco) # laz-perf
makedepends=(cmake ninja opencl-clhpp fcgi qt5-tools sip pyqt-builder)
optdepends=('fcgi: Map server'
            'gpsbabel: GPS Tools plugin')
provides=("$_pkgname=$pkgver")
conflicts=("$_pkgname")
source=("https://qgis.org/downloads/$_pkgname-$pkgver.tar.bz2")
sha256sums=('2934325e873de4c3c9deba131c40eb3edf10f1f04d0016e2177ad2de90949ef0')
# curl -s https://download.qgis.org/downloads/qgis-latest-ltr.tar.bz2.sha256

build() {
  cmake -S $_pkgname-$pkgver -B build -G Ninja \
    -DCMAKE_INSTALL_PREFIX='/usr' \
    -DWITH_3D=TRUE \
    -DWITH_QUICK=TRUE \
    -DWITH_SERVER=TRUE \
    -DWITH_CUSTOM_WIDGETS=TRUE \
    -DBINDINGS_GLOBAL_INSTALL=TRUE \
    -DQGIS_MANUAL_SUBDIR=share/man \
    -DWITH_QTWEBKIT=FALSE \
    -DWITH_QWTPOLAR=TRUE \
    -DQWTPOLAR_LIBRARY=/usr/lib/libqwt.so \
    -DQWTPOLAR_INCLUDE_DIR=/usr/include/qwt \
    -DCMAKE_CXX_FLAGS="${CXXFLAGS} -DQWT_POLAR_VERSION=0x060200" \
    -DWITH_INTERNAL_QWTPOLAR=FALSE \
    -DWITH_PDAL=TRUE \
    -DHAS_KDE_QT5_PDF_TRANSFORM_FIX=TRUE \
    -DHAS_KDE_QT5_SMALL_CAPS_FIX=TRUE \
    -DHAS_KDE_QT5_FONT_STRETCH_FIX=TRUE \
    -DWITH_INTERNAL_SPATIALINDEX=TRUE # https://github.com/libspatialindex/libspatialindex/issues/276
    # https://github.com/qgis/QGIS/issues/48374
    #-DWITH_INTERNAL_LAZPERF=FALSE \
    # https://github.com/qgis/QGIS/issues/35440
    #-DWITH_PY_COMPILE=TRUE \

  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
  install -Dm644 $_pkgname-$pkgver/rpm/sources/qgis-mime.xml "$pkgdir/usr/share/mime/packages/qgis.xml"
}
