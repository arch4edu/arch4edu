# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Contributor: Maarten van Gompel <proycon at anaproy dot nl>

pkgname=python-smart_open
_pkgname=smart_open
pkgver=8.0.1
pkgrel=1
pkgdesc="Library for efficient streaming of very large files from/to S3, HDFS, WebHDFS, HTTP, or local (compressed) files"
arch=('any')
license=('MIT')
url="https://github.com/RaRe-Technologies/smart_open"
depends=("python-wrapt")
optdepends=("python-boto3: AWS support"
	"python-requests: HTTP support"
	"python-paramiko: SSH support"
	"python-zstandard: zstd support")
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools' 'python-setuptools-scm')
provides=("python-smart-open")
conflicts=("python-smart-open")
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/RaRe-Technologies/${_pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=('c36217882ac7dbde73d9ffd02d3bfd077f09b64e1a4e076503f1f19b601b799d08d9a09498db1d37201ff2cac0957d813158c8b6d8d449fbe9bfea9322918fed')

build() {
	cd "${srcdir}/${_pkgname}-${pkgver}"
	python -m build --wheel --no-isolation
}

package() {
	cd "${srcdir}/${_pkgname}-${pkgver}"
	python -m installer --destdir="${pkgdir}" dist/*.whl

	install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
