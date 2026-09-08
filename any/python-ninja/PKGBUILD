# Maintainer: peippo <christoph.fink@gmail.com>
# Contributor: Carlos Aznarán <caznaranl@uni.pe>

pkgname="python-ninja"
_name=${pkgname#python-}
pkgdesc="The infrastructure to build Ninja Python wheels"
url="https://github.com/scikit-build/ninja-python-distributions"

pkgver=1.13.2
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
b2sums=("512055a3515b2812373b98a045785550cdf0c4c3d1c2e1ba3042a63c07aee4f80f141bac57682e26f1bf3318cad2b70f0b4735e59e54e2e1b5eafaf447bc39da")

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
