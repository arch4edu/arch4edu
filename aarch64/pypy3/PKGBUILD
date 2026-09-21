# Maintainer: Sven-Hendrik Haase <svenstaro@archlinux.org>

pkgname=pypy3
_pyversion=3.12
pkgver=8.0.0
pkgrel=1
pkgdesc="A Python3 implementation written in Python, JIT enabled"
url="https://pypy.org"
arch=('x86_64')
depends=('expat' 'bzip2' 'gdbm' 'openssl' 'libffi' 'zlib' 'ncurses')
makedepends=('pypy' 'sqlite' 'tk')
optdepends=('sqlite: sqlite module'
            'tk: tk module')
license=('MIT')
source=("https://downloads.python.org/pypy/pypy${_pyversion}-v${pkgver}-src.tar.gz"
        fix-cffi-verify-chdir-relative-source-paths.patch)
sha512sums=('7eb576fdec8d46e5889dd265951ad49985c7d25ff1f998be83d8f34a011bd2369e00f1e48f93767bcb503b92849d549ce41c97338d65708da42b9833aefb8a2f'
            '7ff8002b51d8d405c752c3ce5ec29f560350f2e9a389bf2283d18380162807dbb6d4561296b8a29e7738b573b8cf7ae81cdfcd57f61e3730dbe9c089e8f7a8a5')

prepare() {
  cd pypy${_pyversion}-v${pkgver}-src

  patch -p1 -i ../fix-cffi-verify-chdir-relative-source-paths.patch
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
