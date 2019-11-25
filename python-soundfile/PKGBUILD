# Maintainer: Christopher Arndt <aur at chrisarndt dot de>

_name=SoundFile
pkgname=python-soundfile
pkgver=0.10.3.post1
pkgrel=1
pkgdesc="An audio library based on libsndfile, CFFI and NumPy"
url="https://github.com/bastibe/PySoundFile"
arch=('any')
license=('BSD')
makedepends=('python-setuptools')
depends=('python-cffi' 'libsndfile' 'python-numpy')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('490cff42650733d1832728b937fe99fa1802896f5ef4d61bcf78cf7ebecb107b')


build() {
  cd "${srcdir}/${_name}-${pkgver}"

  python setup.py build
}

package() {
  cd "${srcdir}/${_name}-${pkgver}"

  python setup.py install --root="${pkgdir}" --skip-build --optimize=1

  # install license
  install -Dm644 LICENSE -t "${pkgdir}"/usr/share/licenses/${pkgname}
}
