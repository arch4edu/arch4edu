# Maintainer: Martin Diehl <aur@martin-diehl.net>

pkgver=0.10.0
pkgrel=2
pkgname=python-scooby
_name=${pkgname#python-}
pkgdesc='A Great Dane turned Python environment detective'
arch=('any')
url='https://github.com/banesullivan/scooby'
license=('MIT')
depends=('python')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools-scm')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha512sums=('c4c7def08dd95697f7ba0c0ea0020cb568fed0c5c359d1f67f71af09d7d05881c7fee9e5e3126e6a5dee98d108f33c8eb685ccb11ed6d93e1c7d85a082a9dd11')

build() {
    cd "$_name-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$_name-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
}
