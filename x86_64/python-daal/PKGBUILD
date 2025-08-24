pkgname='python-daal'
_module='daal'
_src_folder='daal-2025.7.0'
pkgver='2025.7.0'
pkgrel=1
pkgdesc="Intel® oneAPI Data Analytics Library"
url="https://www.intel.com/content/www/us/en/developer/tools/oneapi/onedal.html"
depends=('python' 'onetbb')
makedepends=('python-build' 'python-installer' 'python-wheel')
license=('custom:Other/Proprietary License')
arch=('any')
source=("https://files.pythonhosted.org/packages/fd/a6/ee2d6b76144fff80427047df42d28bdcb1ad8fe970050709aca2194aa5bd/daal-2025.7.0-py2.py3-none-manylinux_2_28_x86_64.whl")
sha256sums=('f293d6e021dbc3a5b5d6c253ff2a272f78c43ff2203be74bd6c6e9e68d1b9a1e')

package() {
    python -m installer --destdir="${pkgdir}" daal-2025.7.0-py2.py3-none-manylinux_2_28_x86_64.whl
}
