# Maintainer: gborzi <gborzi@ieee.org>
# Contributor: mickele <mimocciola@yahoo.com>
pkgname=('gmsh' 'gmsh-docs')
pkgver=4.5.5
pkgrel=1
pkgdesc="An automatic 3D finite element mesh generator with pre and post-processing facilities."
arch=('x86_64')
url="http://gmsh.info/"
license=('custom')
makedepends=('cmake' 'desktop-file-utils' 'sed' 'swig' 'fltk' 'lapack'
             'med' 'opencascade' 'cairo' 'texlive-core')
options=(!emptydirs)
source=("${url}src/${pkgname}-${pkgver}-source.tgz" gmsh.desktop gmsh.completion)
sha256sums=('899d3cded664124fa387da57b6f170f47a7e712c7744aa3562779897e2b9e251'
            '43a8ca33ac917ee7196fdae305ff2c8cb9ae1072569ee546c0ce8ff580c966ae'
            '11605e97636a56cf51e445e65019526ee253bd2e0553fb71ba6d94488dcd34ef')

prepare() {
   cd "${srcdir}/${pkgname}-${pkgver}-source"

   # Help links to local doc (package gmsh-docs)
   sed -e "s|http://gmsh.info/doc/texinfo/|file:///usr/share/doc/gmsh/gmsh.html|" \
       -i Fltk/graphicWindow.cpp
   sed -e "s|http://gmsh.info/|file:///usr/share/licenses/gmsh/|" \
       -i Fltk/helpWindow.cpp
   # remove root of build directory from installation
   sed -i '/install(TARGETS shared DESTINATION ${CMAKE_CURRENT_SOURCE_DIR}\/api OPTIONAL)/d' CMakeLists.txt

}

build() {
   cd "${srcdir}/${pkgname}-${pkgver}-source"

   mkdir -p build

   cd build

   cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DENABLE_BUILD_SHARED=ON \
      -DENABLE_PETSC=FALSE .. 

   make
   LC_ALL=C make doc
}

package_gmsh() {
   depends=('fltk' 'lapack' 'med' 'opencascade' 'cairo')
   optdepends=('gmsh-docs: docs for gmsh'
            'python2: for onelab.py'
            'python: for onelab.py')

   cd "${srcdir}/${pkgname}-${pkgver}-source/build"
   make DESTDIR=${pkgdir} install
   install -D -m644 "${pkgdir}/usr/lib/gmsh.py" "${pkgdir}/usr/lib/python2.7/site-packages/gmsh.py"
   install -D -m644 "${pkgdir}/usr/lib/gmsh.py" "${pkgdir}/usr/lib/python3.8/site-packages/gmsh.py"
   rm "${pkgdir}/usr/lib/gmsh.py"

   install -d "${pkgdir}/usr/share/pixmaps/${pkgname}"
   install -m644 ../utils/icons/*.png "${pkgdir}/usr/share/pixmaps/${pkgname}"
   install -D -m644 ../utils/icons/solid_32x32.png "${pkgdir}/usr/share/icons/${pkgname}.png"

   desktop-file-install --dir="${pkgdir}/usr/share/applications" \
    	"${srcdir}/${pkgname}.desktop"

   install -D -m 644 "../LICENSE.txt" "${pkgdir}/usr/share/licenses/$pkgname/LICENSE.txt"
   install -D -m 644 "../CREDITS.txt" "${pkgdir}/usr/share/licenses/$pkgname/CREDITS.txt"
   install -D -m644 $srcdir/gmsh.completion $pkgdir/etc/bash_completion.d/gmsh

   rm -rf ${pkgdir}/usr/share/doc
}

package_gmsh-docs() {
   pkgdesc="TXT, HMTL and PDF doc for Gmsh"
   arch=('any')
   license=('GPL2')

   cd "${srcdir}/${pkgbase}-${pkgver}-source/build"

   bsdtar -xf ${pkgbase}-${pkgver}-*.tgz

   cd "doc/texinfo"

   install -D -m644 gmsh.html "${pkgdir}/usr/share/doc/gmsh/gmsh.html"
   install -D -m644 gmsh.txt "${pkgdir}/usr/share/doc/gmsh/gmsh.txt"
   install -D -m644 gmsh.pdf "${pkgdir}/usr/share/doc/gmsh/gmsh.pdf"
   install -D -m644 gmsh.info "${pkgdir}/usr/share/info/gmsh.info"
}
