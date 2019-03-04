# Maintainer : Daniel Bermond < gmail-com: danielbermond >

pkgname=caffe-cuda
_srcname=caffe
pkgver=1.0
pkgrel=6
pkgdesc='A deep learning framework made with expression, speed, and modularity in mind (with cuda)'
arch=('x86_64')
url='https://caffe.berkeleyvision.org/'
license=('BSD')
depends=(
    # official repositories:
        'openblas' 'lapack' 'boost-libs' 'protobuf' 'google-glog' 'gflags'
        'hdf5' 'opencv' 'leveldb' 'lmdb' 'cuda' 'cudnn' 'nccl' 'python'
        'cython' 'python-numpy' 'python-scipy' 'python-matplotlib' 'ipython'
        'python-h5py' 'python-networkx' 'python-nose' 'python-pandas'
        'python-dateutil' 'python-protobuf' 'python-gflags' 'python-yaml'
        'python-pillow' 'python-six'
    # AUR:
        'python-leveldb' 'python-scikit-image' 'python-pydotplus'
    # NOTE:
    # python-pydotplus (or python-pydot) is required by python executable 'draw_net.py'
    # https://github.com/BVLC/caffe/blob/1.0/python/caffe/draw.py#L7-L22
)
makedepends=('gcc7' 'boost' 'doxygen' 'texlive-core')
provides=('caffe')
conflicts=('caffe')
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/BVLC/caffe/archive/${pkgver}.tar.gz"
        'Makefile.config'
        'caffe-1.0-opencv4-fix.patch')
sha256sums=('71d3c9eb8a183150f965a465824d01fe82826c22505f7aa314f700ace03fa77f'
            'e3e294f15f46ff46b7243297cb562cd5a5b11d540231eb2874d2c21588ceaf54'
            '2072c8ca1393b53ef280a15c43af940cc9bf1419ae32b3d8a6541b10b8cb50e9')

prepare() {
    cp -af "${srcdir}/Makefile.config" "${srcdir}/${_srcname}-${pkgver}"
    
    # fix build with opencv 4.0
    cd "${_srcname}-${pkgver}"
    patch -Np1 -i "${srcdir}/caffe-1.0-opencv4-fix.patch"
}

build() {
    cd "${_srcname}-${pkgver}"
    
    make all pycaffe
    rm -rf doxygen
    make docs distribute
}

check() {
    cd "${_srcname}-${pkgver}"
    make test runtest
}

package() {
    cd "${_srcname}-${pkgver}/distribute"
    
    local _pythonver
    _pythonver="$(python -c 'import sys; print("%s.%s" %sys.version_info[0:2])')"
    
    mkdir -p "$pkgdir"/usr/{bin,include,lib/python"$_pythonver"/site-packages,share/doc}
    
    # binaries
    install -m755 bin/* "${pkgdir}/usr/bin"
    
    # library
    cp -a lib/libcaffe.so* "${pkgdir}/usr/lib"
    chmod 755 "${pkgdir}/usr/lib"/libcaffe.so.*.*.*
    
    # headers
    cp -a include "${pkgdir}/usr"
    
    # python
    install -m755 python/*.py "${pkgdir}/usr/bin"
    cp -a python/caffe "${pkgdir}/usr/lib/python${_pythonver}/site-packages"
    
    # proto
    install -D -m644 proto/caffe.proto -t "${pkgdir}/usr/share/caffe"
    
    cd "${srcdir}/${_srcname}-${pkgver}"
    
    # docs
    cp -a doxygen/html "${pkgdir}/usr/share/doc/${pkgname}"
    
    # license
    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
