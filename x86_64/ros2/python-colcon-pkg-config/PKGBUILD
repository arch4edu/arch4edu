# Maintainer: Tong Chunli<t.cunly at 163 dot com>
pkgname=python-colcon-pkg-config
pkgver=0.1.0
pkgrel=1
pkgdesc="An extension for colcon-core to set an environment variable to find pkg-config files."
arch=(any)
url="https://pypi.org/project/colcon-pkg-config/"
license=('Apache')
depends=('python-colcon-core')
makedepends=('python-setuptools')
source=("https://files.pythonhosted.org/packages/7c/3f/9979f90a2dc5fe5da4341fab6c3035aaf885f2bf7177fc9de1ea36f3eacb/colcon-pkg-config-$pkgver.tar.gz")
sha256sums=('81fc46d037159030ba7b23970c573a31cead315f3c2410101a3cec858ec6bfa3')


package() {
    cd ${srcdir}/colcon-pkg-config-${pkgver}

    python setup.py install --root=${pkgdir} --prefix=/usr --optimize=1
    install -D -m644 README.rst -t "${pkgdir}/usr/share/doc/${pkgname}"
}
