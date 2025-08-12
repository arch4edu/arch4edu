# Maintainer: peippo <christoph.fink@gmail.com>
# Contributor: Carlos Aznarán <caznaranl@uni.pe>

pkgname="python-ninja"
_name=${pkgname#python-}
pkgdesc="The infrastructure to build Ninja Python wheels"
url="https://github.com/scikit-build/ninja-python-distributions"

pkgver=1.13.0
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
b2sums=("7b330401c776fc3f510e130b52b1bc0cf1103598fc9996d93769cf6de5d72a6a9521e1c5502c63ab5dc8aa9860281ac1b21e5e0086046e26d55a7c76e25bf543")

build() {
    cd "${srcdir}/${_name}-${pkgver}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_name}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
    rm "${pkgdir}/usr/bin/ninja"  # conflict with `ninja`
    rm -R "${pkgdir}/usr/bin"  # now empty
}
