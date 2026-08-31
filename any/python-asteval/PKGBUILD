# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
# Contributor: Andrew Sun <adsun701 at gmail dot com>
# Contributor: NextHendrix <chris dot jones dot 492 at gmail dot com>
_name=asteval
pkgname=python-$_name
pkgver=1.0.10
pkgrel=1
pkgdesc="Minimalistic evaluator of python expression using ast module"
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
b2sums=('75a32e1ca6a58f735f8e4adae76c051c8c27e71a9e0394da754168952384bf065db07aa5fa486ab7d9e72a0771d9ca7ad82b9350bc788a2bd4073f4aabb33915')

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
