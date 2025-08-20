# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=requests
pkgname=pypy3-${_base}
pkgdesc="A simple, yet elegant, HTTP library"
pkgver=2.32.5
pkgrel=1
arch=(any)
url="https://github.com/psf/${_base}"
license=(Apache-2.0)
depends=(ca-certificates pypy3-charset-normalizer pypy3-idna pypy3-urllib3)
makedepends=(pypy3-build pypy3-installer pypy3-setuptools)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz
  https://gitlab.archlinux.org/archlinux/packaging/packages/python-${_base}/-/raw/${pkgver}-1/certs.patch)
sha512sums=('ca73dcaec9a12ecd7d16d5f30a9213fc520b9b9d659bd6d35e6f05f7b823e1bf6209c7ae48d5e301974794d92dbc8facb937ce99e22180b28dd80f6f2afa13ae'
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
