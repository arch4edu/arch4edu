# Maintainer: Ashley Bone <ashley DOT bone AT pm DOT me>
# Contributor: Carlos Aznarán <caznaranl@uni.pe>
pkgname=('python-portalocker')
_pkgname=portalocker
pkgver=2.8.2
pkgrel=2
pkgdesc='Easy, portable file locking API.'
arch=('any')
url="https://github.com/WoLpH/${_pkgname}"
license=('PSF')
depends=('python')
makedepends=('python-build' 'python-installer' 'python-pygments' 'python-setuptools' 'python-setuptools-scm' 'python-wheel')
checkdepends=('python-pytest' 'python-pytest-cov' 'python-pytest-timeout' 'python-redis')
optdepends=('python-redis: redis lock support')
source=("https://pypi.python.org/packages/source/p/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha256sums=('2b035aa7828e46c58e9b31390ee1f169b98e1066ab10b9a6a861fe7e25ee4f33')

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
