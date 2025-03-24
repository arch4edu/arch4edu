# Maintainer: peippo <christoph.fink@gmail.com>
# Contributor: Carlos Aznarán <caznaranl@uni.pe>

pkgname="python-ninja"
_name=${pkgname#python-}
pkgdesc="The infrastructure to build Ninja Python wheels"
url="https://github.com/scikit-build/ninja-python-distributions"

pkgver=1.11.1.4
pkgrel=1

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

source=("${pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_name::1}/${_name//-/_}/${_name//-/_}-$pkgver.tar.gz")
b2sums=("c5b988c97a0bca3604534d2f22b2e255b5dbcd17e4b6386c5c31cd4d7389b4f8855a1874eb1c5951c7c6b80b701e840b0a8ddce93d737753f43b9c6cac2634be")

build() {
    cd "${srcdir}/${_name}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_name}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    rm "${pkgdir}/usr/bin/ninja"  # conflict with `ninja`
}
