# Maintainer: Martin Diehl <aur@martin-diehl.net>

pkgname=python-pyvista
pkgver=0.44.2
pkgrel=3
pkgdesc='3D plotting and mesh analysis through a streamlined interface for VTK'
arch=(any)
url='https://www.pyvista.org'
license=('MIT')
depends=('python-numpy' 'python-pillow' 'python-pooch' 'python-scooby' 'vtk' 'python-matplotlib')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools')
optdepends=('python-meshio' 'xorg-server-xvfb' 'python-imageio')
_name=${pkgname#python-}
source=("https://github.com/pyvista/pyvista/archive/v${pkgver}/pyvista-${pkgver}.tar.gz")
sha512sums=('82a10149dcb47981eb66fa19ccb202a11b5999488b8e69e20913e0e1f11a35bc27e96cd8b983bca49edeaf443d497713a30a2b72f1f82bbb62374d79855a877f')

build() {
    cd "$_name-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$_name-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
}
