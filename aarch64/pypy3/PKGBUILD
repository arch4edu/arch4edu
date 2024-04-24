# Maintainer: Sven-Hendrik Haase <svenstaro@archlinux.org>

pkgname=pypy3
_pyversion=3.10
pkgver=7.3.16
pkgrel=1
pkgdesc="A Python3 implementation written in Python, JIT enabled"
url="https://pypy.org"
arch=('x86_64')
depends=('expat' 'bzip2' 'gdbm' 'openssl' 'libffi' 'zlib' 'ncurses')
makedepends=('pypy' 'sqlite' 'tk')
optdepends=('sqlite: sqlite module'
            'tk: tk module')
options=(!buildflags)
license=('MIT')
source=("https://downloads.python.org/pypy/pypy${_pyversion}-v${pkgver}-src.zip")
sha512sums=('48777b2748f67939377485b1e112d43b4c9b884d8159b140c428abc4a4de854f5175bc3425c6761f2adb95b0b3c3b429672764ce425275a36769e4709841f80f')

build() {
  cd pypy${_pyversion}-v${pkgver}-src/pypy/goal

  # For some reason, PyPy wants to use their vendored dependencies when detecting linux.
  # Weird, we'll patch it out.
  sed -i "s/, 'linux', 'linux2'//" targetpypystandalone.py
  pypy ../../rpython/bin/rpython -Ojit --shared targetpypystandalone

  # Compile binary modules
  PYTHONPATH=../.. ./pypy3.10-c ../../lib_pypy/pypy_tools/build_cffi_imports.py
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
