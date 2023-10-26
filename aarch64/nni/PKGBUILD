# Maintainer: Jingbei Li <i@jingbei.li>

pkgname=nni
pkgver=3.0
pkgrel=1
pkgdesc="An open source AutoML toolkit for automate machine learning lifecycle, including feature engineering, neural architecture search, model compression and hyper-parameter tuning."
arch=('x86_64' 'aarch64')
url="https://github.com/microsoft/nni"
license=('MIT')
depends=(python-cloudpickle python-filelock python-json-tricks python-schema python-typeguard python-websockets)
makedepends=(cmake jupyterlab python-installer python-pip python-setuptools python-wheel typescript)
source=("${url}/archive/refs/tags/v${pkgver}.tar.gz")
md5sums=('7888301a35382fc4e9af845795cec7f1')

prepare() {
  cd "$srcdir/${pkgname}-${pkgver}"

  _jupyterlab_ver=$(pacman -Q jupyterlab | sed -e 's/.* //; s/-.*//g')
  sed "s|\"@jupyterlab/builder\": \"3.0.9\"|\"@jupyterlab/builder\": \"${_jupyterlab_ver}\"|" -i ts/jupyter_extension/package.json

  [[ "$CARCH" = "aarch64" ]] && sed "s|_arch = platform.machine()|_arch = 'arm64'|" -i setup_ts.py || :
}

build() {
  cd "$srcdir/${pkgname}-${pkgver}"

  export NNI_RELEASE=${pkgver}
  python setup.py build_ts
  python setup.py bdist_wheel
}

package() {
  cd "$srcdir/${pkgname}-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl

  install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

# vim:set ts=2 sw=2 et:
