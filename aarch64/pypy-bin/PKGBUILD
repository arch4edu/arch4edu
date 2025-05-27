# Maintainer: Jingbei Li <i@jingbei.li>

pkgname=pypy-bin
pkgver=7.3.19
pkgrel=1
pkgdesc="A Python implementation written in Python, JIT enabled"
url="https://pypy.org"
arch=('x86_64' 'aarch64')
depends=('bzip2' 'openssl' 'zlib')
provides=('pypy')
conflicts=('pypy')
options=(!buildflags)
license=('MIT')
source_x86_64=("https://downloads.python.org/pypy/pypy2.7-v${pkgver}-linux64.tar.bz2")
source_aarch64=("https://downloads.python.org/pypy/pypy2.7-v${pkgver}-aarch64.tar.bz2")
sha512sums_x86_64=('ad63b59b776bc741e68fe6f9538f8d3c584a0f79a41fd63ad09264559d4c454b8be6628be50325f1a32a1979ec3213964f0b079bc0d69e4e15c03bf834c7186f')
sha512sums_aarch64=('2e98d2265f4fc6a3da7c000698edc64dd85395522e2c61a43fe3ef66064d49d6e3f6a8322e94c99d94b28a7b15cff5df82570f02ec82471d4d534400464b6bb3')

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
