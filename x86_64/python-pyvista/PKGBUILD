# Maintainer: Martin Diehl <aur@martin-diehl.net>

pkgname=python-pyvista
pkgver=0.46.5
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
sha512sums=('7bf81be3266d3ebb60b21857daea629999267952a8eb9301856e3d65c613a3f96de629b0478f0222cbfede01bfd088db909de8ce2de702188b99822a3e18c43e')

build() {
    cd ${_name}-${pkgver}
    python -m build --wheel --no-isolation
}

package() {
    cd ${_name}-${pkgver}
    python -m installer --destdir="${pkgdir}" dist/*.whl
    install -Dm644 LICENSE -t "${pkgdir}"/usr/share/licenses/${pkgname}
}
