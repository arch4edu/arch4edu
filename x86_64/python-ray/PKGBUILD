# Maintainer: acxz <akashpatel2008 at yahoo dot com>

pkgname=python-ray
pkgver=2.0.0
pkgrel=1
pkgdesc='A fast and simple framework for building and running distributed
applications.'
arch=('x86_64')
url='https://ray.io'
license=('Apache-2.0')
depends=(psmisc python python-attrs python-click python-filelock python-grpcio
         python-jsonschema python-msgpack python-numpy python-protobuf
         python-pyaml python-redis)
optdepends=(
            'python-pandas: for ray[data]'
            'python-pyarrow: for ray[data]'
            'python-fsspec: for ray[data]'
            'python-aiohttp: for ray[default, serve]'
            'python-aiosignal: for ray[default, serve]'
            'python-aiohttps_cors: for ray[default, serve]'
            'python-aioredis: for ray[default, serve]'
            'python-colorful: for ray[default, serve]'
            'python-frozenlist: for ray[default, serve]'
            'py-spy: for ray[default, serve]'
            'python-requests: for ray[default, serve, tune]'
            'python-gpustat: for ray[default, serve]'
            'python-opencensus: for ray[default, serve]'
            'python-prometheus-client: for ray[default, serve]'
            'python-smart-open: for ray[default, serve]'
            'uvicorn: for ray[serve]'
            'python-starlette: for ray[serve]'
            'python-fastapi: for ray[serve]'
            'python-pandas: for ray[tune, rllib]'
            'python-tabulate: for ray[tune, rllib]'
            'python-tensorboardx: for ray[tune, rllib]'
            'python-kubernetes: for ray[k8s]'
            'python-urllib3: for ray[k8s]'
            'python-kopf: for ray[k8s]'
            'python-opentelemetry-api: for ray[observability]'
            'python-opentelemetry-sdk: for ray[observability]'
            'python-opentelemetry-exporter-otlp: for ray[observability]'
            'python-dm-tree: for ray[rllib]'
            'python-gym: for ray[rllib]'
            'python-lz4: for ray[rllib]'
            'python-scikit-image: for ray[rllib]'
            'python-pyaml: for ray[rllib]'
            'python-scipy: for ray[rllib]'
           )
makedepends=(python python-build python-installer python-wheel python-setuptools
             python-pip cython bazel)
_pkgname=ray
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/ray-project/ray/archive/${_pkgname}-$pkgver.tar.gz")

sha256sums=('333841d6e8ad328e0bcbaa2a1adc4ea1ddb302016debb955acc23eeb121417bf')

prepare() {
  cd "${srcdir}/${_pkgname}-${_pkgname}-${pkgver}"

  # https://aur.archlinux.org/packages/py-spy#comment-781521
  sed -i "/py-spy/d" python/setup.py
}

build() {
  cd "${srcdir}/${_pkgname}-${_pkgname}-${pkgver}/python"
  python -m build --wheel --no-isolation
}

package() {
  cd "${srcdir}/${_pkgname}-${_pkgname}-${pkgver}/python"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
