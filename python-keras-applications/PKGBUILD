# Maintainer: Oliver Harley <oliver.r.harley+aur (at) gmail.com>
# Since python-keras pulls in quite a few dependencies and I assume few people are using python2 for
# keras (no complaints thus far), the required makedepends for the python2 version has been
# commented out, remove the comment if you require python2.
_pkgname=keras-applications
_subrelease='resnet'
pkgbase=python-keras-applications
pkgname=("python-keras-applications" "python2-keras-applications")
pkgver=1.0.4
pkgrel=2

if [ ! -z "$_subrelease" ]; then
_fullrelease=${_pkgname}-${pkgver}-${_subrelease}
else
_fullrelease=${_pkgname}-${pkgver}
fi
# add / remove the $_subrelease as needed

pkgdesc="Applications module of the Keras deep learning library"
arch=('any')
url="https://github.com/keras-team/keras-applications/"
license=('MIT')
provides=(python-keras-applications)

if [ ! -z "$_subrelease" ]; then
source=("${_fullrelease}.tar.gz::https://github.com/keras-team/${_pkgname}/archive/${_subrelease}.tar.gz")
else
source=("${_fullrelease}.tar.gz::https://github.com/keras-team/${_pkgname}/archive/${_fullrelease}.tar.gz")
fi

sha256sums=('43c0033a2506398e5707b0f05588a725015de1e89dc01759b9273924409bced0')

makedepends=('python' 'python-setuptools' 'python-numpy'    #'python-keras'
             'python2' 'python2-setuptools' 'python2-numpy' #'python2-keras'
             )

prepare() {
  cd "$srcdir/"
  if [ ! -z "$_subrelease" ]; then
      mv "${_pkgname}-${_subrelease}" "${_fullrelease}"
  fi

  cp -a "${_fullrelease}" "${_fullrelease}-py2"
  cd "${_fullrelease}-py2"
  sed -e "s|#![ ]*/usr/bin/python$|#!/usr/bin/python2|" \
      -e "s|#![ ]*/usr/bin/env python$|#!/usr/bin/env python2|" \
      -e "s|#![ ]*/bin/env python$|#!/usr/bin/env python2|" \
      -i $(find . -name '*.py')
}

build() {
  msg "Building Python 2"
  cd "$srcdir/${_fullrelease}-py2"
  python2 setup.py build

  msg "Building Python 3"
  cd "$srcdir/${_fullrelease}"
  python setup.py build
}

package_python2-keras-applications() {
  depends=('python2' 'python2-numpy' 'python2-keras')
  #optdepends=('python2-theano' 'cudnn')
  cd "$srcdir/${_fullrelease}-py2"
  python2 setup.py install --root="${pkgdir}"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}

package_python-keras-applications() {
  depends=('python' 'python-numpy' 'python-keras')
  cd "$srcdir/${_fullrelease}"
  python setup.py install --root="${pkgdir}"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}

