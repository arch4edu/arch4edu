# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Contributor: Maarten van Gompel <proycon at anaproy dot nl>

pkgname=python-smart_open
_pkgname=smart_open
pkgver=4.1.0
pkgrel=1
pkgdesc="Library for efficient streaming of very large files from/to S3, HDFS, WebHDFS, HTTP, or local (compressed) files"
arch=('any')
license=('MIT')
url="https://github.com/RaRe-Technologies/smart_open"
depends=('python-boto3')
optdepends=("python-bz2file: Handling bz2 files"
	"python-requests: HTTP support")
makedepends=('python-setuptools')
provides=("python-smart-open")
conflicts=("python-smart-open")
replaces=("python-smart-open")
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/RaRe-Technologies/${_pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=('251ad8a17123ff8b58751f28ad7fdfa9d7809787392c72a4f82b7289ca2cbd99284e7acaad9a0efbbaf58ec0f5922eb1917551c5acb5a96e88a0dad8a7c687ad')

build() {
	cd "${srcdir}/${_pkgname}-${pkgver}"
	python setup.py clean
	rm -rf build dist
	python setup.py build
}

package() {
	cd "${srcdir}/${_pkgname}-${pkgver}"
	python setup.py install --root="${pkgdir}" --optimize=1 --skip-build

	install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
