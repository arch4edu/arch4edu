# Maintainer: acxz <akashpatel2008 at yahoo dot com>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: Yichao Yu <yyc1992@gmail.com>
# Contributor: Douglas Soares de Andrade <douglas@archlinux.org>
# Contributor: riai <riai@bigfoot.com> Ben <ben@benmazer.net>
# Contributor: Homalozoa Xu <nx.tardis@gmail.com>

pkgname=('python-pyqt5-sip4')
pkgdesc="A set of Python bindings for the Qt5 toolkit"
pkgver=5.15.10
pkgrel=1
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv6h')
url="https://riverbankcomputing.com/software/pyqt/intro"
license=('GPL')
depends=('python-pyqt5-sip' 'qt5-base')
optdepends=('python-opengl: enable OpenGL 3D graphics in PyQt applications'
            'python-dbus: for python-dbus mainloop support'
            'qt5-multimedia: QtMultimedia, QtMultimediaWidgets'
            'qt5-tools: QtHelp, QtDesigner'
            'qt5-svg: QtSvg'
            'qt5-xmlpatterns: QtXmlPatterns'
            'qt5-declarative: QtQml, qmlplugin'
            'qt5-serialport: QtSerialPort'
            'qt5-websockets: QtWebSockets'
            'qt5-connectivity: QtNfc, QtBluetooth'
            'qt5-x11extras: QtX11Extras'
            'qt5-remoteobjects: QtRemoteObjects'
            'qt5-speech: QtTextToSpeech'
            'qt5-quick3d: QtQuick3D'
            'qt5-location: QtLocation, QtPositioning'
            'qt5-sensors: QtSensors'
            'qt5-webchannel: QtWebChannel')
provides=(qt5-python-bindings python-pyqt5)
makedepends=('sip' 'pyqt-builder' 'python-opengl' 'python-dbus'
             'qt5-connectivity' 'qt5-multimedia' 'qt5-tools' 'qt5-serialport' 'qt5-speech' 'qt5-svg'
             'qt5-websockets' 'qt5-x11extras' 'qt5-xmlpatterns' 'qt5-remoteobjects' 'qt5-quick3d'
             'qt5-sensors' 'qt5-webchannel' 'qt5-location')
conflicts=('pyqt5-common' 'python-pyqt5')
source=("https://pypi.python.org/packages/source/P/PyQt5/PyQt5-$pkgver.tar.gz"
         restore-sip4-support.patch)
sha256sums=('d46b7804b1b10a4ff91753f8113e5b5580d2b4462f3226288e2d84497334898a'
            'c8881a8dc666e509773f93330615d310f9f040c2167dc9e98843741691395f72')

prepare() {
  patch -d PyQt5-$pkgver -p1 < restore-sip4-support.patch # https://www.riverbankcomputing.com/pipermail/pyqt/2021-November/044346.html
}

build() {
  cd PyQt5-$pkgver
  sip-build \
    --confirm-license \
    --no-make \
    --api-dir /usr/share/qt/qsci/api/python \
    --pep484-pyi
  cd build
  make
}

package() {
  cd PyQt5-$pkgver/build
  make INSTALL_ROOT="$pkgdir" install

  # Remove unused py2 version of uic modules:
  rm -r "$pkgdir"/usr/lib/python*/site-packages/PyQt5/uic/port_v2

  # compile Python bytecode
  python -m compileall -d / "$pkgdir"/usr/lib
  python -O -m compileall -d / "$pkgdir"/usr/lib
}
