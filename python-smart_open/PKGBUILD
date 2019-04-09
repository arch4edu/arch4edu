# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Contributor: Maarten van Gompel <proycon at anaproy dot nl>

pkgbase=python-smart_open
pkgname=('python-smart_open' 'python2-smart_open')
_pkgname=smart_open
pkgver=1.8.1
pkgrel=1
pkgdesc="Library for efficient streaming of very large files from/to S3, HDFS, WebHDFS, HTTP, or local (compressed) files"
arch=('any')
license=('MIT')
url="https://github.com/RaRe-Technologies/smart_open"
makedepends=('python-setuptools' 'python2-setuptools')
provides=("")
conflicts=("")
replaces=("")
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/RaRe-Technologies/${_pkgname}/archive/${pkgver}.tar.gz")
sha512sums=('ad6de5fd65218f4651423da39970d7e6529e23265b21803ff15041d435201ecf760a2fdab08cc80dc0b3c46a2520b0e48ca66cffd5ab1fd3863aee9d2d1a8f52')

prepare() {
	cp -a "${srcdir}/${_pkgname}-${pkgver}"{,-py2}
}

build() {
	cd "${srcdir}/${_pkgname}-${pkgver}"
	python setup.py clean
	rm -rf build dist
	python setup.py build

	cd "${srcdir}/${_pkgname}-${pkgver}-py2"
	python2 setup.py clean
	rm -rf build dist
	python2 setup.py build
}

package_python-smart_open() {
	depends=('python-requests' 'python-boto' 'python-boto3')
	optdepends=("python-bz2file: Handling bz2 files")
	provides=("python-smart-open")
	conflicts=("python-smart-open")
	replaces=("python-smart-open")

	cd "${srcdir}/${_pkgname}-${pkgver}"
	python setup.py install --root="${pkgdir}" --optimize=1

	install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_python2-smart_open() {
	depends=('python2-requests' 'python2-boto' 'python2-boto3' 'python2-backports.lzma')  # Backported LZMA from python>3.3
	optdepends=("python2-bz2file: Handling bz2 files")
	provides=("python2-smart-open")
	conflicts=("python2-smart-open")
	replaces=("python2-smart-open")

	cd "${srcdir}/${_pkgname}-${pkgver}-py2"
	python2 setup.py install --root="${pkgdir}" --optimize=1

	install -Dm644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
