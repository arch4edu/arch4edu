# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=requests
pkgname=pypy3-${_base}
pkgdesc="A simple, yet elegant, HTTP library"
pkgver=2.32.4
pkgrel=1
arch=(any)
url="https://github.com/psf/${_base}"
license=(Apache-2.0)
depends=(ca-certificates pypy3-charset-normalizer pypy3-idna pypy3-urllib3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz
  https://gitlab.archlinux.org/archlinux/packaging/packages/python-${_base}/-/raw/${pkgver}-1/certs.patch)
sha512sums=('7638061283a5e66c51f26107f5a88d090d35feecbf5a9075af842b67c0abd727af855346e2385130fa79738395a3821107be300e3de60a9a0e84fe69904288cd'
            'a13b112e12bb7f64edb2c6b7d3a34ffce660e6d654fb085016e6e67af5001be35f77da4eaccd065444d2ad849ebd8e4b5261d83dea5c3b83a44fb8b402706ba3')

prepare() {
  cd ${_base}-${pkgver}
  sed -i '/certifi/d' setup.py
  patch -p1 -i ../certs.patch
}

build() {
  cd ${_base}-${pkgver}
  pypy3 -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" pypy3 -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
