# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Maintainer: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
# Maintainer: Smoolak <smoolak@gmail.com>
# Contributor: acxz <akashpatel2008 at yahoo dot com>
_base=ray
pkgname=python-${_base}
pkgver=2.59.0
pkgrel=3
pkgdesc="A fast and simple framework for building and running distributed applications"
arch=(x86_64)
url="https://github.com/${_base}-project/${_base}"
license=(Apache-2.0)
depends=(glibc libgcc libstdc++ libxcrypt-compat psmisc python python-aiohttp
  python-click python-colorama python-filelock python-jsonschema python-msgpack
  python-packaging python-protobuf python-psutil python-yaml python-requests)
makedepends=(python-build python-installer python-setuptools-scm python-wheel cython bazelisk unzip git nodejs npm)
checkdepends=(python-cryptography python-grpcio python-numpy python-prometheus_client
  python-pytest python-pytest-asyncio python-pytest-timeout)
optdepends=('python-cryptography: for TLS certificates and autoscaler SSH keys'
  'python-grpcio: for ray[client, default, serve]'
  'python-numpy: for ray[data, tune, rllib]'
  'python-typing_extensions: for ray[data, serve, rllib]'
  'python-pytest: for bundled test helpers'
  'python-pandas: for ray[data, tune, rllib]'
  'python-fsspec: for ray[data, tune, rllib]'
  'python-aiohttp-cors: for ray[default, serve]'
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
  'python-opentelemetry-sdk: for ray[default, observability]'
  'python-opentelemetry-exporter-prometheus: for ray[default]'
  'python-opentelemetry-proto: for ray[default]'
  'python-pydantic: for ray[default, tune, train]'
  'python-opentelemetry-exporter-otlp: for ray[observability]'
  'python-dm-tree: for ray[rllib]'
  'python-gymnasium: for ray[rllib]'
  'python-lz4: for ray[rllib]'
  'python-scipy: for ray[rllib]'
  'python-typer: for ray[rllib]'
  'python-rich: for ray[rllib]'
)
source=(${_base}-${_base}-${pkgver}.tar.gz::${url}/archive/${_base}-${pkgver}.tar.gz
  jemalloc-gcc16.patch
  ray-jemalloc-patch-hook.patch
  dlmalloc-gcc16.patch
  ray-no-ci-pypi.patch)
sha512sums=('99801b0eca43fb1a7cb75f964304dd4e6fb02df68d167104dec01bad13074e5d31fce64c63bb6c3538aa66bdb5b52a4d057583969311be8ada3084db8e4b434c'
  '96f356845327ab1d1b8147877d5f3d78c871bcda1ad28c099cfd4e3190ef74c3b8e9d97910d902fa0eb118954ad3c359fea122fa0d4e6e8108c0ec221808f351'
  'e156fdedc0775be785ed7651b83916f6c502eeb07e98a638340923299b2cab7826fc78da2916280a98b042a9294af6bf74b54b01c1838d899a2ca75b0eb74bda'
  '745718484e8932b6eddf29fdc2796a13e4c02c3d4a17b0f27bfb61f35622fbf4eadefc235fc8a6d9229c19bd41c6960bb6506f548f2e5b686b9eb95e91532310'
  'd57f5cefb0ace61d54c7bc229740eaab6681c21a4efd78b62495152892b1beb2558ab238413c1fe112427e6fe7c11420ed90b6d32451caf39333a59e272da114')

prepare() {
  cd ${_base}-${_base}-${pkgver}
  # https://github.com/ray-project/ray/pull/56243
  sed -i '16i #include <cstdint>' src/ray/observability/open_telemetry_metric_recorder.h

  # Preserve dlmalloc's debug-only assertion counter with GCC 16 and NDEBUG.
  patch --fuzz=0 -Np1 -i "$srcdir/dlmalloc-gcc16.patch"
  # Build helpers use existing rules_python sources instead of CI PyPI wheels.
  patch --fuzz=0 -Np1 -i "$srcdir/ray-no-ci-pypi.patch"

  # Backport jemalloc/jemalloc#2900 for GCC 16 to Ray's bundled allocator.
  patch --fuzz=0 -Np1 -i "$srcdir/ray-jemalloc-patch-hook.patch"
  install -Dm644 "$srcdir/jemalloc-gcc16.patch" thirdparty/patches/jemalloc-gcc16.patch

  # Use the canonical registry for the existing locked archives. Keep all
  # upstream versions and integrity checksums unchanged.
  sed -i "s|https://registry.npmmirror.com/|https://registry.npmjs.org/|g" \
    python/ray/dashboard/client/package-lock.json

  # Vendored Python dependencies are disabled below and supplied by depends.
  # pip is only used to install those vendored copies, not to build the wheel.
  sed -i 's/"cython >= 3.0.12", "pip", "wheel"/"cython >= 3.0.12", "wheel"/' python/setup.py
}

