# Maintainer: Martin Diehl <aur@martin-diehl.net>

pkgver=0.43.8
pkgrel=1
pkgname=python-pyvista
_name=${pkgname#python-}
pkgdesc='3D plotting and mesh analysis through a streamlined interface for the Visualization Toolkit (VTK)'
arch=('any')
url='https://www.pyvista.org'
license=('MIT')
depends=('python-numpy' 'python-pillow' 'python-pooch' 'python-scooby' 'vtk' 'python-matplotlib')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools')
optdepends=('python-meshio' 'xorg-server-xvfb' 'python-imageio')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
sha512sums=('636ddfe46b8bfce8a29f1fb74912de55524feef5511d08942bc5019fafbff63fb5aabb26c69b4d09b78f80e68cf9d8f60058778e241dc2e032eced643a78b07d')

build() {
    cd "$_name-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$_name-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
}
