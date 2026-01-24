# Maintainer: Aseem Athale <athaleaseem@gmail.com>

_pkgname=tf-keras
pkgname=python-${_pkgname}
pkgver=2.20.1
pkgrel=2
pkgdesc='TensorFlow-specific implementation of the Keras API, which was the default Keras from 2019 to 2023.'
arch=('any')
url='https://github.com/keras-team/tf-keras'
license=('Apache-2.0')
makedepends=('python-build' 'python-installer' 'python-wheel')
depends=('python-absl' 'python' 'python-h5py' 'python-optree' 'python-rich'
         'python-ml-dtypes' 'python-packaging' 'python-numpy' 'python-pandas'
         'python-pillow' 'python-pydot' 'python-scipy' 'python-tensorflow' 'python-yaml'
         'tensorboard')
optdepends=('python-pytorch')
source=("https://files.pythonhosted.org/packages/py3/${_pkgname::1}/$_pkgname/${_pkgname//-/_}-$pkgver-py3-none-any.whl"
        "${_pkgname}-${pkgver}-LICENSE::https://raw.githubusercontent.com/keras-team/${_pkgname}/v${pkgver}/LICENSE")
b2sums=('a02632a1e4c3bbe7c6a173ca249c52d3f1c00224496c12625c85a185003e99ceea21cd9fb346f144576a90d59e7d1cd031a7c768ca50aad4230d4c22b4b2d860'
        'dc6395f606b09f8a2fa6e8d28f8436a9b0d2ee7e43b4033542c55eb1bf26e9e6c01fd53770e825b9e996ef15fd2eb77f1e0524d4fc1a3e8bf52d72de3adbd653')

package() {
    python -m installer --destdir="$pkgdir" *.whl
    install -Dm 644 "${_pkgname}-${pkgver}-LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
