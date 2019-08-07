# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Contributor: Maarten van Gompel <proycon at anaproy dot nl>
# Contributor: Lex Black <autumn-wind at web dot de>
# Contributor: Dieter_be

pkgbase=python-gensim
pkgname=('python-gensim' 'python2-gensim')
_pkgname=gensim
pkgver=3.8.0
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
sha512sums=('2f952e847dca5210a79c10a420cb64bceef241fe34f23a9680265569193f4c35d14c708fc0ec395b1fd258f92cb88087430277d2f432be6ae94fd85c8a272b71')

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
