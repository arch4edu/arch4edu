# Maintainer: Jordan Cook <JCook83@gmail.com>
# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Philipp A. <flying-sheep@web.de>
# Contributor: Benoit Pierre <benoit.pierre@gmail.com>
# Contributor: Simon Legner <Simon.Legner@gmail.com>
# Contributor: Aniket Pradhan <aniket17133[at]iiitd[dot]ac[dot]in>
# Contributor: Roman Haritonov <reclosedev[at]gmail[dot]com>
_base=requests-cache
pkgname=python-${_base}
pkgdesc="A transparent persistent cache for the requests library"
pkgver=1.0.1
pkgrel=1
arch=(any)
url="https://github.com/${_base}/${_base}"
license=('custom:BSD-2-clause')
depends=(python-requests python-platformdirs python-cattrs python-url-normalize)
makedepends=(python-poetry-core python-build python-installer python-wheel)
optdepends=(
  'python-boto3: Cache backend for Amazon DynamoDB database'
  'python-botocore: Interface for Amazon Web Services'
  'python-pymongo: Cache backend for MongoDB database'
  'python-redis: Cache backend for Redis cache'
  'python-bson: for BSON codec'
  'python-itsdangerous: for pass trusted data to untrusted environments'
  'python-yaml: for bindings yaml support'
  'python-ujson: for JSON serializer for improved performance'
)
checkdepends=(python-pytest python-requests-mock python-responses python-itsdangerous python-ujson python-timeout-decorator python-rich)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('ec5788e31f60fd95e575d01af1163f981757972db6557d7a62da2ca0719e84262cf66cdd9b40c73cca540b92d6b7f6beba1aa42bedba528734c61edf5013ec3d')

build() {
  cd ${_base}-${pkgver}
  # Note: set `GIT_CEILING_DIRECTORIES` to prevent poetry
  # from incorrectly using a parent git checkout info.
  # https://github.com/pypa/build/issues/384#issuecomment-947675975
  GIT_CEILING_DIRECTORIES="${PWD}/.." python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd ${_base}-${pkgver}
  # https://bugs.archlinux.org/task/75188
  python -m pytest --ignore=tests/integration
}

package() {
  cd ${_base}-${pkgver}
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
