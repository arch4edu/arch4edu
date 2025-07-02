# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Contributor: Maarten van Gompel <proycon at anaproy dot nl>

pkgname=python-smart_open
_pkgname=smart_open
pkgver=7.3.0
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
sha512sums=('220c31f9057cb672056ef57cf3f611badc4a38030d1e74d7c30d952bcec44a81c75463bc6068aac0ea8804227369c19291683b39ddc308bcceb1b7a81ff3d58c')

build() {
	cd "${srcdir}/${_pkgname}-${pkgver}"
	python -m build --wheel --no-isolation
}

package() {
	cd "${srcdir}/${_pkgname}-${pkgver}"
	python -m installer --destdir="${pkgdir}" dist/*.whl

	install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
