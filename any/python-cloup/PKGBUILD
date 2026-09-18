# Maintainer: Groctel <aur@taxorubio.com>
# shellcheck disable=SC2034,SC2154,SC2164

_name=cloup

pkgname=python-cloup
pkgver=4.0.0
pkgrel=1
pkgdesc="Cloup (= Click + groups) contains a set of Click extensions for multiple purposes."

arch=("any")
license=("MIT")
url="https://github.com/janLuke/cloup"

source=("https://github.com/janLuke/$_name/archive/refs/tags/v$pkgver.tar.gz")
sha512sums=('487c28ffc8f7e467da37bc45a7da2467fe57e2934bf51d8fb019eebdad9cb77e47f4547f789450a15d74e9c0cdadca98264ef7b0cf91c8a99ed1b112d0249ab8')

depends=(
    "python"
    "python-click"
    "python-typing_extensions"
)
makedepends=(
    "python-build"
    "python-hatchling"
    "python-hatch-vcs"
    "python-installer"
    "python-setuptools"
    "python-setuptools-scm"
    "python-wheel"
)
checkdepends=(
    "python-pytest"
)

build() {
    cd "$srcdir/$_name-$pkgver"
    SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver} \
        python -m build --wheel --no-isolation
}

check() {
    cd "$srcdir/$_name-$pkgver"

    python -m venv --system-site-packages venv
    source venv/bin/activate
    pip install ./dist/*.whl
    python -m pytest
    rm -rf venv
}

package() {
    cd "$srcdir/$_name-$pkgver"
    python -m installer --destdir="$pkgdir" ./dist/*.whl
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
