# Maintainer : Daniel Bermond < yahoo-com: danielbermond >
# Contributor: Drew Noel <drewmnoel@gmail.com>
# Contributor: Jonathan Yantis

pkgname=caffe-git
pkgver=1.0.r132.g99bd99795
pkgrel=1
pkgdesc='A deep learning framework made with expression, speed, and modularity in mind (cpu only, git version)'
arch=('i686' 'x86_64')
url='http://caffe.berkeleyvision.org/'
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
provides=('caffe' 'caffe-cpu' 'caffe-cpu-git')
conflicts=('caffe' 'caffe-cuda' 'caffe-cuda-git' 'caffe-cpu' 'caffe-cpu-git'
           'caffe2' 'caffe2-cuda')
replaces=('caffe-cpu-git')
source=("$pkgname"::'git+https://github.com/BVLC/caffe.git'
        'Makefile.config')
sha256sums=('SKIP'
            '9cbe8ea31d70904ec02a4ca3978aa072c99f10aff0629e7616c51bf4a6ca92f5')

prepare() {
    cd "$pkgname"
    
    local _pythonver
    local _pythonmaj
    local _opencvmaj
    
    _pythonver="$(python --version | awk '{ print $2 }' | grep -o '^[0-9]*\.[0-9]*')"
    _pythonmaj="$(python --version | awk '{ print $2 }' | awk -F'.' '{ print $1 }')"
    _opencvmaj="$(opencv_version | awk -F'.' '{ print $1 }')"
    
    # copy configuration options
    cp -af "${srcdir}/Makefile.config" .
    
    # make sure to use the correct versions of python and opencv
    
    if ! grep -q "python${_pythonver}" Makefile.config
    then
        sed -i "s/python[0-9]*\.[0-9]*/python${_pythonver}/" Makefile.config
    fi
    
    if ! grep -q "boost_python${_pythonmaj}" Makefile.config
    then
        sed -i "/boost_python[0-9]/s/[0-9]/${_pythonmaj}/" Makefile.config
    fi
    
    if ! grep -q "OPENCV_VERSION[[:space:]]:=[[:space:]]${_opencvmaj}" Makefile.config
    then
        sed -i "/OPENCV_VERSION/s/[0-9]*$/${_opencvmaj}/" Makefile.config
    fi
}

pkgver() {
    cd "$pkgname"
    
    # git, tags available
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
    cd "$pkgname"
    
    msg2 "Building target 'all'..."
    make all
    
    msg2 "Building target 'pycaffe'..."
    make pycaffe
    
    msg2 "Building target 'docs'..."
    rm -rf doxygen
    make docs
    
    msg2 "Building target 'distribute'..."
    make distribute
}

# uncomment this block if you want to run the checks/tests
#check() {
#    cd "$pkgname"
#    msg2 "Building target 'test'..."
#    make test
#    msg2 "Making target 'runtest'..."
#    make runtest
#}

package() {
    local _pythonver
    _pythonver="$(python --version | awk '{ print $2 }' | grep -o '^[0-9]*\.[0-9]*')"
    
    mkdir -p "$pkgdir"/usr/{bin,include,lib/python"$_pythonver"/site-packages,share/doc}
    
    cd "${pkgname}/distribute"
    
    # binaries
    install -m755 bin/* "${pkgdir}/usr/bin"
    
    # library
    cp -af lib/libcaffe.so* "${pkgdir}/usr/lib"
    chmod 755 "${pkgdir}/usr/lib"/libcaffe.so.*.*.*
    
    # headers
    cp -af include "${pkgdir}/usr"
    
    # python
    install -m755 python/*.py "${pkgdir}/usr/bin"
    cp -af python/caffe "${pkgdir}/usr/lib/python${_pythonver}/site-packages"
    
    # proto
    install -D -m644 proto/caffe.proto -t "${pkgdir}/usr/share/caffe"
    
    cd "${srcdir}/${pkgname}"
    
    # docs
    cp -af doxygen/html "${pkgdir}/usr/share/doc/${pkgname}"
    
    # license
    install -D -m644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
