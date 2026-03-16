# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Contributor: Maarten van Gompel <proycon at anaproy dot nl>

pkgname=python-smart_open
_pkgname=smart_open
pkgver=7.5.1
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
sha512sums=('390ae0e31af6d237c0fe63cf2412531b7ebe6f5b7d015f49384ac09b96950c1a7967307b00875e0a824c46cc3a90a1aaeec6b135bfb787b5afda605ed1263d57')

build() {
	cd "${srcdir}/${_pkgname}-${pkgver}"
	python -m build --wheel --no-isolation
}

package() {
	cd "${srcdir}/${_pkgname}-${pkgver}"
	python -m installer --destdir="${pkgdir}" dist/*.whl

	install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
