# Maintainer: Phil Schaf <flying-sheep@web.de>
_name=pydot
pkgname=python-$_name
pkgver=1.2.3
pkgrel=1
pkgdesc='Python interface to Graphviz’s Dot language'
arch=('any')
url='https://github.com/erocarrera/pydot'
license=('MIT')
depends=('python' 'python-pyparsing' 'graphviz')
makedepends=('python-setuptools')
provides=('python-dot')
conflicts=('python-dot')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
md5sums=('5b50fd8cf022811d8718562ebc8aefb2')

package() {
	cd "$srcdir/$_name-$pkgver"
	
	python setup.py install --root="$pkgdir" || return 1
	install -D -m644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
