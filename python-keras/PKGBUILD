# Maintainer: Jingbei Li <i@jingbei.li>
# Contributer: David McInnis <dave@dave3.xyz>
# Contributer: Fabien Dubosson <fabien.dubosson@gmail.com>

pkgname=python-keras
_pkgname="keras"
pkgver=2.4.0
pkgrel=1
pkgdesc="Deep Learning library (convnets, recurrent neural networks, and more)"
arch=('any')
url="https://github.com/keras-team/keras"
license=('Apache')
depends=(
  absl-py
  python-h5py
  python-keras-preprocessing
  python-numpy
  python-pandas
  python-pydot
  python-scipy
  python-six
  python-yaml
  python-pillow
)
makedepends=(python-setuptools)
optdepends=(
  'python-theano: For Theano backend'
  'python-tensorflow: For TensorFlow backend'
  'mxnet: For MXNet backend'
)
source=("https://github.com/keras-team/${_pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('ef97067e35719cf93b7b835d1300015bb1e1f1a7b3dd7be897c110419fa1a1d1')

build() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py build
}

package_python-keras() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}
