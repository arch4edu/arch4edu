# Maintainer: Sylvain POULAIN <sylvain dot poulain at giscan dot com>
# Contributor: Doug Newgard <scimmia at archlinux dot org>
# Contributor: Maciej Sieczka <msieczka at sieczka dot org>

pkgname=grass
pkgver=8.3.0
pkgrel=1
_shortver=${pkgver%.*}; _shortver=${_shortver/./}
pkgdesc='Geospatial data management and analysis, image processing, graphics/maps production, spatial modeling and visualization'
arch=('i686' 'x86_64')
url='http://grass.osgeo.org/'
license=('GPL')
depends=('bzip2' 'cairo' 'fftw' 'fontconfig' 'freetype2' 'gcc-libs' 'gdal' 'geos' 'glibc' 'glu'
         'libpng' 'libtiff' 'libx11' 'libgl' 'netcdf' 'pdal' 'proj' 'python-gdal' 'python-numpy'
         'python-pillow' 'python-wxpython' 'readline' 'zlib' 'zstd')
makedepends=('libxt' 'postgresql-libs')
optdepends=('postgresql: PostgreSQL database interface'
            'sqlite: SQLite database interface')
source=("http://grass.osgeo.org/grass$_shortver/source/$pkgname-$pkgver.tar.gz")
b2sums=('dc918958333387356ec655c0f12f18654522976ab0b942fb1751fca5b49d4d06a7ec63f83e890b75f7c509ba128da58587e532554ba99d59b6cefd6bbf111415')

build() {
  cd $pkgname-$pkgver

  # Ancient autoconf used upstream can't handle CPPFLAGS correctly, so set CPP to ignore warnings
  CPP="gcc -E -w" \
  ./configure \
    --prefix=/opt/$pkgname \
    --with-freetype-includes=/usr/include/freetype2 \
    --with-wxwidgets \
    --with-readline \
    --with-pthread \
    --with-netcdf \
    --with-nls \
    --with-geos \
    --with-postgres \
    --with-pdal \
    --with-bzlib \
    --with-zstd

  LC_ALL=C
  make
}

package() {
  cd $pkgname-$pkgver

  make exec_prefix="$pkgdir/usr" INST_DIR="$pkgdir/opt/$pkgname" install

  # Install linker config file, needed for qgis to find grass
  install -d "$pkgdir/etc/ld.so.conf.d/"
  echo "/opt/$pkgname/lib" > "$pkgdir/etc/ld.so.conf.d/$pkgname.conf"

  cd "$pkgdir/opt/$pkgname"

  # Put freedesktop.org files in correct location
  mv share "$pkgdir/usr"

  # Fix some paths that get hard coded by make install
  sed -i "s|$pkgdir||g" demolocation/.grassrc$_shortver \
                        include/Make/{Platform,Grass}.make \
                        etc/fontcap \
                        "$pkgdir/usr/bin/grass"

  # Get python lib path
  pylib=$(python -c "import sys; print(sys.path[-1])")
  # Link pygrass to main python site-packages
  mkdir -p "$pkgdir$pylib"
  ln -s "$pkgdir/opt/grass/etc/python/grass" "$pkgdir$pylib"
}
