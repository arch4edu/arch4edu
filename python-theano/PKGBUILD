# Maintainer: David McInnis <dave@dave3.xyz>

pkgbase="python-theano"
pkgname=("python-theano" "python2-theano")
_pkgname="Theano"
pkgver="1.0.4"
pkgrel="1"
pkgdesc='Definition and optimized evaluation of mathematical expressions on Numpy arrays.'
arch=('any')
url='http://www.deeplearning.net/software/theano/'
license=('BSD')
makedepends=('python-distribute' 'python2-distribute')
checkdepends=('python-nose' 'python-parameterized' 'python2-nose' 'python2-parameterized')
optdepends=('python-sympy: Recommended'
            'python-scipy: Recommended'
            'python-pycuda'
            'python-pydot-ng: Preferred over python-pydot'
            'python-pydot'
            'python-pygpu-git'
            'python-scikit-sparse'
            'python-mpi4py: minimal support for opencl'
            'python2-sympy'
            'python2-scipy'
            'python2-pycuda'
            'python2-pydot-ng'
            'python2-pygpu-git'
            'python2-pydot'
            'python2-mpi4py')
source=("https://pypi.python.org/packages/7d/c4/6341148ad458b6cd8361b774d7ee6895c38eab88f05331f22304c484ed5d/Theano-${pkgver}.tar.gz")
sha256sums=('35c9bbef56b61ffa299265a42a4e8f8cb5a07b2997dabaef0f8830b397086913')

prepare() {
  cd "${_pkgname}-${pkgver}"
  chmod +x "${_pkgname}.egg-info"
  chmod 644 ${_pkgname}.egg-info/*
  chmod -R a+r ./
  cd "$srcdir/"
  cp -a "${_pkgname}-${pkgver}" "${_pkgname}-${pkgver}-py2"
  cd "${_pkgname}-${pkgver}"
  sed -e "s|#![ ]*/usr/bin/python$|#!/usr/bin/python2|" \
      -e "s|#![ ]*/usr/bin/env python$|#!/usr/bin/env python2|" \
      -e "s|#![ ]*/bin/env python$|#!/usr/bin/env python2|" \
      -i $(find . -name '*.py')
}

build() {
  msg "Building Python 2"
  cd "$srcdir/${_pkgname}-${pkgver}-py2"
  python2 setup.py build

  msg "Building Python 3"
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py build
}

# Tests take many hours and need over 8G of memory
# All Python and Python2 tests pass
#
# -------------------------------------------------
#check() {
#  msg "Checking Python 2"
#  cd "$srcdir/${_pkgname}-${pkgver}-py2"/build/lib/theano/
#  nosetests2 -vv -d
#
#  msg "Checking Python 3"
#  cd "$srcdir/${_pkgname}-${pkgver}"/build/lib/theano/
#  nosetests3 -vv -d
#}

package_python2-theano() {
  depends=('python2-numpy')
  cd "$srcdir/${_pkgname}-${pkgver}-py2"
  python2 setup.py install --root="$pkgdir"/ --optimize=1
  mv "${pkgdir}/usr/bin/theano-cache" "${pkgdir}/usr/bin/theano2-cache"
  mv "${pkgdir}/usr/bin/theano-nose" "${pkgdir}/usr/bin/theano2-nose"
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/python2-theano/LICENSE.txt"
}

package_python-theano() {
  depends=('python-numpy')
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/python-theano/LICENSE.txt"
}
