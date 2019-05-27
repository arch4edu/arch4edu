# Maintainer : Daniel Bermond < gmail-com: danielbermond >

_commit='f9f811ebc5abd625d63da79e936d9015497b5f58'

pkgbase=python-nvd3
pkgname=('python-nvd3' 'python2-nvd3')
pkgver=0.15.0
pkgrel=4
pkgdesc='Python wrapper for the NVD3 chart generator'
arch=('any')
url='https://github.com/areski/python-nvd3/'
license=('MIT')
makedepends=('git' 'python' 'python-setuptools' 'python2' 'python2-setuptools')
source=("git+https://github.com/areski/python-nvd3.git#commit=${_commit}")
sha256sums=('SKIP')

prepare() {
    cp -a "$pkgbase" "${pkgbase}-py2"
}

build() {
    printf '%s\n' '  -> Building for Python...'
    cd "$pkgbase"
    python setup.py build
    
    printf '%s\n' '  -> Building for Python2...'
    cd "${srcdir}/${pkgbase}-py2"
    python2 setup.py build
}

check() {
    cd "$pkgbase"
    python setup.py test
    
    cd "${srcdir}/${pkgbase}-py2"
    python2 setup.py test
}

package_python-nvd3() {
    depends=(
        # official repositories:
            'python' 'python-jinja'
        # AUR:
            'python-slugify'
    )
    
    cd "$pkgbase"
    python setup.py install --root="$pkgdir" --skip-build --optimize='1'
    
    install -D -m644 MIT-LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

package_python2-nvd3() {
    pkgdesc='Python2 wrapper for the NVD3 chart generator'
    depends=(
        # official repositories:
            'python2' 'python2-jinja'
        # AUR:
            'python2-slugify'
    )
    
    cd "${pkgbase}-py2"
    python2 setup.py install --root="$pkgdir" --skip-build --optimize='1'
    
    mv "${pkgdir}/usr/bin/nvd3" "${pkgdir}/usr/bin/nvd3-2"
    local _script _script_list
    _script_list=('__init__.py' 'cumulativeLineChart.py' 'discreteBarChart.py'
                  'lineChart.py' 'linePlusBarChart.py' 'lineWithFocusChart.py'
                  'multiBarChart.py' 'multiBarHorizontalChart.py' 'pieChart.py'
                  'scatterChart.py' 'stackedAreaChart.py' 'translator.py'
                  'NVD3Chart.py')
    for _script in "${_script_list[@]}"
    do
        sed -i '1s/$/2/' "${pkgdir}/usr/lib/python2.7/site-packages/nvd3/${_script}"
    done
    
    install -D -m644 MIT-LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
