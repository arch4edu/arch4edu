# Maintainer: Tong Chunli<t.cunly at 163 dot com>
pkgname=python-colcon-library-path
pkgver=0.2.1
pkgrel=1
pkgdesc="An extension for colcon-core to set an environment variable to find shared libraries at runtime."
arch=(any)
url="https://pypi.org/project/colcon-library-path/"
license=('Apache')
depends=('python-colcon-core')
makedepends=('python-setuptools')
source=(https://files.pythonhosted.org/packages/7a/72/1427af79ac1265103b58ff6fbacd75d325f590ec0e3c1c98027ebd1fff12/colcon-library-path-0.2.1.tar.gz)
sha256sums=('8288fc911aab5682771b45fff6437adefefbd30adf38acd2adffeccf4a24e9e2')


package() {
    cd ${srcdir}/colcon-library-path-${pkgver}

    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1 || echo "Not A Problem"
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
}
