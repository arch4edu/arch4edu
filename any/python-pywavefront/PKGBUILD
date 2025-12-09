# Maintainer: Felipe Bartelt <fbartelt at ufmg dot br>
pkgname='python-pywavefront'
_name=${pkgname#python-}
_capsname='PyWavefront'
pkgver=1.3.3
pkgrel=1
pkgdesc="Python library for importing Wavefront .obj files"
arch=('any')
url="https://github.com/pywavefront/PyWavefront"
license=('BSD-3-Clause')
depends=('python>=3.4' )
makedepends=(python-build python-installer python-wheel)
source=("https://files.pythonhosted.org/packages/py3/${_name::1}/$_name/$_capsname-$pkgver-py3-none-any.whl")
sha256sums=('ec79cadd046b168434b01031e574f4105f821d06cb8cf754801e4dc18076bbeb')

#build() {
#    cd $_name
#    python -m build --wheel --no-isolation
#}

package() {
    #cd $_name-$pkgver
    python -m installer --destdir="$pkgdir" *.whl
    install -Dm644 "${_capsname}-${pkgver}.dist-info/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
