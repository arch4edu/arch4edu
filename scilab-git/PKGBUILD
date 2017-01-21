# Maintainer: Victor Dmitriyev <mrvvitek@gmail.com>

_pkgname=scilab
pkgname=scilab-git
pkgver=6.0.0.beta.2.r240.g7703c347
pkgrel=1
pkgdesc='A scientific software package for numerical computations'
arch=('i686' 'x86_64')
url="https://www.scilab.org/"
license=('custom:CeCILL' 'BSD')
makedepends=('apache-ant' 'git' 'ocaml' 'java-environment>=8' 'gcc-fortran')
depends=('suitesparse>=4.4.1'  'arpack' 'fftw' 'eigen'
         'libmatio' 'tk' 'curl'
         'hdf5'
         'java-runtime>=8'
         'beanshell' 'eclipse-ecj' 'java-flexdock>=1.2.4' 'fop-hyph'
         'jeuclid-core' 'jgraphx>=2.0.0.1' 'javahelp2'
         'saxon-he' 'jlatexmath-fop>=1.0.3' 'jrosetta>=1.0.4' 'jgoodies-looks' 'java-qdox'
         'java-skinlf' 'java-testng' 'xalan-java' 'docbook-xsl'
         'jogl>=2.3.2' 'java-batik>=1.8')
provides=('scilab')
conflicts=('scilab')
source=("git://git.scilab.org/scilab"
        "${pkgname}_strict-jar.patch"
        "${pkgname}_jogl.patch::http://gitweb.scilab.org/?p=scilab.git;a=patch;h=db79126ed25fc254e83f8a96b164cb2dbf0d6204"
        "${pkgname}-hdf5-1.8.10.patch"
        "${pkgname}_LD_LIBRARY_PATH.patch"
        "${pkgname}_java-default-dir.patch")
sha256sums=('SKIP'
            '38aa094951338fa1d267dc6f397552e175213b0f8ba7b35727c178607861f6dd'
            '7777f0e5fedb3f71f8869a20c448f139501caab17537786db37b999d5c76e618'
            '87e4c7b182755cf557a370820d880aaacfb4be2d3be6255f533668d8e677fd31'
            '37f649fea0196b255e5a8576dd1e8c5fd219c6e8c600b703b35303fb90b6a7e0'
            'a2eb7888bf52862fdba300e113667ad4d3f95512dbf1a99b661eb54b68038948')

pkgver() {
  cd "${srcdir}/${_pkgname}/${_pkgname}"

  git describe --long --tags --always | sed -r 's/([^-]*-g)/r\1/;s/-/./g'
}

prepare(){
  cd "${srcdir}/${_pkgname}/${_pkgname}"

  # https://codereview.scilab.org/#/c/17530/
  patch -p2 < "${srcdir}"/${pkgname}_jogl.patch
  # Linked to: https://codereview.scilab.org/#/c/18089/
  patch < "${srcdir}"/${pkgname}_strict-jar.patch
  # Fix path for Java
  patch -p1 < "${srcdir}"/${pkgname}_java-default-dir.patch
  # http://bugzilla.scilab.org/show_bug.cgi?id=14539
  patch -p1 < "${srcdir}"/${pkgname}-hdf5-1.8.10.patch
  # Fix for LD_LIBRARY_PATH
  patch bin/scilab "${srcdir}"/${pkgname}_LD_LIBRARY_PATH.patch
}

build() {
  cd "${srcdir}/${_pkgname}/${_pkgname}"

  ./configure \
    --prefix=/usr \
    --with-gcc \
    --with-gfortran \
    --with-jdk=/usr/lib/jvm/java-8-openjdk \
    --with-mpi \
    --with-matio \
    --with-umfpack \
    --with-fftw \
    --without-modelica \
    --without-emf \
    --with-install-help-xml \
    --enable-build-help \
    --enable-build-localization \
    --disable-static-system-lib

  make
  make doc
}

package() {
  cd "${srcdir}/${_pkgname}/${_pkgname}"

  make DESTDIR="${pkgdir}" install

  install -Dm644 "${srcdir}/${_pkgname}/${_pkgname}/COPYING" \
    "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
  install -Dm644 "${srcdir}/${_pkgname}/${_pkgname}/COPYING-BSD" \
    "${pkgdir}/usr/share/licenses/${pkgname}/COPYING-BSD"
}

# vim:set ts=2 sw=2 et:
