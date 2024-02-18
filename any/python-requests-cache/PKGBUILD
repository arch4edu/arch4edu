# Maintainer: Jordan Cook <JCook83@gmail.com>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Philipp A. <flying-sheep@web.de>
# Contributor: Benoit Pierre <benoit.pierre@gmail.com>
# Contributor: Simon Legner <Simon.Legner@gmail.com>
# Contributor: Aniket Pradhan <aniket17133[at]iiitd[dot]ac[dot]in>
# Contributor: Roman Haritonov <reclosedev[at]gmail[dot]com>
_base=requests-cache
pkgname=python-${_base}
pkgdesc="A persistent cache for python requests"
pkgver=1.2.0
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=('custom:BSD-2-clause')
depends=(python-requests python-cattrs python-platformdirs python-url-normalize)
makedepends=(python-build python-installer python-poetry-core python-wheel)
optdepends=('python-boto3: Cache backend for Amazon DynamoDB database'
  'python-botocore: Interface for Amazon Web Services'
  'python-pymongo: Cache backend for MongoDB database'
  'python-redis: Cache backend for Redis cache'
  'python-bson: for BSON codec'
  'python-itsdangerous: for pass trusted data to untrusted environments'
  'python-yaml: for bindings yaml support'
  'python-ujson: for JSON serializer for improved performance'
)
checkdepends=(python-pytest python-requests-mock python-responses python-timeout-decorator
  python-time-machine python-rich python-ujson python-itsdangerous)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('b198d282cfd656c432d3a63f4d615191ac1ff97c9563e9bd6945e7a78444601108beb47a0f4a79740c7bd6942c3753f025cd52457e87ece7964229799bbb8fa1')

build() {
  cd ${_base}-${pkgver}
  # Note: set `GIT_CEILING_DIRECTORIES` to prevent poetry
  # from incorrectly using a parent git checkout info.
  # https://github.com/pypa/build/issues/384#issuecomment-947675975
  GIT_CEILING_DIRECTORIES="${PWD}/.." python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd ${_base}-${pkgver}
  python -m pytest --ignore=tests/integration
}

package() {
  cd ${_base}-${pkgver}
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
