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
pkgver=3.44.12
pkgrel=1
pkgdesc='Geographic Information System (GIS); Long Term Release'
arch=(x86_64)
url='https://qgis.org/'
license=(GPL-2.0-or-later)
depends=(
  abseil-cpp
  draco
  exiv2
  expat
  gcc-libs
  gdal
  geos
  glibc
  gsl
  hdf5
  hicolor-icon-theme
# libspatialindex
  libspatialite
  libxml2
  libzip
  netcdf
  ocl-icd
  pdal
  postgresql-libs
  proj
  protobuf
  python
  python-gdal
  python-jinja
  python-numpy
  python-owslib
  python-packaging
  python-psycopg2
  python-pyqt6
  python-qscintilla-qt6
  python-yaml
  qca-qt6
  qscintilla-qt6
  qt6-3d
  qt6-5compat
  qt6-base
  qt6-declarative
  qt6-imageformats
  qt6-multimedia
  qt6-positioning
  qt6-serialport
  qt6-svg
  qt6-tools
  qt6-webengine
  qtkeychain-qt6
  qwt
  sqlite
  zlib
  zstd
)
makedepends=(
  cmake
  fcgi
  ninja
  opencl-clhpp
  pyqt-builder
  sip
)
optdepends=(
  'fcgi: Map server'
  'gpsbabel: GPS Tools plugin'
)
provides=("$_pkgname=$pkgver")
conflicts=("$_pkgname")
source=("$url/downloads/$_pkgname-$pkgver.tar.bz2"
        https://github.com/JanCaha/QGIS/commit/67af3cdf8bfd8c482c718beb1452ac7dc0d3bd0c.patch)
sha256sums=('62547cefa7818e7453e4043e6073797eb1a8886b7a8dfbc4765f57b931404a57'
            '9cc3cc824792d5a3ede3ff499b77c81241a5451952c6e9ae8104c02b37737827')

prepare() {
  cd "$_pkgname-$pkgver"
  patch -p1 -i "$srcdir/67af3cdf8bfd8c482c718beb1452ac7dc0d3bd0c.patch"
}

build() {
  cmake -S $_pkgname-$pkgver -B build -G Ninja \
    -DBUILD_WITH_QT6=ON \
    -DWITH_QTWEBKIT=OFF \
    -DWITH_QTWEBENGINE=ON \
    -DCMAKE_INSTALL_PREFIX='/usr' \
    -DWITH_3D=TRUE \
    -DWITH_QUICK=TRUE \
    -DQGIS_QML_SUBDIR=lib/qt/qml \
    -DWITH_SERVER=TRUE \
    -DWITH_CUSTOM_WIDGETS=TRUE \
    -DBINDINGS_GLOBAL_INSTALL=TRUE \
    -DQGIS_MANUAL_SUBDIR=share/man \
    -DWITH_PDAL=TRUE \
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
