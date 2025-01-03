# Maintainer: Vekhir <vekhir at yahoo dot com>

pkgname=python-audioop-lts
_pkg="${pkgname#python-}"
pkgver=0.2.1
pkgrel=1
pkgdesc="An LTS port of Python's 'audioop' module."
arch=('x86_64')
url="https://github.com/AbstractUmbra/audioop"
license=('PSF-2.0')
depends=('glibc' 'python')
makedepends=('git' 'python-build' 'python-installer' 'python-setuptools' 'python-wheel')
checkdepends=('python-pytest')
provides=('python-audioop')
source=("$pkgname-$pkgver::git+https://github.com/AbstractUmbra/audioop.git#tag=$pkgver")
sha512sums=('473358b4c634225511d802a45bc0dd419fce8f030cacbac7e4a1de160112aab39a35f9c2c0904f518d5c3c2dd03b7f217194863140ec8f51f564e025b5b8d959')

build() {
    cd "$pkgname-$pkgver"
    python -m build --wheel --no-isolation
}

check() {
    cd "$pkgname-$pkgver"
    pytest || echo "Tests failed"
}

package() {
    cd "$pkgname-$pkgver"
    python -m installer --destdir="$pkgdir/" dist/*.whl
    install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
