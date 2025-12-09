# Maintainer: Marco Rubin <marco.rubin@protonmail.com>

_name=moderngl
pkgname=python-$_name
pkgver=5.12.0
pkgrel=1
pkgdesc='ModernGL: High performance rendering for Python 3'
arch=(x86_64)
url='https://github.com/moderngl/moderngl'
license=('MIT')
depends=(python python-glcontext)
makedepends=(python-build python-installer python-setuptools python-wheel)
source=("$url/archive/$pkgver.tar.gz")
b2sums=('79a5e6eec0d90e64f0c74ed35fc73957fc0a3488c2e831f55ebba41582330f84d104cfb29e051cc0333248d1e66649934432494b505d03765d2f86806e45e259')

build() {
    cd $_name-$pkgver
    python -m build --wheel --no-isolation
}

package() {
    cd $_name-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
