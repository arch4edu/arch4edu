
_project_name='aioftp'
pkgname="python-${_project_name}"
pkgver=0.21.4
pkgrel=1
pkgdesc="ftp client/server for asyncio"
url="https://github.com/aio-libs/aioftp"
arch=('any')
license=("Apache License Version 2.0")
depends=('python')
makedepends=('python' 'python-setuptools')
source=("https://pypi.io/packages/source/${_project_name:0:1}/${_project_name}/${_project_name}-${pkgver}.tar.gz")

package() {
  cd "${srcdir}/${_project_name}-${pkgver}"
  python3 setup.py build
  python3 setup.py install --prefix=/usr --root="${pkgdir}"
}

sha256sums=('28bb26d4616c7c381a1543281f987051b8d2d1d5bfaf023d9e7e2c2105c51bb9')
