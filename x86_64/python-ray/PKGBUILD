# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
_base=ray
pkgname=python-${_base}
pkgver=2.50.0
pkgrel=2
pkgdesc="A fast and simple framework for building and running distributed applications"
arch=(x86_64)
url="https://github.com/${_base}-project/${_base}"
license=(Apache-2.0)
depends=(psmisc python-click python-filelock python-jsonschema python-msgpack
  python-packaging python-protobuf python-pyaml python-requests libxcrypt-compat)
makedepends=(python-build python-installer python-setuptools-scm python-wheel cython bazelisk unzip git)
optdepends=('python-pandas: for ray[data, tune, rllib]'
  'python-fsspec: for ray[data, tune, rllib]'
  'python-aiohttp: for ray[default, serve]'
  'python-aiohttps-cors: for ray[default, serve]'
  'python-colorful: for ray[default, serve]'
  'py-spy: for ray[default, serve]'
  'python-opencensus: for ray[default, serve]'
  'python-prometheus_client: for ray[default, serve]'
  'python-smart-open: for ray[default, serve]'
  'python-virtualenv: for ray[default, serve]'
  'uvicorn: for ray[serve]'
  'python-starlette: for ray[serve]'
  'python-fastapi: for ray[serve]'
  'python-tensorboardx: for ray[tune, rllib]'
  'python-opentelemetry-api: for ray[observability]'
  'python-opentelemetry-sdk: for ray[observability]'
  'python-opentelemetry-exporter-otlp: for ray[observability]'
  'python-dm-tree: for ray[rllib]'
  'python-gymnasium: for ray[rllib]'
  'python-lz4: for ray[rllib]'
  'python-scipy: for ray[rllib]'
  'python-typer: for ray[rllib]'
  'python-rich: for ray[rllib]'
)
source=(${_base}-${_base}-${pkgver}.tar.gz::${url}/archive/${_base}-${pkgver}.tar.gz)
sha512sums=('ec19884076936d35810acf8ce3cad52457a9d0158dd2d0f04a22d8ce3d5349ce840074e0ef99e8faa2049de20e7072bdab5c4a4f57e99e7b38fa29b355068fd5')

prepare() {
  # https://github.com/ray-project/ray/pull/56243
  sed -i '16i #include <cstdint>' ${_base}-${_base}-${pkgver}/src/ray/observability/open_telemetry_metric_recorder.h
}

build() {
  cd ${_base}-${_base}-${pkgver}/python
  export SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver}
  SKIP_THIRDPARTY_INSTALL_CONDA_FORGE=1 python -m build --wheel --skip-dependency-check --no-isolation
}

package() {
  cd ${_base}-${_base}-${pkgver}/python
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 ../LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
