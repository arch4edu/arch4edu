# Maintainer: Gordian Edenhofer <gordian.edenhofer@gmail.com>
# Contributor: Maarten van Gompel <proycon at anaproy dot nl>
# Contributor: Lex Black <autumn-wind at web dot de>
# Contributor: Dieter_be

pkgname=python-gensim
_pkgname=gensim
pkgver=3.8.3
pkgrel=1
pkgdesc="Library for topic modelling, document indexing and similarity retrieval with large corpora"
arch=('i686' 'x86_64')
license=('LGPL2.1')
url="https://radimrehurek.com/gensim/"
depends=('python-numpy' 'python-scipy' 'python-six' 'python-smart_open')
optdepends=("python-pyro: Usage in a distributed environment")
makedepends=('python-setuptools' 'cython')
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/RaRe-Technologies/${_pkgname}/archive/${pkgver}.tar.gz")
sha512sums=('09a60a53aa1de2c9c23eeaae01503d6b3102d7db6c82a04cb995f1bcd41828692044dd94818175c178d7524bd95382fa9ebd234adc865a4da707519dd80b1109')

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
