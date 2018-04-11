# Maintainer: Florian Pritz <bluewind@xinu.at>
# Contributor: Giuseppe Borzi <gborzi@ieee.org>
# Contributor: Brice M<E9>alier <mealier_brice@yahoo.fr>
# Contributor: Michele Mocciola <mickele>
pkgname=opencascade
pkgver=6.9.1
pkgrel=1
pkgdesc="Open CASCADE Technology, 3D modeling & numerical simulation"
arch=('i686' 'x86_64')
url="http://www.opencascade.org"
license=('custom')
depends=('tk' 'mesa' 'java-runtime' 'libxmu' 'ftgl' 'vtk')
makedepends=('java-environment' cmake)
source=("occt-$pkgver.tar.gz::http://git.dev.opencascade.org/gitweb/?p=occt.git;a=snapshot;h=V${pkgver//\./_};sf=tgz" "env.sh" "opencascade.sh" "opencascade.conf")
md5sums=('ea47e4716791f005e40de09f5c416a87'
         'a96f28ee7f4273ae1771ee033a2a3af3'
         'd9368b8d348ced3ec4462012977552d2'
         '2924ecf57c95d25888f51071fdc72ad0')

build() {
  cd "$srcdir/occt-V${pkgver//\./_}-"*

  sed -i 's#OCCT_INCLUDE_CMAKE_FILE ("adm/cmake/occt_modules")##' CMakeLists.txt
  sed -i 's#OCCT_INCLUDE_CMAKE_FILE ("adm/cmake/occt_toolkits")##' CMakeLists.txt
  sed -i 's#include (adm/cmake/occt_inc_toolkits.cmake)##' CMakeLists.txt

  cmake -DINSTALL_DIR="$pkgdir" .

  # fix for automake 1.13
  #sed -i -e 's/AM_CONFIG_HEADER/AC_CONFIG_HEADERS/' configure.ac
  #./build_configure
  #./configure --disable-debug --enable-production \
    #--with-java-include=/usr/lib/jvm/default/include \
    #--with-vtk-library=/usr/lib/ --with-vtk-include=/usr/include/vtk-6.1/ \
    #--prefix=/opt/$pkgname
  make
}

package() {
  cd "$srcdir/occt-V${pkgver//\./_}-"*

  # no DESTDIR support so use prefix. This has to suffix match the prefix in ./configure
  make prefix="$pkgdir/opt/$pkgname" install
  cp -r src/UnitsAPI/ "${pkgdir}/opt/$pkgname/src"
  install -D -m644 "${srcdir}/opencascade.conf" "${pkgdir}/etc/ld.so.conf.d/opencascade.conf"
  install -D -m 755 "${srcdir}/opencascade.sh" "${pkgdir}/etc/profile.d/opencascade.sh"
  install -m 755 "${srcdir}/env.sh" "${pkgdir}/opt/$pkgname"
  install -dm755 "$pkgdir/usr/share/licenses/$pkgname/"
  install -m644 LICENSE_LGPL_21.txt OCCT_LGPL_EXCEPTION.txt "$pkgdir/usr/share/licenses/$pkgname"
}

# vim:set ts=2 sw=2 et:
