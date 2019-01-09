# Maintainer: Matthew McGinn <mamcgi@gmail.com>
# Contributor: Gryffyn
# Contributor: Tetsumi

pkgname=python-pygame
_name=pygame
pkgver=1.9.4
pkgrel=1
pkgdesc="Python game library"
arch=('i686' 'x86_64')
url="http://www.pygame.org"
license=('LGPL')
makedepends=('python-setuptools')
depends=('python' 'sdl_mixer' 'sdl_ttf' 'sdl_image' 'portmidi')
provides=('python-pygame')

source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")

md5sums=('35123425da093da331a89ec0dcbd1ac4')

package() 
{
  cd ${_name}-${pkgver}
  python config.py -auto
  python setup.py install --root="${pkgdir}" --prefix=/usr
}
