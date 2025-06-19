# Maintainer: Ashley Bone <ashley DOT bone AT pm DOT me>
# Contributor: Carlos Aznarán <caznaranl@uni.pe>
pkgname=('python-portalocker')
_pkgname=portalocker
pkgver=3.2.0
pkgrel=1
pkgdesc='Easy, portable file locking API.'
arch=('any')
url="https://github.com/WoLpH/${_pkgname}"
license=('BSD-3-Clause')
depends=('python')
makedepends=('python-build' 'python-installer' 'python-pygments' 'python-setuptools' 'python-setuptools-scm' 'python-wheel')
checkdepends=('python-coverage-conditional-plugin' 'python-pytest' 'python-pytest-cov'
              'python-pytest-timeout' 'python-redis')
optdepends=('python-redis: redis lock support')
source=("https://pypi.python.org/packages/source/p/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha256sums=('1f3002956a54a8c3730586c5c77bf18fae4149e07eaf1c29fc3faf4d5a3f89ac')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

#check() {
#    cd "${srcdir}/${_pkgname}-${pkgver}"
#    pytest
#}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
    install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
