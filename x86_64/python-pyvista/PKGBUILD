# Maintainer: Martin Diehl <aur@martin-diehl.net>

pkgname=python-pyvista
pkgver=0.46.3
pkgrel=1
pkgdesc='3D plotting and mesh analysis through a streamlined interface for VTK'
arch=(any)
url=https://www.pyvista.org
license=(MIT)
depends=(python-numpy python-pillow python-pooch python-scooby vtk python-matplotlib)
optdepends=(python-meshio xorg-server-xvfb python-imageio)
makedepends=(python-build python-installer python-wheel python-setuptools)
_name=${pkgname#python-}
source=(https://github.com/pyvista/${_name}/archive/v${pkgver}/${_name}-${pkgver}.tar.gz)
sha512sums=('5fb86516c267427e0124d273437ee019c0d70f14baacf615a682bd80efab2af96fd2aab7c31b33a3e26e54c818c64fcb33651390f42487ea9915b41f0d23ba81')

build() {
    cd ${_name}-${pkgver}
    python -m build --wheel --no-isolation
}

package() {
    cd ${_name}-${pkgver}
    python -m installer --destdir="${pkgdir}" dist/*.whl
    install -Dm644 LICENSE -t "${pkgdir}"/usr/share/licenses/${pkgname}
}
