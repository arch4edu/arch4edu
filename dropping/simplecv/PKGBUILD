# Maintainer: Jingbei Li <i@jingbei.li>
pkgname=simplecv
pkgver=1.3
pkgrel=3
pkgdesc='Framework for computer (machine) vision in Python, providing a unified, Pythonic interface to image aquisition, conversion, manipulation, and feature extraction.'
url='http://simplecv.org'
license=('BSD')
arch=('any')
depends=('opencv' 'python2-pillow' 'python2-pygame' 'python2-scipy')
makedepends=('python2-setuptools')
optdepends=('ipython2: for using SimpleCV with the IPython Notebook')
source=("http://downloads.sourceforge.net/project/${pkgname}/${pkgver}/SimpleCV-${pkgver}.tar.gz")
sha256sums=('7a0aaf61f357a78429ff4409f75d4ac67b9924f06013245706a3ccfcff8c92b0')

prepare() {
	cd "${srcdir}/SimpleCV"
	sed -e "s|#![ ]*/usr/bin/python[ ]*$|#!/usr/bin/python2|" \
		-e "s|#![ ]*/usr/bin/env python$|#!/usr/bin/env python2|" \
		-e "s|#![ ]*/bin/env python$|#!/usr/bin/env python2|" \
		-i $(find . -name '*.py')
}

build() {
	cd "${srcdir}/SimpleCV"
	python2 setup.py build
}


package() {
	cd "${srcdir}/SimpleCV"
	python2 setup.py install "--root=${pkgdir}" --optimize=1
	install -D --mode=u=rw,go=r LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
