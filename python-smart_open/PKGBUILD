# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Contributor: Maarten van Gompel <proycon at anaproy dot nl>

pkgname=python-smart_open
_pkgname=smart_open
pkgver=3.0.0
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
sha512sums=('65d4483bc53831cca60f789dd2e48a1f8a81ba8c023e95c2dce081958a761cfaca9662c1d098d09ce0182bff94af8a8c582e390ef0a74d092d4bc687f3dce982')

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
