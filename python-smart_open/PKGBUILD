# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Contributor: Maarten van Gompel <proycon at anaproy dot nl>

pkgname=python-smart_open
_pkgname=smart_open
pkgver=1.11.1
pkgrel=1
pkgdesc="Library for efficient streaming of very large files from/to S3, HDFS, WebHDFS, HTTP, or local (compressed) files"
arch=('any')
license=('MIT')
url="https://github.com/RaRe-Technologies/smart_open"
depends=('python-requests' 'python-boto3')
optdepends=("python-bz2file: Handling bz2 files")
makedepends=('python-setuptools')
provides=("python-smart-open")
conflicts=("python-smart-open")
replaces=("python-smart-open")
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/RaRe-Technologies/${_pkgname}/archive/${pkgver}.tar.gz")
sha512sums=('ef89f1e65e20c8b80e0a753b4bf1dc6eba610562eaeee6a6d85749744a53e68aeff8c793f3a32249f114eeafa7cdb76f9ceccfa3ea3b536282969541d5b81a8f')

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
