# Maintainer: Jingbei Li <i@jingbei.li>
# Contributer: David McInnis <dave@dave3.xyz>
# Contributer: Fabien Dubosson <fabien.dubosson@gmail.com>

pkgname=python-keras
_pkgname="Keras"
pkgver=2.4.3
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
source=("https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha256sums=('fedd729b52572fb108a98e3d97e1bac10a81d3917d2103cc20ab2a5f03beb973')

build() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py build
}

package_python-keras() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  python setup.py install --root="$pkgdir"/ --optimize=1
  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt"
}
