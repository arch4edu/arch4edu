# Maintainer: Matthew McGinn <mamcgi@gmail.com>
# Contributor: Gryffyn
# Contributor: Tetsumi

pkgname=python-pygame
_name=pygame
pkgver=1.9.6
pkgrel=1
pkgdesc="Python game library"
arch=('i686' 'x86_64')
url="http://www.pygame.org"
license=('LGPL')
makedepends=('python-setuptools')
depends=('python' 'sdl_mixer' 'sdl_ttf' 'sdl_image' 'portmidi')
provides=('python-pygame')

source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")

md5sums=('36f8817874f9e63acdf12914340b60e9')

package() 
{
  cd ${_name}-${pkgver}
  python setup.py install --root="${pkgdir}" --prefix=/usr
}
