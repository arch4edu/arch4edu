# Maintainer: Tong Chunli<t.cunly at 163 dot com>
pkgname=python-colcon-parallel-executor
pkgver=0.2.4
pkgrel=1
pkgdesc="An extension for colcon-core to process packages in parallel."
arch=(any)
url="https://pypi.org/project/colcon-parallel-executor/"
license=('Apache')
depends=('python-colcon-core')
makedepends=('python-setuptools')
source=(https://files.pythonhosted.org/packages/61/c6/4b4c91a398ecf6f8de4fad2d6f13d6289d4f50db471f13d2433737b1c520/colcon-parallel-executor-0.2.4.tar.gz)
sha256sums=('6c04ec240ce0a6b6bae69b13d8859ea1eac03469424fa220be43a99e7d1d3123')


package() {
    cd ${srcdir}/colcon-parallel-executor-${pkgver}

    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
}
