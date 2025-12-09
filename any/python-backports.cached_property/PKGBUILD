# Maintainer: Groctel <aur@taxorubio.com>
# shellcheck disable=SC2034,SC2154,SC2164

_name=backports.cached_property

pkgname=python-backports.cached_property
pkgver=1.0.2
pkgrel=1
pkgdesc="Python 3.8 functools.cached_property backport to python 3.6."

arch=("any")
license=("MIT")
url="https://github.com/penguinolog/backports.cached_property"

source=("$url/archive/refs/tags/$pkgver.tar.gz")
sha512sums=('393272e93f97783d575268e19005d3295570dfc562afe179b6d4ac56960b57b71454639f3588a1dcd531e0871fc7b6fa91bbd854ad4f1c16875f1d6d75cb0aa2')

depends=("python")
makedepends=(
    "python-build"
    "python-installer"
    "python-setuptools"
    "python-setuptools-scm"
    "python-wheel"
)
checkdepends=(
    "python-pytest"
    "python-pytest-mock"
    "python-virtualenv"
)

build () {
    cd "$srcdir/$_name-$pkgver" || exit
    SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver} \
        python -m build --wheel --no-isolation
}

check () {
    cd "$srcdir/$_name-$pkgver"

    python -m venv --system-site-packages venv
    source venv/bin/activate
    pip install ./dist/*.whl
    PYTHONPATH="$PYTHONPATH:." pytest
    rm -rf venv
}

package () {
    cd "$srcdir/$_name-$pkgver" || exit
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
