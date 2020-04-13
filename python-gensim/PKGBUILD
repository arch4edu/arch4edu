# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Contributor: Maarten van Gompel <proycon at anaproy dot nl>
# Contributor: Lex Black <autumn-wind at web dot de>
# Contributor: Dieter_be

pkgname=python-gensim
_pkgname=gensim
pkgver=3.8.2
pkgrel=1
pkgdesc="Library for topic modelling, document indexing and similarity retrieval with large corpora"
arch=('i686' 'x86_64')
license=('LGPL2.1')
url="https://radimrehurek.com/gensim/"
depends=('python-numpy' 'python-scipy' 'python-six' 'python-smart_open')
optdepends=("python-pyro: Usage in a distributed environment")
makedepends=('python-setuptools' 'cython')
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/RaRe-Technologies/${_pkgname}/archive/${pkgver}.tar.gz")
sha512sums=('d6f6352cab49815e97145c7c9fa77f86ba3633d6884d8ba518ddc017bd3d6610c9e3e687353ec5e58040603a91ff89240ed09c9623ff0fb3b0d5d499001218ca')

build() {
	cd "${srcdir}/${_pkgname}-${pkgver}"
	python setup.py clean
	rm -rf build dist
	python setup.py build
}

package() {
	cd "${srcdir}/${_pkgname}-${pkgver}"
	python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
