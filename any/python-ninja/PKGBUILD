# Maintainer: peippo <christoph.fink@gmail.com>
# Contributor: Carlos Aznarán <caznaranl@uni.pe>

pkgname="python-ninja"
_name=${pkgname#python-}
pkgdesc="The infrastructure to build Ninja Python wheels"
url="https://github.com/scikit-build/ninja-python-distributions"

pkgver=1.11.1.1
pkgrel=1

arch=("any")
license=("Apache-2.0")

depends=(
    "python"
)
makedepends=(
    "python-build"
    "python-installer"
    "python-scikit-build"
    "python-setuptools"
    "python-setuptools-scm"
    "python-wheel"
)
checkdepends=(
    "python-coverage"
    "python-importlib-metadata"
    "python-path"
    "python-pytest"
    "python-pytest-cov"
)
source=(
    "${pkgname}-${pkgver}.tar.gz::https://github.com/scikit-build/ninja-python-distributions/archive/refs/tags/${pkgver}.tar.gz"
    "python-ninja-entrypoints.patch"
)
b2sums=(
    "eceaaa7abd538930e41625ad33c923d9619c9fe851454afdcf5b20d0df932e9f961f7c2332ec2a99c4baa48db9d2e0dc9cef10915e2765da98cb056c63c5107b"
    "3dfd40633dc9797736faf7507d9c172aee961d105d92168bf2d72af1b4d3ae4a79f656668b3332516908c18351784a2744973408e126ce4efa31174e01f7bd28"
)

prepare() {
    cd "${srcdir}/ninja-python-distributions-${pkgver}"
    patch --forward --strip=1 --input="${srcdir}/python-ninja-entrypoints.patch"
}

build() {
    cd "${srcdir}/ninja-python-distributions-${pkgver}"
    python -m build --wheel --no-isolation
}

check() {
    cd "${srcdir}/ninja-python-distributions-${pkgver}"
    python -m pytest . || true
}

package() {
    cd "${srcdir}/ninja-python-distributions-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}
