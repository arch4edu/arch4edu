# Maintainer: Miguel de Val-Borro <miguel dot deval at gmail dot com>
# Contributor: James Tappin <jtappinatgmaildotcom>
# Contributor: Gergely Imreh <imrehgATgmailDOTcom>
# Contributor: Eric Belanger <eric@archlinux.org>
pkgname=plplot
pkgver=5.15.0
pkgrel=4
pkgdesc="A cross-platform software package for creating scientific plots"
arch=('i686' 'x86_64')
url="http://plplot.sourceforge.net/"
license=("LGPL" "custom")
depends=('libtool' 'tk')
makedepends=('cmake')
optdepends=('qhull: calculating convex hulls'
            'agg: high quality rendering engine in C++'
            'swig: connects Plplot C library to Python, Java and Lua (must be present at compile time for Java)'
            'gd: ability to output png, jpeg and gif files'
            'qt4: display plots, output various formats  using the Qt UI framework'
            'wxgtk: displays plots using wxWidgets library'
            'freetype2: enables use of ttf fonts for some drivers'
            'ttf-freefont: enables use of ttf fonts for some drivers'
            'cairo: displays plots and save to different file formats')
options=('!libtool' '!makeflags')
source=(http://downloads.sourceforge.net/sourceforge/plplot/${pkgname}-${pkgver}.tar.gz plplot.patch)
md5sums=('36aec5bfadc2e207cf8ee39f573c9303'
         '16ed4043306ce791e28ef80a80c1fbfd')

prepare() {
    cd "$pkgname-$pkgver"
    patch --forward --strip=1 --input="${srcdir}/plplot.patch"
}

build() {
  cd ${srcdir}/${pkgname}-${pkgver}
  if [ -d build ]; then
      rm -r build
  fi
  mkdir build
  cd build
  cmake -DCMAKE_INSTALL_PREFIX=/usr \
      -DENABLE_octave=off \
      -DENABLE_tcl=ON \
      -DENABLE_tk=ON \
      -DPL_FREETYPE_FONT_PATH=/usr/share/fonts/TTF ..
  find . -name '*.make' -exec sed -i 's|-isystem /usr/include ||g' '{}' ';'
  make 
}

package() {
    cd ${srcdir}/${pkgname}-${pkgver}/build
    make DESTDIR=${pkgdir} install
    install -D -m644 ../Copyright ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE
}
