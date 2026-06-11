# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Contributor: Maarten van Gompel <proycon at anaproy dot nl>
# Contributor: Lex Black <autumn-wind at web dot de>
# Contributor: Dieter_be

pkgname=python-gensim
_pkgname=gensim
pkgver=4.4.0
pkgrel=1
pkgdesc="Library for topic modelling, document indexing and similarity retrieval with large corpora"
arch=('i686' 'x86_64')
license=('LGPL2.1')
url="https://radimrehurek.com/gensim/"
depends=('python-numpy' 'python-scipy' 'python-smart_open')
optdepends=("python-pyro: Usage in a distributed environment")
makedepends=('python-setuptools' 'python-wheel' 'python-pip' 'cython')
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/RaRe-Technologies/${_pkgname}/archive/${pkgver}.tar.gz")
sha512sums=('216bcea37421a7ef4a95616e334f0d8829e0c95d996c3c1d1753483158483557ac1f3b0b4b031a149573f9f007112e7defbc881edca28825d4679b38cf5c2517')

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
