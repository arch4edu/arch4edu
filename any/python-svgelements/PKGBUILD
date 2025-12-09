# Maintainer: Marco Rubin <marco.rubin@protonmail.com>

_name=svgelements
pkgname=python-$_name
pkgver=1.9.6
pkgrel=2
pkgdesc='Svg Elements Parsing'
arch=(any)
url='https://github.com/meerk40t/svgelements'
license=('MIT')
depends=(python)
optdepends=('python-numpy: enable npoint() to do lightning fast linearization for Shapes'
            'python-pillow: load images with PIL/Pillow'
            'python-scipy: quickly provide the exact correct answer for the arc length')
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pillow python-scipy)
optdepends=('python-numpy: fast linearization for Shapes'
            'python-pillow: load images with SVGImage'
            'python-scipy: exact arc length')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz")
b2sums=('f17649b4934210a3ba8bd48c01ce895b8236908384bb278c5feaf9d346d745f0b02a106b5848c6114827edff4d6cc901e819f086168e5ba8bb02167d50cebfbe')

prepare() {
    cd $_name-$pkgver
    sed -i 's/assertNotAlmostEquals/assertNotAlmostEqual/g' test/test_cubic_bezier.py
    sed -i 's/assertEquals/assertEqual/g' test/test_write.py
}

build() {
    cd $_name-$pkgver
    python -m build --wheel --no-isolation
}

check() {
    cd $_name-$pkgver
    python -m unittest -v
}

package() {
    cd $_name-$pkgver
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
