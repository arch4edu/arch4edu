# Maintainer: Duck
# Contributor: Alexander F. Rødseth <xyproto@archlinux.org>
# Contributor: Andreas Radke <andyrtr@archlinux.org>
# Contributor: Stéphane Gaudreault <stephane@archlinux.org>
# Contributor: SleepyDog

_pkgbase=glew
pkgname=glew-egl-glx
pkgver=2.2.0
pkgrel=1
pkgdesc="The OpenGL Extension Wrangler Library"
arch=('aarch64' 'armv7h' 'pentium4' 'x86_64')
url="http://glew.sourceforge.net" # no https available
license=('BSD' 'MIT' 'GPL')
depends=('glibc' 'libegl' 'libgl')
optdepends=('libx11: for glxewinfo and visualinfo')
conflicts=('glew' 'glew-wayland')
provides=('glew')
source=(https://downloads.sourceforge.net/${_pkgbase}/${_pkgbase}-${pkgver}.tgz
        egl+glx.patch)
sha256sums=('d4fc82893cfb00109578d0a1a2337fb8ca335b3ceccf97b97e5cc7f08e4353e1'
            '206dc53e185aa2bd64b21107dcaafccb3207a8185ccd1c02a87ed9783c25cc61')

prepare() {
  cd ${_pkgbase}-${pkgver}

  sed -i 's|lib64|lib|' config/Makefile.linux
  sed -i '/^.PHONY: .*\.pc$/d' Makefile

  patch -p1 <"${srcdir}/egl+glx.patch"
}

build() {
  cd ${_pkgbase}-${pkgver}

  make STRIP= glew.bin
  mv bin/glewinfo bin/glxewinfo
  rm glew.pc
  make STRIP= SYSTEM=linux-egl glew.lib.shared bin/glewinfo
  mv bin/glewinfo bin/eglewinfo
}

package() {
  cd ${_pkgbase}-${pkgver}
  make GLEW_DEST="${pkgdir}/usr" STRIP= SYSTEM=linux-egl install
  install -D -m755 -t "${pkgdir}/usr/bin" bin/eglewinfo bin/glxewinfo bin/visualinfo
  rm ${pkgdir}/usr/include/GL/wglew.h
  install -m644 include/GL/eglew.h ${pkgdir}/usr/include/GL
  ln -s eglewinfo "${pkgdir}/usr/bin/glewinfo"
  install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
