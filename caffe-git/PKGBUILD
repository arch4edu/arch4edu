# Maintainer : Daniel Bermond < gmail-com: danielbermond >
# Contributor: Drew Noel <drewmnoel@gmail.com>
# Contributor: Jonathan Yantis

pkgname=caffe-git
_srcname=caffe
pkgver=1.0.r132.g99bd99795
pkgrel=7
pkgdesc='A deep learning framework made with expression, speed, and modularity in mind (cpu only, git version)'
arch=('i686' 'x86_64')
url='https://caffe.berkeleyvision.org/'
license=('BSD')
depends=(
    # official repositories:
        'openblas' 'lapack' 'boost-libs' 'protobuf' 'google-glog' 'gflags'
        'hdf5' 'opencv' 'leveldb' 'lmdb' 'python' 'cython'
        'python-numpy' 'python-scipy' 'python-matplotlib' 'ipython'
        'python-h5py' 'python-networkx' 'python-nose' 'python-pandas'
        'python-dateutil' 'python-protobuf' 'python-gflags' 'python-yaml'
        'python-pillow' 'python-six'
    # AUR:
        'python-leveldb' 'python-scikit-image' 'python-pydotplus'
    # NOTE:
    # python-pydotplus (or python-pydot) is required by python executable 'draw_net.py'
    # https://github.com/BVLC/caffe/blob/99bd99795dcdf0b1d3086a8d67ab1782a8a08383/python/caffe/draw.py#L7-L22
)
makedepends=('git' 'boost' 'doxygen' 'texlive-core')
provides=('caffe' 'caffe-cpu-git')
conflicts=('caffe' 'caffe-cpu-git')
replaces=('caffe-cpu-git')
source=('git+https://github.com/BVLC/caffe.git'
        'Makefile.config'
        'caffe-git-opencv4-fix.patch')
sha256sums=('SKIP'
            '78137e80f764f51c0d4eeed5ce566f3745614b572b481c50197199291d34e2cd'
            '2072c8ca1393b53ef280a15c43af940cc9bf1419ae32b3d8a6541b10b8cb50e9')

prepare() {
    cp -af "${srcdir}/Makefile.config" "${srcdir}/${_srcname}"
    
    # fix build with opencv 4.0
    cd "$_srcname"
    patch -Np1 -i "${srcdir}/caffe-git-opencv4-fix.patch"
}

pkgver() {
    cd "$_srcname"
    
    # git, tags available
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
    cd "$_srcname"
    
    make all pycaffe
    rm -rf doxygen
    make docs distribute
}

check() {
    cd "$_srcname"
    make test runtest
}

package() {
    cd "${_srcname}/distribute"
    
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
    
    cd "${srcdir}/${_srcname}"
    
    # docs
    cp -a doxygen/html "${pkgdir}/usr/share/doc/${pkgname}"
    
    # license
    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
