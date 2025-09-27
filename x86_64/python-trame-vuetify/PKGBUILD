# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=trame-vuetify
_npm_base=vuetify
_npm_font_base=@mdi/font
pkgname=python-${_base}
pkgdesc="Vuetify widgets for trame"
pkgver=3.1.0
_npm_pkgver=3.7.6
_npm_font_pkgver=7.4.47
pkgrel=1
arch=(any)
url="https://github.com/Kitware/${_base}"
license=(MIT)
depends=(python-trame-client)
makedepends=(python-build python-installer python-setuptools python-wheel nodejs npm)
checkdepends=(python-pytest python-trame-server)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz
  https://registry.npmjs.org/${_npm_base}/-/${_npm_base}-${_npm_pkgver}.tgz
  https://registry.npmjs.org/${_npm_font_base}/-/${_npm_font_base:5:4}-${_npm_font_pkgver}.tgz)
sha512sums=('d9e4a950aa8e16a67c4f2b0bbde32bfa16d8bc39ed09b2da929e8994106553c861040b618f1dce4a5f6485c4a83770f86a9315b87d8cd14fec06993ebf6286b3'
            '96897455ae47b4c22a65f8dc7120f90cbbf9bf7d51fdab095f373ab3b50bcb9d4f1ebd438d7c56ca565e8e1ab4915a4c196eb832257516603fa7c79841f3967d'
            'e3732d1a9779f3948dcc764f718a30bbff38573d9ada0df54ef3cc4e6f6e4e20925b36a1790c9251c4b2507ff8e9f3e7b8f416a1fdb2774a4606dcde7bf2105b')

prepare() {
  sed -i 's/^include/#include/' ${_base}-${pkgver}/MANIFEST.in
  mkdir -p ${_base}-${pkgver}/${_base/-/_}/module/vue3-serve/{fonts,css}
  mv ${srcdir}/package/dist/${_npm_base}.min.css ${srcdir}/${_base}-${pkgver}/${_base/-/_}/module/vue3-serve/${_npm_base}3.css
  mv ${srcdir}/package/dist/${_npm_base}.min.js ${srcdir}/${_base}-${pkgver}/${_base/-/_}/module/vue3-serve/${_npm_base}3.js
  mv ${srcdir}/package/css/materialdesignicons.min.css ${srcdir}/${_base}-${pkgver}/${_base/-/_}/module/vue3-serve/css/mdi.css
  mv ${srcdir}/package/fonts/materialdesignicons-webfont.woff2 ${srcdir}/${_base}-${pkgver}/${_base/-/_}/module/vue3-serve/fonts
}

build() {
  cd ${srcdir}/${_base}-${pkgver}/vue2
  npm install
  npm run build

  # cd ${srcdir}/${_base}-${pkgver}/vue3
  # npm install
  # npm run build

  cd ${srcdir}/${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

check() {
  cd ${_base}-${pkgver}
  python -m venv --system-site-packages test-env
  test-env/bin/python -m installer dist/*.whl
  test-env/bin/python -m pytest
}

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"

  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm ${pkgdir}${site_packages}/trame/__init__.py
  rm ${pkgdir}${site_packages}/trame/modules/__init__.py
  rm ${pkgdir}${site_packages}/trame/ui/__init__.py
  rm ${pkgdir}${site_packages}/trame/widgets/__init__.py
}
