# Maintainer: Martin Diehl <aur@martin-diehl.net>

pkgver=0.9.2
pkgrel=1
pkgname=python-scooby
_name=${pkgname#python-}
pkgdesc='A Great Dane turned Python environment detective'
arch=('any')
url='https://github.com/banesullivan/scooby'
license=('MIT')
depends=('python')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools-scm')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha512sums=('901655c468c1338a38ec3139515b517ec7e89892e209b9966b5274ae073e61152fa9fc5a7526cf3c2a05bdfe3148d4576b77d27cd6c1d043c29924692097a596')

build() {
    cd "$_name-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$_name-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
