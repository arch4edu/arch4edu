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
pkgver=3.28.13
pkgrel=1
pkgdesc='Geographic Information System (GIS); Long Term Release'
arch=(x86_64)
url='https://qgis.org/'
license=(GPL)
depends=(ocl-icd proj geos gdal expat spatialindex qwt libzip sqlite3 protobuf
         zlib exiv2 postgresql-libs libspatialite zstd
         qt5-base qt5-svg qt5-serialport qt5-location qt5-3d qt5-declarative
         qscintilla-qt5 qtkeychain-qt5 qca-qt5 gsl python-pyqt5 python-qscintilla-qt5
         hdf5 netcdf libxml2) # laz-perf
makedepends=(cmake ninja opencl-clhpp fcgi qt5-tools)
optdepends=('fcgi: Map server'
            'gpsbabel: GPS Tools plugin')
provides=("$_pkgname=$pkgver")
conflicts=("$_pkgname")
source=("https://download.qgis.org/downloads/$_pkgname-$pkgver.tar.bz2"
        protobuf-23.patch
        exiv2-0.28.patch)
sha256sums=('f9bf9b56b930fc530ad4ec131ba36d324f07dac4428d6330d3e52c0914145c2a'
            'ac6c96e88346c1cec739b1e628afb02aef1895c0d09213269bad75b1a8cee617'
            'b8f7181211263866829531d239e07ab7400d18b9afde70a8ced23f602dfb5c2f')
# curl https://download.qgis.org/downloads/qgis-latest-ltr.tar.bz2.sha256

prepare () {
  cd "$_pkgname-$pkgver"
  patch -p1 -i ../protobuf-23.patch
  patch -p1 -i ../exiv2-0.28.patch
}

build() {
  cmake -G Ninja -B build -S "$_pkgname-$pkgver" \
    -DCMAKE_INSTALL_PREFIX=/usr \
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
    -DWITH_PDAL=FALSE \
    -DWITH_BINDINGS=FALSE \
    -DHAS_KDE_QT5_PDF_TRANSFORM_FIX=TRUE \
    -DHAS_KDE_QT5_SMALL_CAPS_FIX=TRUE \
    -DHAS_KDE_QT5_FONT_STRETCH_FIX=TRUE
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
