# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=openqasm
pkgname=python-${_pkgname}3
pkgver=1.0.2
pkgrel=1
pkgdesc="Reference OpenQASM AST in Python"
arch=(any)
url=https://github.com/openqasm/openqasm
license=(Apache-2.0)
depends=(
    python-antlr4
    python-importlib-metadata
)
makedepends=(
    antlr4
    git
    python-build
    python-installer
    python-setuptools
    python-wheel
)
checkdepends=(python-pytest)
source=($_pkgname::git+https://github.com/openqasm/openqasm#tag=ast-py/v$pkgver)
b2sums=('1853d71dd862dc2c1b83b2221b65b82f03e47d0bb6bdd6943af0c514c6878d60ec5a0af28b09c4b9805983099382d3de529dbfce9255661746c5ba4f3bc59794')

build() {
    cd $_pkgname/source/grammar

    # Build the ANTLR files
    local python_version=$(python -c 'import sys; print("".join(map(str, sys.version_info[:2])))')
    local antlr_version=$(ls /usr/share/java/antlr-*-complete.jar | cut -d "-" -f 2)
    local antlr_major=$(echo $antlr_version | cut -d "." -f 1)
    local antlr_minor=$(echo $antlr_version | cut -d "." -f 2)
    local antlr_out_dir=../$_pkgname/${_pkgname}3/_antlr/_${antlr_major}_${antlr_minor}
    mkdir -p $antlr_out_dir
    java -Xmx500M -jar /usr/share/java/antlr-complete.jar -o $antlr_out_dir -Dlanguage=Python3 -visitor qasm3Lexer.g4 qasm3Parser.g4

    # Build the wheel package
    cd ../$_pkgname
    python -m build --wheel --no-isolation
}

check() {
    cd $_pkgname/source/$_pkgname
    python -m venv --system-site-packages test-env
    test-env/bin/python -m installer dist/*.whl
    rm -r ${_pkgname}3
    test-env/bin/python -P -m pytest -o addopts="" tests
}

package() {
    cd $_pkgname/source/$_pkgname
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -D -m644 LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
