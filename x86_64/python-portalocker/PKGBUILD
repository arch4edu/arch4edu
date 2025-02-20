# Maintainer: Ashley Bone <ashley DOT bone AT pm DOT me>
# Contributor: Carlos Aznarán <caznaranl@uni.pe>
pkgname=('python-portalocker')
_pkgname=portalocker
pkgver=3.1.1
pkgrel=1
pkgdesc='Easy, portable file locking API.'
arch=('any')
url="https://github.com/WoLpH/${_pkgname}"
license=('BSD-3-Clause')
depends=('python')
makedepends=('python-build' 'python-installer' 'python-pygments' 'python-setuptools' 'python-setuptools-scm' 'python-wheel')
checkdepends=('python-pytest' 'python-pytest-cov' 'python-pytest-timeout' 'python-redis')
optdepends=('python-redis: redis lock support')
source=("https://pypi.python.org/packages/source/p/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha256sums=('ec20f6dda2ad9ce89fa399a5f31f4f1495f515958f0cb7ca6543cef7bb5a749e')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

check() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    pytest
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
    install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
