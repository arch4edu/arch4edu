# Maintainer: Oliver Harley <oliver.r.harley+aur (at) gmail.com>
# Since python-keras pulls in quite a few dependencies and I assume few people are using python2 for
# keras (no complaints thus far), the required makedepends for the python2 version has been
# commented out, remove the comment if you require python2.
_pkgname=Keras_Applications
pkgbase=python-keras-applications
pkgname=("python-keras-applications" "python2-keras-applications")
pkgver=1.0.5
pkgrel=1

pkgdesc="Applications module of the Keras deep learning library"
arch=('any')
url="https://pypi.org/project/Keras-Applications/"
license=('MIT')
provides=(python-keras-applications)

source=("https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")

sha256sums=('26a7318b9d8d5be80d75ab08a1284aaf4b94125dd8271b18ca89791e16eb2cfc')

makedepends=('python' 'python-setuptools' 'python-numpy'    #'python-keras'
             'python2' 'python2-setuptools' 'python2-numpy' #'python2-keras'
             )

prepare() {
  cd "$srcdir/"
# Python 2 package
  cp -a "${_pkgname}-${pkgver}" "${_pkgname}-${pkgver}-py2"
  cd "${_pkgname}-${pkgver}-py2"
  sed -e "s|#![ ]*/usr/bin/python$|#!/usr/bin/python2|" \
      -e "s|#![ ]*/usr/bin/env python$|#!/usr/bin/env python2|" \
      -e "s|#![ ]*/bin/env python$|#!/usr/bin/env python2|" \
      -i $(find . -name '*.py')
}

build() {

  msg "Building Python 3"
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py build

  msg "Building Python 2"
  cd "$srcdir/${_pkgname}-${pkgver}-py2"
  python2 setup.py build
}

package_python2-keras-applications() {
  depends=('python2' 'python2-numpy' 'python2-keras')
  #optdepends=('python2-theano' 'cudnn')
  cd "$srcdir/${_pkgname}-${pkgver}-py2"
  python2 setup.py install --root="${pkgdir}"/ --optimize=1
}

package_python-keras-applications() {
  depends=('python' 'python-numpy' 'python-keras')
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}"/ --optimize=1
}
