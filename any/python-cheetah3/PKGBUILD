# Maintainer: Alex Brinister <alex_brinister at yahoo dot com>

pkgbase=python-cheetah3
pkgname='python-cheetah3'
_name=Cheetah3
pkgver=3.2.6
_subver="post2"
pkgrel=4
pkgdesc="A Python powered template engine and code generator"
arch=('any')
url="http://www.cheetahtemplate.org"
license=(MIT)
depends=('python')
optdepends=('python-markdown')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.${_subver}.tar.gz")
sha512sums=('94b45c4e48e507b9eca254d097fff7175b2d75597cfda05a7a8f373917d333a5bc2e48ff7eebe5f8f711b0ed2531adbe2bfee3c271c093026c3ece2627734e1b')

package_python-cheetah3() {
  cd "${srcdir}/${_name}-${pkgver}.${_subver}"
  python setup.py install --root="${pkgdir}" --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