build() {
  # The wheel only includes dashboard assets when they are built beforehand.
  # Use the upstream lockfile and omit dependency lifecycle scripts.
  cd ${_base}-${_base}-${pkgver}/python/ray/dashboard/client
  npm ci --ignore-scripts --no-audit --no-fund
  npm run build
  test -s build/index.html

  cd "$srcdir"
  cd ${_base}-${_base}-${pkgver}/python
  export SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver}
  local _jobs=${MAX_JOBS:-$(env -u OMP_NUM_THREADS -u OMP_THREAD_LIMIT nproc)}
  export CMAKE_BUILD_PARALLEL_LEVEL=${CMAKE_BUILD_PARALLEL_LEVEL:-$_jobs}
  # Bazel otherwise drops the parallelism limit for RocksDB's nested CMake build.
  export BAZEL_ARGS="${BAZEL_ARGS:---jobs=$_jobs} --action_env=CMAKE_BUILD_PARALLEL_LEVEL"
  SKIP_THIRDPARTY_INSTALL_CONDA_FORGE=1 python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd ${_base}-${_base}-${pkgver}
  local _source=$PWD
  (
    cd python/ray/dashboard/client
    # SWR's default visibility callback outlives JSDOM in asynchronous UI
    # tests. Preserve normal visibility behavior and treat a destroyed test
    # document as hidden, as required by the browser lifecycle.
    # https://github.com/vercel/swr/issues/2373
    python - <<'PYTESTFIXTURE'
from pathlib import Path
fixture = Path("src/util/test-utils.tsx")
text = fixture.read_text()
old = "<SWRConfig value={{ provider: () => new Map() }}>"
new = """<SWRConfig value={{
        provider: () => new Map(),
        isVisible: () => typeof document !== "undefined" && document !== null
          && document.visibilityState !== "hidden",
      }}>"""
assert text.count(old) == 1
fixture.write_text(text.replace(old, new))
PYTESTFIXTURE
    # Upstream's dataset timestamp assertions use Pacific time.
    TZ=America/Los_Angeles CI=true npm test -- --watchAll=false --runInBand
  )
  local _check="$srcdir/check-install"
  local _site
  rm -rf "$_check"
  python -m venv --without-pip --system-site-packages "$_check"
  "$_check/bin/python" -m installer python/dist/ray-${pkgver}-*.whl
  _site=$("$_check/bin/python" -c 'import sysconfig; print(sysconfig.get_path("purelib"))')
  "$_check/bin/python" - "$_site" <<'PY'
import json
from pathlib import Path
import sys

frontend = Path(sys.argv[1]) / "ray/dashboard/client/build"
assert (frontend / "index.html").is_file()
manifest = json.loads((frontend / "asset-manifest.json").read_text())
assert any(name.endswith(".js") for name in manifest["files"])
for value in manifest["files"].values():
    asset = frontend / value.lstrip("/")
    assert asset.is_relative_to(frontend) and asset.is_file(), value
print("Installed dashboard asset manifest: PASS")
PY
  # Upstream excludes its test package from wheels. Stage only the tests beside
  # the installed wheel so subprocess workers can import their test modules.
  cp -a python/ray/tests "$_site/ray/"
  local _tmp
  _tmp=$(mktemp -d /tmp/ray-check.XXXXXX)
  mkdir -p "$_tmp/home" "$_tmp/tmp"
  (
    export PATH="$_check/bin:$PATH"
    export PYTHONPATH="$_site/ray/tests:$_site"
    export HOME="$_tmp/home" TMPDIR="$_tmp/tmp" RAY_TMPDIR="$_tmp"
    export RAY_USAGE_STATS_ENABLED=0 RAY_MINIMAL=1
    cd "$_tmp"
    # Representative CPU scope: labels/paths, worker scheduling, object-store
    # round trips, nested tasks and NumPy/dataclass serialization. Optional ML
    # backends, GPU workloads and pip-created runtime environments are separate.
    python -m pytest -c "$_source/pytest.ini" --import-mode=prepend -ra \
      "$_site/ray/tests/test_path_utils.py" \
      "$_site/ray/tests/test_label_utils.py" \
      "$_site/ray/tests/test_basic.py::test_release_cpu_resources" \
      "$_site/ray/tests/test_basic.py::test_put_get" \
      "$_site/ray/tests/test_basic.py::test_nested_functions" \
      "$_site/ray/tests/test_basic.py::test_recursive_remote_call" \
      "$_site/ray/tests/test_basic.py::test_base_exception_raised" \
      "$_site/ray/tests/test_serialization.py::test_simple_serialization" \
      "$_site/ray/tests/test_serialization.py::test_numpy_serialization" \
      "$_site/ray/tests/test_serialization.py::test_usage_with_dataclass"
  )
  rm -rf "$_tmp"
}

package() {
  cd ${_base}-${_base}-${pkgver}/python
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 ../LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
