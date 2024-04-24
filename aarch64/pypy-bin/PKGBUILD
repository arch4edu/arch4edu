# Maintainer: Jingbei Li <i@jingbei.li>

pkgname=pypy-bin
pkgver=7.3.16
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
sha512sums_x86_64=('49bc3abe383704516bc9ca92d9b9529bd1b4325543bad027d2d565770d3f5135fea347dd5eb426dfc7aa51182cb78ab9f43bf9137fdf4e7d9235a86249aafc29')
sha512sums_aarch64=('1ad3395d981936c3f4726a02464190ac89261378d361b37bd55b634f1a418e7f8f0a555fd2d7ead3dcdfca5192325397be3094bd9d6d6d4dd498c3901d6e5549')

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
