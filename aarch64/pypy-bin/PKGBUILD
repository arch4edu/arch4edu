# Maintainer: Jingbei Li <i@jingbei.li>

pkgname=pypy-bin
pkgver=7.3.14
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
sha512sums_x86_64=('0aebd1fc0c3e61582559e9ed383d311511fb4bf2f20bf20a388040c85f611de0366d1dd4a6290b039872a16fec684c134fea1d4c5ec5741f74a2fa3c0e39be42')
sha512sums_aarch64=('d15e6157b40c0830ca7373a6c64432dadaf2170731e9bd15b08fb53496891f4b77fc0709d974629a6b5ff7be064677e2188be09c7f692ce334a7e02adbdd3fda')

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
