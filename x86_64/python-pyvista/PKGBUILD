# Maintainer: Martin Diehl <aur@martin-diehl.net>

pkgname=python-pyvista
pkgver=0.49.1
pkgrel=1
pkgdesc='3D plotting and mesh analysis through a streamlined interface for VTK'
arch=(any)
url=https://www.pyvista.org
license=(MIT)
depends=(python-cyclopts python-matplotlib python-numpy python-pillow python-pooch python-scooby python-typing_extensions vtk)
optdepends=(python-meshio xorg-server-xvfb python-imageio)
makedepends=(python-build python-installer python-wheel python-setuptools)
_name=${pkgname#python-}
source=(https://github.com/pyvista/${_name}/archive/v${pkgver}/${_name}-${pkgver}.tar.gz)
sha512sums=('85834f1af1d0caf5eb231b05b067fe44d64f4ced492ea2b55cbd38f738ea85ab9ab7239c60840a6adf0f45f1403cfca89d49439e6f7e2579c16d9c770fccc533')

build() {
    cd ${_name}-${pkgver}
    python -m build --wheel --no-isolation
}

package() {
    cd ${_name}-${pkgver}
    python -m installer --destdir="${pkgdir}" dist/*.whl
    install -Dm644 LICENSE -t "${pkgdir}"/usr/share/licenses/${pkgname}
}
