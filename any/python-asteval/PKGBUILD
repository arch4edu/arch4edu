# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
# Contributor: Andrew Sun <adsun701 at gmail dot com>
# Contributor: NextHendrix <chris dot jones dot 492 at gmail dot com>
_name=asteval
pkgname=python-$_name
pkgver=1.0.8
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
b2sums=('909926f9e6e2f7cb507c13b0fdf4c8a05ac9704215db0bf830e3fed4bf8cf8688b5477ccafee2aa6f42f3fbab4554ef6144707220eb933397ad1a2bfaf119cc9')

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
