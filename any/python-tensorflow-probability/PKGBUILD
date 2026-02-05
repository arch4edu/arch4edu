# Maintainer: Oystein Sture <oysstu (at) gmail (dot) com>
# Contributor:
pkgname=python-tensorflow-probability
_name=tensorflow_probability
pkgver=0.25.0
pkgrel=4
pkgdesc="Probabilistic reasoning and statistical analysis in TensorFlow"
url="https://github.com/tensorflow/probability"
arch=('any')
license=('Apache-2.0')
depends=('python' 'python-tensorflow' 'python-numpy' 'python-six' 'python-decorator' 'python-cloudpickle' 'python-gast' 'python-dm-tree' 'python-absl' 'python-tf-keras')
makedepends=('python-installer' 'python-wheel')
source=("https://files.pythonhosted.org/packages/py2.py3/${_name::1}/$_name/${_name//-/_}-$pkgver-py2.py3-none-any.whl")
sha256sums=('f3f4d6431656c0122906888afe1b67b4400e82bd7f254b45b92e6c5b84ea8e3e')

package() {
  python -m installer --destdir="$pkgdir" "$srcdir/${_name//-/_}-$pkgver-py2.py3-none-any.whl"
}
