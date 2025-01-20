# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
# Contributor: Andrew Sun <adsun701 at gmail dot com>
# Contributor: NextHendrix <chris dot jones dot 492 at gmail dot com>
_name=asteval
pkgname=python-$_name
pkgver=1.0.6
pkgrel=1
pkgdesc="Minimalistic evaluator of python expression using ast module "
arch=(any)
url=https://github.com/lmfit/asteval
license=(MIT)
depends=(python-numpy)
makedepends=(
    git
    python-build
    python-installer
    python-setuptools
    python-setuptools-scm
    python-wheel
)
checkdepends=(python-pytest)
source=($_name::git+https://github.com/lmfit/$_name#tag=$pkgver)
b2sums=('ca852d4fd57abaa442fbe59bd75f16556291138a8340eff8d88d5d82d6596eef6197857651c5b446070ca7becc7e56455e81d7e7bc8747a2a7c7be241d81ee0c')

build() {
    cd $_name
    python -m build --wheel --no-isolation
}

check() {
   cd $_name
   local python_version=$(python -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
   python -m installer --destdir=../test_dir dist/*.whl
   rm -rf asteval
   PYTHONPATH="$PWD/../test_dir/usr/lib/python$python_version/site-packages" pytest -o addopts="" tests
}

package() {
    cd $_name
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
