#Maintainer: M0Rf30

pkgname=gyp-git
pkgver=2077.8e8c317
pkgrel=1
pkgdesc="GYP can Generate Your Projects."
url="http://code.google.com/p/gyp/"
arch=('i686' 'x86_64')   
makedepends=('git')
depends=('python2' 'python2-setuptools')
license=('custom')
source=("gyp::git+https://chromium.googlesource.com/external/gyp")
conflicts=('gyp-svn')
replaces=('gyp-svn')

pkgver() {
  cd gyp
  echo $(git rev-list --count master).$(git rev-parse --short master)
}

package() {
  cd gyp
  python2 setup.py install --root=$pkgdir
}

md5sums=('SKIP')
