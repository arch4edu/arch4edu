# Maintainer: Ashley Bone <ashley DOT bone AT pm DOT me>
# Contributor: Carlos Aznarán <caznaranl@uni.pe>
pkgname=('python-portalocker')
_pkgname=portalocker
pkgver=4.4.0
pkgrel=1
pkgdesc='Easy, portable file locking API.'
arch=('any')
url="https://github.com/WoLpH/${_pkgname}"
license=('BSD-3-Clause')
depends=('python')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-uv-build' 'python-wheel')
#checkdepends=('python-coverage-conditional-plugin' 'python-fakeredis' 'python-flaky' 'python-pytest'
#              'python-pytest-cov' 'python-pytest-rerunfailures' 'python-pytest-timeout' 'python-redis')
optdepends=('python-redis: redis lock support')
source=("https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname//-/_}/${_pkgname//-/_}-$pkgver.tar.gz")
sha256sums=('90c0df939d4ffba121f8e925bbf98ecea8b9381718666ab871a226938d2b63b2')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

# check() {
#     cd "${srcdir}/${_pkgname}-${pkgver}"
#     pytest
# }

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
    install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
