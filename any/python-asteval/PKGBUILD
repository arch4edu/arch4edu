# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
# Contributor: Andrew Sun <adsun701 at gmail dot com>
# Contributor: NextHendrix <chris dot jones dot 492 at gmail dot com>
_pkgname=asteval
pkgname=python-${_pkgname}
pkgver=1.0.5
pkgrel=2
pkgdesc="Minimalistic evaluator of python expression using ast module "
arch=(any)
url=https://github.com/lmfit/asteval
license=(MIT)
depends=(python-numpy)
makedepends=(
    python-build
    python-installer
    python-setuptools
    python-setuptools-scm
    python-wheel
)
source=($_pkgname-$pkgver.tar.gz::https://github.com/lmfit/$_pkgname/archive/refs/tags/$pkgver.tar.gz)
b2sums=('159076d1cdcac9ee6d9bf319ccb6ffcdb775fea7a930dce85d1171ede4f3e2b6acf1e9293cfe9d44e8da2762f20507c0781492fa5e6054a4f28fe836581af958')

build() {
    cd $_pkgname-$pkgver
    export SETUPTOOLS_SCM_PRETEND_VERSION=$pkgver
    python -m build --wheel --no-isolation
}

package() {
    cd $_pkgname-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
