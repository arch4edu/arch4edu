# Maintainer: Brian Thompson <brianrobt@pm.me>
# Contributor: Daniel Maslowski <info@orangecms.org>
# Contributor: Ke Liu <specter119@gmail.com>

pkgname=python-conda
_name=${pkgname#python-}
pkgver=25.11.0
pkgrel=1
pkgdesc="OS-agnostic, system-level binary package manager and ecosystem https://conda.io"
arch=('any')
url="https://github.com/conda/conda"
license=('BSD-3-Clause')
depends=(
  'python'
  'python-archspec'
  'python-boltons'
  'python-boto3'
  'python-botocore'
  'python-conda-package-handling'
  'python-conda-libmamba-solver'  # this is actually required, do not remove.
  'python-frozendict'
  'python-packaging'
  'python-platformdirs'
  'python-pluggy>=1.0.0'
  'python-pycosat>=0.6.3'
  'python-requests>=2.20.1'
  'python-ruamel-yaml>=0.11.14'
  'python-setuptools-scm'
  'python-tqdm'
)
optdepends=(
  'python-pytest: for running conda tests'
  'python-pytest-mock: for running conda tests'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-hatchling'
  'python-hatch-vcs'
  'python-wheel'
)
provides=(
  'python-conda-env'
)
conflicts=(
  'python-conda-git'
)
options=(!emptydirs)
backup=(etc/conda/condarc)
source=("$url/releases/download/$pkgver/$_name-$pkgver.tar.gz"
        "py-3.13-logging.patch::$url/commit/62196c897df3d7aea7063d0c08d1bf6e6fd91600.patch")
sha256sums=('62aad5c046936b07e3ea44d6d908f2d94b427049420332def421e9c72ff3961e'
            'ffb6ee9cc5572e1a24d547bcaf04ccf987a2f8a6c54321ccd242633454675743')

prepare() {
  cd "$srcdir/$_name-$pkgver" || exit

  patch -p 1 -i "$srcdir/py-3.13-logging.patch"
  sed -i '3s/^/set _CONDA_EXE=\/usr\/bin\/conda\n/' conda/shell/etc/profile.d/conda.csh
  sed -i '3s/^/export CONDA_EXE=\/usr\/bin\/conda\n/' conda/shell/etc/profile.d/conda.sh
  sed -i '8s/^/set -l CONDA_EXE \/usr\/bin\/conda\n/' conda/shell/etc/fish/conf.d/conda.fish
  echo -e 'envs_dirs:\n  - ~/.conda/envs\npkgs_dirs:\n  - ~/.conda/pkgs' > condarc
}

build() {
  cd "$srcdir/$_name-$pkgver" || exit

  python -m build --wheel --no-isolation
}

package() {
  cd "$srcdir/$_name-$pkgver" || exit

  # install package contents
  python -m installer --destdir "$pkgdir" "$srcdir/$_name-$pkgver/dist/$_name-$pkgver-"*.whl
  # patch binary
  sed -i 's/conda\.cli\.main_pip/conda.cli.main/' "$pkgdir/usr/bin/conda"
  # install completions and conda shell function
  mkdir -p "$pkgdir/"{usr/share/fish/functions,etc/profile.d}
  _site_packages="$(python -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')"
  ln -s "$_site_packages/conda/shell/etc/fish/conf.d/conda.fish" "$pkgdir/usr/share/fish/functions/conda.fish"
  ln -s "$_site_packages/conda/shell/etc/profile.d/conda.csh" "$pkgdir/etc/profile.d/conda.csh"
  ln -s "$_site_packages/conda/shell/etc/profile.d/conda.sh" "$pkgdir/etc/profile.d/conda.sh"
  # install config and license
  install -Dm 644 condarc "$pkgdir/etc/conda/condarc"
  install -Dm 644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# vim:set ts=2 sw=2 et:
