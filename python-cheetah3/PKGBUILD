# Maintainer: Alex Brinister <alex_brinister at yahoo dot com>

pkgbase=python-cheetah3
pkgname=('python-cheetah3' 'python2-cheetah3')
_name=Cheetah3
pkgver=3.2.6
_subver="post1"
pkgrel=2
pkgdesc="A Python powered template engine and code generator"
arch=('any')
url="http://www.cheetahtemplate.org"
license=(MIT)
makedepends=('python-setuptools'
             'python2-setuptools')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.${_subver}.tar.gz")
sha512sums=('69b82ccf31930c50ffdcbc7608683a8456d8025ca3633b0637d16de64aa9337f5f65da86d54bb2b3aa41722f25727a503307b5a7cc80a13d74f332117d6ca05e')

prepare() {
  cp -a Cheetah3-${pkgver}.${_subver}{,-py2}
}

package_python-cheetah3() {
  optdepends=('python-markdown')

  cd "${srcdir}/${_name}-${pkgver}.${_subver}"
  python setup.py install --root="${pkgdir}" --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_python2-cheetah3() {
  optdepends=('python2-markdown')

  cd "${srcdir}/${_name}-${pkgver}.${_subver}-py2"
  python2 setup.py install --root="${pkgdir}" --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  # Avoid conflict with python-cheetah3
  for name in cheetah cheetah-analyze cheetah-compile; do
    mv "${pkgdir}/usr/bin/${name}"{,2}
  done
}
