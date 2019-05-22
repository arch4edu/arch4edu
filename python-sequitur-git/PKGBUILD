# Maintainer: Jingbei Li <i@jingbei.li>
pkgname=python-sequitur-git
_gitname=sequitur-g2p
pkgver=33.ecebf07
pkgrel=1
pkgdesc="Sequitur G2P: A trainable Grapheme-to-Phoneme converter."
arch=('x86_64')
url="https://github.com/${_gitname}/${_gitname}"
license=('GPL2')
depends=('python-numpy')
makedepends=('git' 'python-setuptools' 'swig')
source=("git+$url")
md5sums=('SKIP')

pkgver(){
	cd "${srcdir}/${_gitname}"
	echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

build(){
	cd "${srcdir}/${_gitname}"
	python setup.py build build_ext
}


package(){
	cd "${srcdir}/${_gitname}"
	python setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1
}
