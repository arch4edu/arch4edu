# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Contributor: Maarten van Gompel <proycon at anaproy dot nl>

pkgname=python-smart_open
_pkgname=smart_open
pkgver=7.0.4
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
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools')
provides=("python-smart-open")
conflicts=("python-smart-open")
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/RaRe-Technologies/${_pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=('285348acbf0f829bbeb942cc00877f9fcd0fcfbe002553927c13f2885ccab3f49571e83c7d7b83894bda602e23548dde215713f05a73aba9d0e101708ace322e')

build() {
	cd "${srcdir}/${_pkgname}-${pkgver}"
	python -m build --wheel --no-isolation
}

package() {
	cd "${srcdir}/${_pkgname}-${pkgver}"
	python -m installer --destdir="${pkgdir}" dist/*.whl

	install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
