# Maintainer: Groctel <aur@taxorubio.com>
# Maintainer: Naveen M K <naveen521kk@gmail.com>
# shellcheck disable=SC1091,SC2034,SC2154,SC2164

_name=manimpango

pkgname=python-manimpango
pkgver=0.7.0
pkgrel=1
pkgdesc="C binding for Pango using Cython used in Manim to render (non-LaTeX) text."

arch=("x86_64")
license=("MIT")
url="https://github.com/ManimCommunity/ManimPango"

source=("$url/releases/download/v$pkgver/$_name-$pkgver.tar.gz")
sha512sums=('f73ac8b396a416a14658349a6e689b4cad9d39109bd55070a26f51dd7ea6161868af7f20dfcacfa72a3e40a66fada7035c303fbb70f6597d0ac88c4b04955399')

depends=(
    "cairo"
    "fontconfig"
    "glib2"
    "pango"
    "python"
)
makedepends=(
    "cython"
    "python-build"
    "python-installer"
    "python-setuptools"
    "python-wheel"
)
checkdepends=(
    "cython"
    "python-coverage"
    "python-pytest"
    "python-pytest-cov"
    "python-setuptools"
    "python-virtualenv"
    # https://github.com/ManimCommunity/ManimPango/issues/110
    "cantarell-fonts" # An installed font is required; it doesn't need to be this one.
)

prepare () {
    sed -i 's/Cython>=3.0.2,<3.1/Cython>=3.1/' "$_name-$pkgver/pyproject.toml"
}

build () {
    cd "$srcdir/$_name-$pkgver"
    python -m build --wheel --no-isolation
    python setup.py build_ext -i
}

check () {
    cd "$srcdir/$_name-$pkgver"

    python -m venv --system-site-packages venv
    source venv/bin/activate
    pip install ./dist/*.whl
    pytest
    rm -rf venv
}

package () {
    cd "$srcdir/$_name-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
