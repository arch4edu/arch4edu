# Maintainer: Martin Diehl <aur@martin-diehl.net>

pkgver=0.43.7
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
sha512sums=('1245d884f1e53230af30e27ec4d9f40a527f583370386e3cbc1d1a1e9d5d1c0df831cfe7293ef84ce8ee03913124a9a413c77b5ae8eee475d1ffc106ebe148ad')

build() {
    cd "$_name-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$_name-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
