# Maintainer: Sylvain POULAIN <sylvain dot poulain at giscan dot com>
# Contributor: Doug Newgard <scimmia at archlinux dot org>
# Contributor: Maciej Sieczka <msieczka at sieczka dot org>

pkgname=grass
pkgver=8.5.0
pkgrel=2
_shortver=${pkgver%.*}; _shortver=${_shortver/./}
pkgdesc='Geospatial data management and analysis, image processing, graphics/maps production, spatial modeling and visualization'
arch=('i686' 'x86_64')
url='http://grass.osgeo.org/'
license=('GPL')
depends=('bzip2' 'cairo' 'fftw' 'fontconfig' 'freetype2' 'gcc-libs' 'gdal' 'geos' 'glibc' 'glu'
         'libpng' 'libsvm' 'libtiff' 'libx11' 'libgl' 'netcdf' 'openblas' 'pdal' 'proj'
         'python-gdal' 'python-numpy' 'python-pillow' 'python-wxpython' 'readline' 'zlib' 'zstd')
makedepends=('libxt' 'postgresql-libs')
optdepends=('postgresql: PostgreSQL database interface'
            'sqlite: SQLite database interface')
source=("$pkgname-$pkgver.tar.gz::https://github.com/OSGeo/$pkgname/archive/refs/tags/$pkgver.tar.gz"
        "wxgui.py::https://raw.githubusercontent.com/kikislater/grass/85ffbe3cefc63fb3ca813f254d5e958aa40d9d6e/gui/wxpython/wxgui.py"
)
sha256sums=('c40cb6e741e92a253a44ddd38c7b665d0b44726495f0b8422ef205c0d33ca998'
            'c0db1bb0c5193ff8ddb74932690e39c72d63a1098594f1f7640cd3197d320135')

build() {
  cd $pkgname-$pkgver

  export CXXFLAGS="${CXXFLAGS} -std=c++17"

  ./configure \
    --prefix=/opt/$pkgname \
    --enable-largefile \
    --with-blas \
    --with-bzlib \
    --with-cairo \
    --with-cxx \
    --with-fftw \
    --with-freetype \
    --with-freetype-includes=/usr/include/freetype2 \
    --with-geos \
    --with-lapack \
    --with-libsvm \
    --with-netcdf \
    --with-openmp \
    --with-pcre \
    --with-pdal=/usr/include/pdal \
    --with-proj-share=/usr/share/proj \
    --with-pthread \
    --with-readline \
    --with-sqlite \
    --with-tiff \
    --with-nls \
    --with-opengl \
    --with-x \
    --with-postgres \
    --with-wxwidgets \
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

  # Replace wxGUI.py fix messages in console. Temporary fix until PR 7373 merge
  cp "$srcdir/wxgui.py" "$pkgdir/opt/$pkgname/gui/wxpython/wxgui.py"

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
