pkgname='python-wikiteam3'
pkgver='4.4.6'
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
	'python-pdm-backend'
)
license=('GPL-3.0-or-later')
arch=('any')
source=("https://pypi.io/packages/source/${_src_folder::1}/${pkgname#python-}/${_src_folder}.tar.gz")
sha256sums=('a4ab24d73795b8f33cea8067578c831b0b949484c8b0aa8e88858a3bd003ac9c')

build() {
    cd "${srcdir}/${_src_folder}"
    python -m build --wheel --no-isolation
}

package() {

    cd "${srcdir}/${_src_folder}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
