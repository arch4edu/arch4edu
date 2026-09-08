# Maintainer: Martin Diehl <aur@martin-diehl.net>

pkgname=python-scooby
pkgver=0.11.1
pkgrel=1
pkgdesc='A Great Dane turned Python environment detective'
arch=(any)
url=https://github.com/banesullivan/scooby
license=(MIT)
depends=(python)
makedepends=(python-build python-installer python-wheel python-setuptools-scm)
_name=${pkgname#python-}
source=(https://github.com/banesullivan/${_name}/archive/v${pkgver}/${_name}-${pkgver}.tar.gz)
sha512sums=('1efb4fa4aebb1d56f422aff0744fc471e10d41d63eb614d401208d811b9ed4bbbc66c29ba9a67ada5c82d0c3aa1d723f0f97848db1bfd663602bf4ab71db99af')

build() {
    cd ${_name}-${pkgver}
    SETUPTOOLS_SCM_PRETEND_VERSION_FOR_SCOOBY=$pkgver python -m build --wheel --no-isolation
}

package() {
    cd ${_name}-${pkgver}
    python -m installer --destdir="${pkgdir}" dist/*.whl
    install -Dm644 LICENSE -t "${pkgdir}"/usr/share/licenses/${pkgname}
}
