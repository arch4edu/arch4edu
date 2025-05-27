# Maintainer: acxz <akashpatel2008@yahoo.com>
# Contributor: Tong Chunli<t.cunly at 163 dot com>

pkgname=python-colcon-core
pkgver=0.19.0
pkgrel=1
pkgdesc="Command line tool to build sets of software packages."
arch=(any)
url="https://colcon.readthedocs.io/en/released/"
license=('Apache')
depends=(
    python-pytest
    python-pytest-runner
    python-pytest-rerunfailures
    python-pytest-repeat
    python-coverage
    python-pytest-cov
    python-distlib
    python-notify2
    python-empy3
)
makedepends=(
    python-setuptools
    python-build
    python-installer
    python-wheel
)
source=("$pkgname-$pkgver.tar.gz"::"https://github.com/colcon/colcon-core/archive/$pkgver.tar.gz")
sha256sums=('005e5c3260e03c3118fe96a12b08e443947382fd376a97389c630064c1a6b5fc')

_pkgname=colcon-core

build() {
    cd "$_pkgname-${pkgver}"
    python -m build --wheel --no-isolation
}

check() {
    cd "$_pkgname-${pkgver}"
    python bin/colcon build --paths $_pkgname-${pkgver}
    python bin/colcon test --paths $_pkgname-${pkgver} --return-code-on-test-failure
}

package() {
    cd ${srcdir}/${_pkgname}-${pkgver}
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 README.rst -t "$pkgdir/usr/share/doc/$pkgname"
}
