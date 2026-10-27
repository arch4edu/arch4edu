# Maintainer: Jingbei Li <i@jingbei.li>

pkgname=pypy-bin
pkgver=8.0.1
pkgrel=1
pkgdesc="A Python implementation written in Python, JIT enabled"
url="https://pypy.org"
arch=('x86_64' 'aarch64')
depends=('bzip2' 'openssl' 'zlib')
provides=('pypy')
conflicts=('pypy')
options=(!buildflags)
license=('MIT')
source_x86_64=("https://downloads.python.org/pypy/pypy2.7-v${pkgver}-linux64.tar.gz")
source_aarch64=("https://downloads.python.org/pypy/pypy2.7-v${pkgver}-aarch64.tar.gz")
sha512sums_x86_64=('c3a20f5ab8c140cd7b0edf77afeb56b3f395d995244abc029755c561d80a31d6a3313c620a6bf223301fef789f85c2b6afc078c5e35e1cc8fe82f52fc8953476')
sha512sums_aarch64=('d42f90401e04b3f1b8f99e9a6cb3de6250f8b537719891d845e01be0628107113a7e25613829fe82f8caf421503f61c92356ab934fb823b8c4bf1cd77a3d5237')

package() {
  [ "$CARCH" = "x86_64" ] && cd pypy2.7-v${pkgver}-linux64
  [ "$CARCH" = "aarch64" ] && cd pypy2.7-v${pkgver}-aarch64

  # Fix permissions
  find . -type d -exec chmod +rx {} \;
  find . -name '*.so*' -exec chmod +rx {} \;

  # Install pypy
  mkdir -p "${pkgdir}"/opt/pypy/
  cp -r * "${pkgdir}"/opt/pypy/

  # Install symlink
  mkdir -p "${pkgdir}"/usr/bin "${pkgdir}"/usr/lib
  ln -s /opt/pypy/bin/pypy "${pkgdir}"/usr/bin/pypy
  ln -s /opt/pypy/bin/libpypy-c.so "${pkgdir}"/usr/lib/libpypy-c.so

  # Install misc stuff
  install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/pypy/LICENSE
}
# vim: ts=2 sw=2 et:
