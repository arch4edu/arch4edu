# Maintainer: David McInnis <davidm@eagles.ewu.edu>

pkgbase="python-theano"
pkgname=("python-theano" "python2-theano")
_pkgname="Theano"
pkgver="0.9.0"
pkgrel="1"
pkgdesc='Definition and optimized evaluation of mathematical expressions on Numpy arrays.'
arch=('any')
url='http://www.deeplearning.net/software/theano/'
license=('BSD')
depends=('python'  'python-numpy' 
         'python2' 'python2-numpy')
makedepends=('python-distribute' 'python2-distribute')
checkdepends=('python-nose' 'python-nose-parameterized' 'python2-nose' 'python2-nose-parameterized')
optdepends=('python-sympy: Recommended'
            'python-scipy: Recommended'
            'python-pycuda:'
            'python-pydot-ng: Preferred over python-pydot'
            'python-pydot'
            'python-pygpu'
            'python-scikit-sparse'
            'python-mpi4py: minimal support for opencl'
            'python2-sympy'
            'python2-scipy'
            'python2-pycuda'
            'python2-pydot-ng'
            'python2-pydot'
            'python2-mpi4py')
source=("http://pypi.python.org/packages/28/03/6af9ff242da966f89de6ab81164db0d1a36fd89379b7370f07043de62f10/Theano-${pkgver}.tar.gz")
sha256sums=('745d66716531f9063127274b40503fbc21f931f78b7b03e79e5523d50078bc17')
         
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

# All CPU tests for Python2 pass on my machine, but the 
# theano.tensor.tests.test_mpi.test_mpi_roundtrip test
# for Python3 Hangs indefinitely
# many CUDA tests fail on my machine
# My Nvidia 9600GT is old & requires cuda65 to work
#-------------------------------------------------
#check() {
#  msg "Checking Python 2"
#  cd "$srcdir/${_pkgname}-${pkgver}-py2"/build/lib/theano/
#  ../../../bin/theano-cache clear
#  THEANO_FLAGS=cuda.enabled=False nosetests2 -v -d
#
#  msg "Checking Python 3"
#  cd "$srcdir/${_pkgname}-${pkgver}"/build/lib/theano/
#  ../../../bin/theano-cache clear
#  THEANO_FLAGS=cuda.enabled=False nosetests3 -v -d
#}

package_python2-theano() {
  depends=('python2' 'python2-numpy')
  cd "$srcdir/${_pkgname}-${pkgver}-py2"
  python2 setup.py install --root="$pkgdir"/ --optimize=1
  mv "${pkgdir}/usr/bin/theano-cache" "${pkgdir}/usr/bin/theano2-cache"
  mv "${pkgdir}/usr/bin/theano-nose" "${pkgdir}/usr/bin/theano2-nose"
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/python2-theano/LICENSE.txt"
}

package_python-theano() {
  depends=('python' 'python-numpy')
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/python-theano/LICENSE.txt"
}
