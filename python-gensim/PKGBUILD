# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Contributor: Maarten van Gompel <proycon at anaproy dot nl>
# Contributor: Lex Black <autumn-wind at web dot de>
# Contributor: Dieter_be

pkgbase=python-gensim
pkgname=('python-gensim' 'python2-gensim')
_pkgname=gensim
pkgver=3.7.3
pkgrel=1
pkgdesc="Library for topic modelling, document indexing and similarity retrieval with large corpora"
arch=('i686' 'x86_64')
license=('LGPL2.1')
url="https://radimrehurek.com/gensim/"
depends=('')
makedepends=('python-setuptools' 'python2-setuptools' 'python-numpy' 'python2-numpy' 'cython' 'cython2')
optdepends=("python-pyro: Usage in a distributed environment")
provides=("")
conflicts=("")
replaces=("")
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/RaRe-Technologies/${_pkgname}/archive/${pkgver}.tar.gz")
sha512sums=('d66c7edd06537190980e7d6b621187bc05c011fe2e4eb77c0a7c9d6dd781535c07aa55fe2921549912d27d589c8870866a14693afb0a00fecd04db0509c03817')

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

package_python-gensim() {
	depends=('python-numpy' 'python-scipy' 'python-six' 'python-smart_open')
	optdepends=("python-pyro: Usage in a distributed environment")

	cd "${srcdir}/${_pkgname}-${pkgver}"
	python setup.py install --root="${pkgdir}" --optimize=1
}

package_python2-gensim() {
	depends=('python2-numpy' 'python2-scipy' 'python2-six' 'python2-smart_open')
	optdepends=("python2-pyro: Usage in a distributed environment")

	cd "${srcdir}/${_pkgname}-${pkgver}-py2"
	python2 setup.py install --root="${pkgdir}" --optimize=1
}
