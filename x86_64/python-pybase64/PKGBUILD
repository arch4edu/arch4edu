# Maintainer: Smoolak <smoolak@gmail.com>
# Contributor: envolution
# Contributor: irmluity <45vw4yz8g@mozmail.com>
# shellcheck shell=bash disable=SC2034,SC2154,SC2164

pkgname=python-pybase64
_pkgname=pybase64
pkgver=1.5.1
pkgrel=1
pkgdesc="Fast Base64 encoding/decoding in Python"
arch=(x86_64)
url="https://github.com/mayeut/pybase64"
license=('BSD-2-Clause')
depends=(
  glibc
  python
)
makedepends=(
  git
  cmake
  python-build
  python-installer
  python-setuptools
  python-wheel
)
checkdepends=(
  'python-pytest'
  'python-packaging'
  'python-typing_extensions'
)
provides=("${_pkgname}")
_base64_commit=bf058e571ac5002b75b03fed38e33ed4e8d45eff
source=(
  "${_pkgname}-${pkgver}::git+https://github.com/mayeut/pybase64.git#tag=v${pkgver}"
  "git+https://github.com/aklomp/base64.git#commit=${_base64_commit}"
)
sha256sums=('SKIP' 'SKIP')

prepare() {
  cd "${_pkgname}-${pkgver}"
  git submodule init
  git config submodule.base64.url "$srcdir/base64"
  git -c protocol.file.allow=always submodule update
}
build() {
  cd "${_pkgname}-${pkgver}"
  CIBUILDWHEEL=1 python -m build --wheel --no-isolation
}

check() {
  cd "${_pkgname}-${pkgver}"
  local _check="$srcdir/_check"
  local _run="$srcdir/_check-run"
  local _site

  rm -rf "$_check" "$_run"
  python -m installer --destdir="$_check" dist/*.whl
  _site="$_check/usr/lib/python$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')/site-packages"
  mkdir -p "$_run"
  cp -a tests "$_run/"
  cp conftest.py "$_run/"

  cd "$_run"
  CIBUILDWHEEL=1 PATH="$_check/usr/bin:$PATH" PYTHONNOUSERSITE=1 PYTHONPATH="$_site:$_run" \
    python -P -m pytest \
      -c "$srcdir/${_pkgname}-${pkgver}/pyproject.toml" \
      --rootdir="$_run" \
      --import-mode=importlib \
      tests

  CHECK_SITE="$_site" CHECK_RUN="$_run" PYTHONNOUSERSITE=1 PYTHONPATH="$_site" python -P <<'PY'
import base64
import os
from pathlib import Path

import pybase64

site = Path(os.environ["CHECK_SITE"]).resolve()
run = Path(os.environ["CHECK_RUN"]).resolve()
assert Path(pybase64.__file__).resolve().is_relative_to(site)
assert "C extension active" in pybase64.get_version()

payload = bytes(range(256)) * 4096 + b"\x00Arch Linux\xff"
standard = pybase64.standard_b64encode(payload)
urlsafe = pybase64.urlsafe_b64encode(payload)
assert standard == base64.standard_b64encode(payload)
assert urlsafe == base64.urlsafe_b64encode(payload)
assert pybase64.standard_b64decode(standard) == payload
assert pybase64.urlsafe_b64decode(urlsafe) == payload
(run / "input.bin").write_bytes(payload)
PY

  PYTHONNOUSERSITE=1 PYTHONPATH="$_site" "$_check/usr/bin/pybase64" encode \
    --url "$_run/input.bin" --output "$_run/encoded.txt"
  PYTHONNOUSERSITE=1 PYTHONPATH="$_site" "$_check/usr/bin/pybase64" decode \
    --url "$_run/encoded.txt" --output "$_run/decoded.bin"
  cmp "$_run/input.bin" "$_run/decoded.bin"
  PYTHONNOUSERSITE=1 PYTHONPATH="$_site" "$_check/usr/bin/pybase64" --version |
    grep -F 'C extension active'
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/python-${_pkgname}/"
}

# vim:set ts=2 sw=2 et:
