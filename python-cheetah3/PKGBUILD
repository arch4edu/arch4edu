# Maintainer: Alex Brinister <alex_brinister at yahoo dot com>

pkgbase=python-cheetah3
pkgname=('python-cheetah3' 'python2-cheetah3')
_name=Cheetah3
pkgver=3.2.6
_subver="post2"
pkgrel=3
pkgdesc="A Python powered template engine and code generator"
arch=('any')
url="http://www.cheetahtemplate.org"
license=(MIT)
makedepends=('python-setuptools'
             'python2-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.${_subver}.tar.gz")
sha512sums=('94b45c4e48e507b9eca254d097fff7175b2d75597cfda05a7a8f373917d333a5bc2e48ff7eebe5f8f711b0ed2531adbe2bfee3c271c093026c3ece2627734e1b')

prepare() {
  cp -a Cheetah3-${pkgver}.${_subver}{,-py2}
}

package_python-cheetah3() {
  depends=('python')
  optdepends=('python-markdown')

  cd "${srcdir}/${_name}-${pkgver}.${_subver}"
  python setup.py install --root="${pkgdir}" --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_python2-cheetah3() {
  depends=('python2')
  optdepends=('python2-markdown')

  cd "${srcdir}/${_name}-${pkgver}.${_subver}-py2"
  python2 setup.py install --root="${pkgdir}" --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  # Avoid conflict with python-cheetah3
  for name in cheetah cheetah-analyze cheetah-compile; do
    mv "${pkgdir}/usr/bin/${name}"{,2}
  done
}
