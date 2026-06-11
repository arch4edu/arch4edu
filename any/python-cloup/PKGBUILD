# Maintainer: Groctel <aur@taxorubio.com>
# shellcheck disable=SC2034,SC2154,SC2164

_name=cloup

pkgname=python-cloup
pkgver=3.1.0
pkgrel=1
pkgdesc="Cloup (= Click + groups) contains a set of Click extensions for multiple purposes."

arch=("any")
license=("MIT")
url="https://github.com/janLuke/cloup"

source=("https://github.com/janLuke/$_name/archive/refs/tags/v$pkgver.tar.gz")
sha512sums=('c9eed29f4b9ce6ccdb7b2e9b74f34922f4e1105b90da35cb652b20860a10409f9490a6966db58914454ffaabf53ea00641110b2ebb8e2f1f8f2f9240865af604')

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

prepare() {
    cd "$srcdir/$_name-$pkgver"
    sed -i 's/setuptools_scm<10/setuptools_scm/' setup.py
}

build() {
    cd "$srcdir/$_name-$pkgver"
    SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver} \
        python -m build --wheel --no-isolation
}

check() {
    cd "$srcdir/$_name-$pkgver"
    pytest
}

package() {
    cd "$srcdir/$_name-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
