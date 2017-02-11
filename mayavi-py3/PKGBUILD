# $Id$
# Mainteiner: Alex Maystrenko <alexeytech@gmail.com>

pkgname=mayavi-py3
pkgver=4.5.0
pkgrel=1
pkgdesc="A 3-dimensional visualizer of scientific data, build with python3 bindings"
arch=('i686' 'x86_64')
url="https://github.com/enthought/mayavi"
license=('BSD')
depends=('vtk-py3-qt4' 'python-traitsui' 'python-configobj' 'python-envisage' 'wxpython')
makedepends=('python-setuptools' 'python-sphinx' 'python-mock')
provides=('python-mayavi')
options=(!emptydirs)

source=("$pkgname-$pkgver.tar.gz::https://github.com/enthought/mayavi/archive/${pkgver}.tar.gz"
        vtk7-hack.patch
        python35-ast.patch)
md5sums=('ed3b0004b810bd5741ae9bb46d197250'
         'd85d1b681b687a11399b3109f1486ff6'
         '2e8da054570d81f830e5d7a840d3bd09')

prepare() {
   cd "$srcdir"/mayavi-$pkgver
   patch -p1 < ../vtk7-hack.patch
   patch -p1 < ../python35-ast.patch
}

build() {
  cd "$srcdir"/mayavi-$pkgver

  rm -rf build
  mkdir build
  python setup.py build

}

package() {
  cd "$srcdir"/mayavi-$pkgver
  python setup.py install --skip-build --root="$pkgdir"/ --optimize=1


  # install manpage
  mkdir -p "${pkgdir}"/usr/share/man/man1
  cp -p docs/mayavi2.man "${pkgdir}"/usr/share/man/man1/mayavi2.1
  install -D LICENSE.txt "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}
