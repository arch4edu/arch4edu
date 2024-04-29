# Maintainer: Martin Diehl <aur@martin-diehl.net>

pkgver=0.43.6
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
sha512sums=('27cf0d7e25f1144de471e169259e3b10c40132c12a9a403d4688e0a5c800d262f62648747b2c9ec4cc608e01cc2b78156ef7b9919f3a1503bb273b656c29dc68')

build() {
    cd "$_name-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$_name-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
