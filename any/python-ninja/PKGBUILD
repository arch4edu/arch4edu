# Maintainer: peippo <christoph.fink@gmail.com>
# Contributor: Carlos Aznarán <caznaranl@uni.pe>

pkgname="python-ninja"
_name=${pkgname#python-}
pkgdesc="The infrastructure to build Ninja Python wheels"
url="https://github.com/scikit-build/ninja-python-distributions"

pkgver=1.11.1.3
pkgrel=2

arch=("any")
license=("Apache-2.0")

depends=(
    "python"
)
makedepends=(
    "python-build"
    "python-hatch-fancy-pypi-readme"
    "python-installer"
    "python-scikit-build-core"
    "python-setuptools-scm"
    "python-wheel"
)

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/scikit-build/ninja-python-distributions/archive/refs/tags/${pkgver}.tar.gz")
b2sums=("cce325cfa743c43025c8bd820ee17c580241221e6974e6ffa95f28ecc23a7ffeb957359cc68e6e4acac3bf8770ccad3351795abce9443fb714794dfc00a1f5f4")

build() {
    cd "${srcdir}/ninja-python-distributions-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/ninja-python-distributions-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    rm "${pkgdir}/usr/bin/ninja"  # conflict with `ninja`
}
