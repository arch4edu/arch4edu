# Maintainer: Martchus <martchus@gmx.net>
# Contributor: éclairevoyant
# Contributor: Marco Pompili <aur AT emarcs DOT org>
# Contributor: Ben Duffield <bavardage AT archlinux.us>
pkgbase=pocketsphinx
pkgname=(pocketsphinx python-pocketsphinx)
pkgver=5.1.1
pkgrel=1
pkgdesc='A small speech recognizer'
arch=('i686' 'x86_64')
url='https://cmusphinx.github.io'
license=('BSD-2-Clause' 'BSD-3-Clause' 'MIT')
depends=('glibc')
makedepends=('cmake' 'cython' 'gst-plugins-base-libs' 'libpulse' 'ninja' 'python-build' 'python-installer' 'python-scikit-build-core' 'python-sounddevice')
source=("$pkgbase-$pkgver.tar.gz::https://github.com/cmusphinx/pocketsphinx/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('e2db414eb66618cd0a98de77507db32517a48f6900b06bfb94c0acc4bef5761d')

prepare() {
  cd $pkgbase-$pkgver

}

build() {
  cd $pkgbase-$pkgver

  cmake -S . -B build -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS=ON -DBUILD_GSTREAMER=ON
  cmake --build build
  python -m build --wheel --no-isolation
}

package_pocketsphinx() {
  cd $pkgbase-$pkgver

  optdepends=('gst-plugins-base-libs: GStreamer plugin')
  DESTDIR="$pkgdir" cmake --install build
  install -D -m644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgbase/"
}
package_python-pocketsphinx() {
  cd $pkgbase-$pkgver
  depends+=('python' 'python-sounddevice')
  python -m installer --destdir=${pkgdir} dist/*.whl
  install -D -m644 LICENSE -t "$pkgdir/usr/share/licenses/python-$pkgbase/"
}
