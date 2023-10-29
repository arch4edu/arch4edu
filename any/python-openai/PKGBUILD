# Maintainer: Liam Timms <timms5000@gmail.com>
# Contributor: Mark Wagie <mark dot wagie at proton dot me>
pkgname=python-openai
_name=openai-python
pkgver=0.28.1
pkgrel=1
pkgdesc="Python client library for the OpenAI API"
arch=('any')
url="https://openai.com"
license=('MIT')
depends=('python-aiohttp' 'python-requests' 'python-tqdm')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
optdepends=('python-numpy: Needed for CLI fine-tuning data preparation tool'
            'python-pandas: Needed for CLI fine-tuning data preparation tool'
            'python-pandas-stubs: Needed for type hints for mypy'
            'python-openpyxl: Needed for CLI fine-tuning data preparation tool xlsx format'
            'python-wandb: Support for Weights & Biases'
            'python-scikit-learn: Needed for embedding utils'
            'python-tenacity: embeddings'
            'python-matplotlib: embeddings'
            'python-plotly: embeddings'
            'python-scipy: embeddings')
source=("${_name}-$pkgver.tar.gz::https://github.com/openai/openai-python/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('6f4e0a244cec994c064695ea5d66625623327a942582ff67e885346dc997b4da')

build() {
  cd "${_name}-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_name}-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl

  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"
}

