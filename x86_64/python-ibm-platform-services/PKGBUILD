# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
_pkgname=platform-services-python-sdk
pkgname=python-ibm-platform-services
pkgver=0.49.2
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
b2sums=('9754c9bdadd669d458c44331c2a5f4af9a11027e5d843ed5c2ae3976fac6e1f356d44460b8f4e429aa80d36c91031683e476c2c3b8f54d5b9d73e481ded7906e')

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
