# Maintainer: Ashley Bone <ashley DOT bone AT pm DOT me>
# Contributor: Carlos Aznarán <caznaranl@uni.pe>
pkgname=('python-portalocker')
_pkgname=portalocker
pkgver=4.4.2
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
sha256sums=('7ac85bb2aa3c7873bf2ac72586fc6154afa4671ac786994a16617a6b7ccb3e5e')

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
