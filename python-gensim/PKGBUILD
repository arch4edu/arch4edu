# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Contributor: Maarten van Gompel <proycon at anaproy dot nl>
# Contributor: Lex Black <autumn-wind at web dot de>
# Contributor: Dieter_be

pkgbase=python-gensim
pkgname=('python-gensim' 'python2-gensim')
_pkgname=gensim
pkgver=3.7.2
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
sha512sums=('e519a2cec996488f1ac51f37d564a124a639392c86e4fbb1278904790f5960d71aebcd2d8bea5905889eb274a2d67348836d4fb24100909295ff9df4810a87fd')

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
