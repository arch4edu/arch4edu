pkgname='python-wikiteam3'
pkgver=4.4.10
_src_folder=${pkgname#python-}-$pkgver
pkgrel=1
pkgdesc="Tools for downloading and preserving MediaWikis. We archive MediaWikis, from Wikipedia to tiniest wikis."
url="https://github.com/saveweb/wikiteam3"
depends=(
	'python'
	'python-requests'
	'python-internetarchive'
	'python-lxml'
	'python-mwclient'
	'python-file-read-backwards'
	'python-slugify'
	'7zip'
	'zstd'
)
makedepends=(
	'python-build'
	'python-installer'
	'python-wheel'
	'python-uv-build'
)
license=('GPL-3.0-or-later')
arch=('any')
source=("https://pypi.io/packages/source/${_src_folder::1}/${pkgname#python-}/${_src_folder}.tar.gz")
sha256sums=('62b9a8312e1dc241a7a5a6e1a00c79d6c7e2d3ffed9f84412fda7b053d689ed1')

build() {
    cd "${srcdir}/${_src_folder}"
    python -m build --wheel --no-isolation
}

package() {

    cd "${srcdir}/${_src_folder}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
