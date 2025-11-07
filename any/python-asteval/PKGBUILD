# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
# Contributor: Andrew Sun <adsun701 at gmail dot com>
# Contributor: NextHendrix <chris dot jones dot 492 at gmail dot com>
_name=asteval
pkgname=python-$_name
pkgver=1.0.7
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
b2sums=('9d51df1a722b8fc4c30d9ef271757df9fdadf15a20ecc36c5f1c112bd6d8214d108f479b07f50004b4ac48326531b4012ba2a348a39c3ecd7aff8f520416f3ba')

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
