# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=platform-services-python-sdk
pkgname=python-ibm-platform-services
pkgver=0.49.0
pkgrel=1
pkgdesc="Python client library for IBM Cloud Platform Services"
arch=('any')
url="https://github.com/IBM/platform-services-python-sdk"
license=('Apache-2.0')
depends=(
    'python'
    'python-ibm-cloud-sdk-core'
)
makedepends=(
    'python-build'
    'python-installer'
    'python-setuptools'
    'python-wheel'
)
checkdepends=(
    'python-pytest'
    'python-responses'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/IBM/${_pkgname}/archive/refs/tags/v${pkgver}.tar.gz")
b2sums=('e6caa510fd3ccabc7f883aabb2a63aecd04b91fe3ee309535ee4956d8d33e7cbf814b1160b65220b3b2fd723deec29aff1552c58878a901318283b6707b9c0d1')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

check() {
    local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
    cd "${_pkgname}-${pkgver}"
    python -m installer --destdir=test_dir dist/*.whl
    PYTHONPATH="test_dir/$_site_packages:$PYTHONPATH" pytest test/unit
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="$pkgdir" dist/*.whl
}
