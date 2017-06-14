# Maintainer: Jingbei Li <i@jingbei.li>

pkgname=python-ruamel-yaml-hg
_hgname=yaml
pkgver=0.15.6.r1.498e40e91a0c
pkgrel=1
pkgdesc="YAML parser/emitter that supports roundtrip preservation of comments, seq/map flow style, and map key order"
arch=('i686' 'x86_64')
url="https://bitbucket.org/ruamel/yaml"
license=('MIT')
groups=('devel')
depends=('python')
makedepends=('python-pip' 'mercurial' 'wget')
provides=('python-ruamel-yaml')
conflicts=('python-ruamel-yaml-hg')
source=("hg+$url")
md5sums=('SKIP')

pkgver() {
	cd "${_hgname}"
	hg log -r . --template '{latesttag}.r{latesttagdistance}.{node|short}\n'
}

build() {
	_pkgver=${pkgver/.r*/}
	cd $srcdir
	[ ! -f ruamel.yaml-$_pkgver.tar.gz ] && wget -O ruamel.yaml-$_pkgver.tar.gz "https://pypi.io/packages/source/r/ruamel.yaml/ruamel.yaml-$_pkgver.tar.gz"
	tar zxvf ruamel.yaml-$_pkgver.tar.gz
	cp ruamel.yaml-$_pkgver/setup.py $_hgname
}

package() {
	cd "$srcdir/$_hgname"
	pip install . --root="$pkgdir"
	install -D -m644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
