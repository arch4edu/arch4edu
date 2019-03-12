# Maintainer: Lara Maia <dev@lara.click>
# Co-maintainer: Fernando Manfredi <contact at acidhub.click>


pkgname=python-wiringpi-git
pkgver=126.4ca39a6
pkgrel=1
pkgdesc="Python-wrapped version of Gordon Henderson's WiringPI."
url="https://github.com/WiringPi/WiringPi-Python"
arch=('x86_64' 'i686' 'armv6h' 'armv7h' 'armv8h')
license=('GPLv3')
depends=('python')
makedepends=('git' 'python-setuptools' 'swig')
replaces=('python-wiringpi2-git')
conflicts=('python-wiringpi')
provides=('python-wiringpi')
source=(git+https://github.com/WiringPi/WiringPi-Python.git)
sha256sums=('SKIP')

pkgver() {
    cd "$srcdir"/WiringPi-Python
    echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

prepare() {
    cd "$srcdir"/WiringPi-Python
    git submodule init
    git submodule update
    swig -python wiringpi.i
}

build() {
    cd "$srcdir"/WiringPi-Python
    python setup.py build
}

package() {
    cd "$srcdir"/WiringPi-Python
    python setup.py install --prefix=/usr --root=$pkgdir
}

