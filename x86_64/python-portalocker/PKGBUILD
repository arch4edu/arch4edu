# Maintainer: Ashley Bone <ashley DOT bone AT pm DOT me>
# Contributor: Carlos Aznarán <caznaranl@uni.pe>
pkgname=('python-portalocker')
_pkgname=portalocker
pkgver=4.3.0
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
source=("https://pypi.python.org/packages/source/p/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha256sums=('69bf8e46769d66eb0a23219b9550253d2c3b5f03400202a2333784c1e6395e32')

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
