pkgname='python-daal'
_module='daal'
_src_folder='daal-2025.8.0'
pkgver='2025.8.0'
pkgrel=1
pkgdesc="Intel® oneAPI Data Analytics Library"
url="https://github.com/uxlfoundation/oneDAL"
depends=('python' 'onetbb')
makedepends=('python-build' 'python-installer' 'python-wheel')
license=('custom:Other/Proprietary License')
arch=('any')
source=("https://files.pythonhosted.org/packages/76/32/da06ba2bf09ebf841f5847a300dad83032e4c66c07015a2aa38ec34eeaec/daal-2025.8.0-py2.py3-none-manylinux_2_28_x86_64.whl")
sha256sums=('f5f7c8b8d2fcadcd73b195e1c9dc296b096f1094df2c84cb7e91c2a11a8d4e2d')

package() {
    python -m installer --destdir="${pkgdir}" *.whl
}
