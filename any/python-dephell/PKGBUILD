# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Caleb Maclennana <caleb@alerque.com>
# Contributor: Eli Schwartz <eschwartz@archlinux.org>
_pyname=dephell
pkgname=python-dephell
pkgver=0.8.3
pkgrel=8
pkgdesc="universal Python project management: convert between formats, build, manage venvs"
arch=(any)
url="https://github.com/dephell/$_pyname"
license=(ISC)
_dhdeps=(archive
         argparse
         changelogs
         discover
         licenses
         links markers
         pythons
         setuptools
         shells
         specifier
         venvs
         versioning)
_pydeps=(aiohttp
         appdirs
         attrs
         bowler
         cerberus
         colorama
         "${_dhdeps[@]/#/dephell-}"
         html5lib
         jinja
         m2r2
         packaging
         pip
         pygments
         requests
         ruamel-yaml
         tabulate
         tomlkit
         yaspin)
depends=("${_pydeps[@]/#/python-}")
checkdepends=(git python-pytest python-aioresponses python-requests-mock
              python-moreorless python-graphviz)
optdepends=('python-aiofiles: speed up file writes for files downloaded from warehouse'
            'python-docker: for the docker subcommand'
            'python-dockerpty: for the docker subcommand'
            'python-gnupg: for the package verify subcommand'
            'python-graphviz: print deps tree as a graph'
            'autopep8: make setup.py converter produce formatted pep8 output'
            'yapf: make setup.py converter produce google yapf-formatted output')
_archive="$_pyname-$pkgver"
source=("https://files.pythonhosted.org/packages/source/${_pyname:0:1}/${_pyname}/$_archive.tar.gz"
        'new-pip-parser-api.patch'
        '0001-Do-not-override-the-system-SSL-certificates-with-the.patch')
sha256sums=('a9fcc528a0c6f9f5d721292bdf846e5338e4dca7cd6fef1551fbe71564dfe61e'
            '85ac9db84375d9063fae8cbc91ad7cbcec5b0da8cfe800ed400bcc92f0412934'
            'acbe38854daef23a6cb752bfa98323ae5c7f85cca8562cb070d59e11e05991b0')
b2sums=('7ab8e2022134ff11a39476e121388e627b434b5568bd39879f60a9f14cb27cfee153d27df880fd755c5ab0b0c44fa960a9330df4d2bb15c55b03ffaaa600cbf2'
        'f6f32fbddb21fb263541f6025b9bd111354f39ad2624fa1830d962f40915948bf2bfcc678b9cc2332b3eae7da7d94555a693e5295507004ba2674831854c60a2'
        'b69a0f264700c93144adddf86ee133ca15a5e373dc077bc9d24010cce6238a779435e48cab41bf47b72482c357e790ac9bafeafb89b85a36c29769601300a2cf')

prepare() {
	cd "$_archive"

	# https://github.com/dephell/dephell/pull/473
	patch -Np1 -i ../new-pip-parser-api.patch

	# bad certifi
	patch -p1 -i ../0001-Do-not-override-the-system-SSL-certificates-with-the.patch

	# don't lock pip version to below pip 20:
	# https://github.com/dephell/dephell/pull/363#issuecomment-606150965
	# because https://github.com/pypa/pip/issues/7629 seems insufficient
	# to hold up non-PyPY platforms :/
	sed -i 's/pip<=19.3.1,>=18.0/pip/' setup.py

        # Use m2r2 instead m2r
        sed -i 's/m2r/m2r2/' dephell/controllers/_readme.py
        sed -i 's/m2r/m2r2/' setup.py
        sed -i 's/m2r/m2r2/' tests/test_repositories/test_warehouse_api.py
        sed -i 's/0.2.1/0.3.3.post2/' tests/test_repositories/test_warehouse_api.py
}

build(){
	cd "$_archive"
	python setup.py build
}

check() {
	cd "$_archive"

	# skip git tests, which rely on being run from dephell's own git repo
	# skip doc test, which tests whether html docs not in the tarball, cover all commands
	python -m pytest \
		-k 'not test_git_git and not test_docs' \
		--no-network \
		--deselect tests/test_actions/test_entrypoints.py::test_smoke_get_entrypoints \
                --deselect tests/test_commands/test_vendor_import.py::test_patch_imports \
                --deselect tests/test_repositories/test_local.py::test_deps_file \
                --deselect tests/test_resolving/test_apply_envs.py::test_not_deep \
                --deselect tests/test_commands/test_inspect_project.py::test_inspect_project_command \
                --deselect tests/test_commands/test_inspect_venv.py::test_inspect_venv_command \
                --deselect tests/test_commands/test_venv_create.py::test_venv_create_command \
                --deselect tests/test_commands/test_venv_destroy.py::test_venv_destroy_command \
                --ignore=tests/test_resolving/test_python_compat.py \
                --ignore=tests/test_converters/test_pip.py \
                --ignore=tests/test_models/test_marker_tracker.py \
                --ignore=tests/test_converters/test_poetrylock.py \
                --ignore=tests/test_models/test_requirement.py \
                --ignore=tests/test_commands/test_build.py \
                --ignore=tests/test_commands/test_deps_convert.py \
                --ignore=tests/test_converters/test_egginfo.py \
                --ignore=tests/test_converters/test_poetry.py
}

package() {
	cd "$_archive"

	python setup.py install --root="$pkgdir" --optimize=1 --skip-build
	install -Dm0644 -t "$pkgdir/usr/share/licenses/$pkgname/" LICENSE

	# make shell completions
	python -c 'from dephell.actions._autocomplete import make_bash_autocomplete as comp; print(comp())' |
		install -Dm0644 /dev/stdin "$pkgdir/usr/share/bash-completion/completions/$_pyname"

	# rewrite zsh completion to support autoloading
	{   printf '#compdef dephell\n'
		python -c 'from dephell.actions._autocomplete import make_zsh_autocomplete as comp; print(comp())' |
			sed 's/^compdef _dephell dephell$/_dephell/'
	} | install -Dm0644 /dev/stdin "$pkgdir/usr/share/zsh/site-functions/_$_pyname"
}
