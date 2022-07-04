# Maintainer: Renato Caldas <renato@calgera.com>
pkgname=ros2-pyqt5-sip-compat
pkgver=0.2
pkgrel=1
pkgdesc="pyqt5-sip compatibility symlinks for building ros2"
arch=('any')
license=('MIT')
depends=(
    'python-pyqt5'
)

package() {
    mkdir -p $pkgdir/usr/share/sip/PyQt5
    ln -s /usr/lib/python3.10/site-packages/PyQt5/* $pkgdir/usr/share/sip/PyQt5
    ln -s /usr/lib/python3.10/site-packages/PyQt5/bindings/* $pkgdir/usr/share/sip/PyQt5/.
}
