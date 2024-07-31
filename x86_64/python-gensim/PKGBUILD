# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Contributor: Maarten van Gompel <proycon at anaproy dot nl>
# Contributor: Lex Black <autumn-wind at web dot de>
# Contributor: Dieter_be

pkgname=python-gensim
_pkgname=gensim
pkgver=4.3.3
pkgrel=1
pkgdesc="Library for topic modelling, document indexing and similarity retrieval with large corpora"
arch=('i686' 'x86_64')
license=('LGPL2.1')
url="https://radimrehurek.com/gensim/"
depends=('python-numpy' 'python-scipy' 'python-smart_open')
optdepends=("python-pyro: Usage in a distributed environment")
makedepends=('python-setuptools' 'python-wheel' 'python-pip' 'cython')
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/RaRe-Technologies/${_pkgname}/archive/${pkgver}.tar.gz")
sha512sums=('e0f870161b7d0738f9a8eb75f2d06d0c67e47d79332746cb646ef8fc0c843ebf39a153e3e3f90cc8364eea21df250167a5ed13c92828ff0fad4391600c8bb126')

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
