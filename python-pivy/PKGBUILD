pkgname=python-pivy
_module='pivy'
pkgver=0.6.4
_RC="0.6.5a0"
pkgrel=1
pkgdesc="A Python binding for Coin"
url="http://pivy.coin3d.org/"
depends=('python' 'coin' 'python')
makedepends=('python-setuptools')
license=('BSD')
arch=('any')
source=("https://github.com/FreeCAD/pivy/archive/${_RC}.tar.gz")
md5sums=('63efa3bd078868c25a5efbd0c7707efd')

prepare() {
    cd "$srcdir/${_module}-${_RC}/fake_headers"
    touch cstddef cstdarg cassert
}

build() {
    cd "${srcdir}/${_module}-${_RC}"
    python setup.py build
}

package() {
    depends+=()
    cd "${srcdir}/${_module}-${_RC}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
