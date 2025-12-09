# Maintainer: Groctel <aur@taxorubio.com>
# shellcheck disable=SC2034,SC2154,SC2164

_name=cloup

pkgname=python-cloup
pkgver=3.0.8
pkgrel=1
pkgdesc="Cloup (= Click + groups) contains a set of Click extensions for multiple purposes."

arch=("any")
license=("MIT")
url="https://github.com/janLuke/cloup"

source=("https://github.com/janLuke/$_name/archive/refs/tags/v$pkgver.tar.gz")
sha512sums=('f14d5f68aeebb958acdf5812ff6c211db245103688006eba3f0afb82884a4c915bdd8753f2823a515b6acb571fb26d079a0ec3a68e894b365b25dc1b8ca8f6ac')

depends=(
    "python"
    "python-click"
    "python-typing_extensions"
)
makedepends=(
    "python-build"
    "python-installer"
    "python-setuptools"
    "python-setuptools-scm"
    "python-wheel"
)
checkdepends=(
    "python-pytest"
)

build () {
    cd "$srcdir/$_name-$pkgver"
    SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver} \
        python -m build --wheel --no-isolation
}

check () {
    cd "$srcdir/$_name-$pkgver"
    pytest
}

package () {
    cd "$srcdir/$_name-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
