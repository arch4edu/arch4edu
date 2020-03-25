# Maintainer: Manuel Schmitzberger <mail@ms-sw.at>

pkgname='python-cppheaderparser'
pkgver=2.7.4
pkgrel=1
pkgdesc="Parse C++ header files and generate a data structure representing the class"
arch=('any')
url="https://github.com/clothbot/cppheaderparser"
license=('APACHE')
depends=('python')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/3c/ba/d8d168a4b54cae66eaf13d1d9197ca9349c94653815e061f79e7eed86c01/CppHeaderParser-${pkgver}.tar.gz")
md5sums=('53bbc8984ccb61b37444a4e8110d2591')

package() {
  cd "${srcdir}/CppHeaderParser-${pkgver}"
  python3 setup.py install --root="${pkgdir}" -O1
}
