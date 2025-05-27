# Maintainer: Sven-Hendrik Haase <svenstaro@archlinux.org>

pkgname=pypy3
_pyversion=3.11
pkgver=7.3.19
pkgrel=1
pkgdesc="A Python3 implementation written in Python, JIT enabled"
url="https://pypy.org"
arch=('x86_64')
depends=('expat' 'bzip2' 'gdbm' 'openssl' 'libffi' 'zlib' 'ncurses')
makedepends=('pypy' 'sqlite' 'tk')
optdepends=('sqlite: sqlite module'
            'tk: tk module')
license=('MIT')
source=("https://downloads.python.org/pypy/pypy${_pyversion}-v${pkgver}-src.tar.bz2")
sha512sums=('ab078e81e5eefe16823350bdc9adcc444e0ef6835ff2234197f9e5cb0903c5208deb6df60722e99aa529ffff703c5dcbc08eaa7f753c2e5c1185afea6358395a')

build() {
  cd pypy${_pyversion}-v${pkgver}-src/pypy/goal

  # Workaround for https://github.com/pypy/pypy/issues/5194
  export CFLAGS+=" -Wno-error=incompatible-pointer-types"

  pypy ../../rpython/bin/rpython -Ojit --shared targetpypystandalone

  # Compile binary modules
  PYTHONPATH=../.. ./pypy${_pyversion}-c ../../lib_pypy/pypy_tools/build_cffi_imports.py
}

package() {
  cd pypy${_pyversion}-v${pkgver}-src

  # Prepare installation
  pypy pypy/tool/release/package.py --archive-name pypy --targetdir .
  mkdir unpacked
  tar xf pypy.tar.bz2 -C unpacked

  # Install pypy
  mkdir -p "${pkgdir}"/usr/bin "${pkgdir}"/usr/lib "${pkgdir}"/opt/pypy3
  cp -r unpacked/pypy/* "${pkgdir}"/opt/pypy3

  # Install symlinks
  ln -s /opt/pypy3/bin/pypy3 "${pkgdir}"/usr/bin/pypy3
  ln -s /opt/pypy3/bin/pypy${_pyversion} "${pkgdir}"/usr/bin/pypy${_pyversion}
  ln -s /opt/pypy3/bin/libpypy${_pyversion}-c.so "${pkgdir}"/usr/lib/libpypy${_pyversion}-c.so

  # Install misc stuff
  install -Dm644 README.rst "${pkgdir}"/opt/pypy3/README.rst
  install -Dm644 LICENSE "${pkgdir}"/opt/pypy3/LICENSE
  install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/pypy3/LICENSE
}
# vim: ts=2 sw=2 et:
