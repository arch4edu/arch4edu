# Maintainer: Sven-Hendrik Haase <svenstaro@archlinux.org>

pkgname=pypy3
_pyversion=3.12
pkgver=8.0.1
pkgrel=2
pkgdesc="A Python3 implementation written in Python, JIT enabled"
url="https://pypy.org"
arch=('x86_64')
depends=('expat' 'bzip2' 'gdbm' 'openssl' 'libffi' 'zlib' 'ncurses')
makedepends=('pypy' 'sqlite' 'tk')
optdepends=('sqlite: sqlite module'
            'tk: tk module')
license=('MIT')
source=("https://downloads.python.org/pypy/pypy${_pyversion}-v${pkgver}-src.tar.gz"
        "pypy3-8.0.1-openssl-4.patch::https://github.com/loqs/pypy/compare/5810ee7762f124b272bc17bbc9aaef2655a6ea71...ca3f7fe07b12f9f668cf24bf72f4b6da77f06109.patch")
sha512sums=('bb60f8107079188b9214907c1bdd8d8aebb912cf4beb55f6c8cf80e16029d5e677f18a2f13d3fe3bd11676944e8dca7335a0f52ae1d47dec9b6b4312ac6c1604'
            'c94a1e75e456dd3e44035a3a6512c091891bb3743b9d5af9158afe45167c31d88eede450c6ca8f8c0bd8c5da99601656865739abff2a97e6413c1bfae8ce1c8c')

prepare() {
  cd pypy${_pyversion}-v${pkgver}-src

  # Fix OpenSSL 4 compatibility using the Python 3.12 port of this PR.
  # https://github.com/pypy/pypy/pull/5489
  patch -Np1 -i ../pypy3-8.0.1-openssl-4.patch
}

build() {
  cd pypy${_pyversion}-v${pkgver}-src/pypy/goal

  pypy ../../rpython/bin/rpython -Ojit --shared targetpypystandalone

  # Compile binary modules
  PYTHONPATH=../.. ./pypy${_pyversion}-c ../../lib_pypy/pypy_tools/build_cffi_imports.py
}

package() {
  cd pypy${_pyversion}-v${pkgver}-src

  # Prepare installation
  pypy pypy/tool/release/package.py --archive-name pypy --targetdir .
  mkdir unpacked
  tar xf pypy.tar.gz -C unpacked

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
