# Maintainer : Daniel Bermond < yahoo-com: danielbermond >
# Contributor: Drew Noel <drewmnoel@gmail.com>
# Contributor: Jonathan Yantis

# NOTE:
# In order to build with NCCL support, uncomment the NCCL
# lines in 'depends' and 'preprare()'.

pkgname=caffe-git
_srcname=caffe
pkgver=1.0.r29.geffcdb0b6
pkgrel=1
pkgdesc="A deep learning framework made with expression, speed, and modularity in mind (git version, gpu enabled)"
arch=('x86_64')
url="http://caffe.berkeleyvision.org/"
license=('BSD')
depends=(
    # official repositories:
        'boost-libs' 'protobuf' 'google-glog' 'gflags' 'hdf5' 'opencv' 'leveldb'
        'lmdb' 'cuda' 'cudnn' 'python' 'boost' 'cython' 'python-numpy' 'python-scipy'
        'python-matplotlib' 'ipython' 'python-h5py' 'python-networkx' 'python-nose'
        'python-pandas' 'python-dateutil' 'python-protobuf' 'python-gflags'
        'python-yaml' 'python-pillow' 'python-six'
    # AUR:
        # required:
            'openblas-lapack'
        # not required:
            # 'nccl'
        #python:
            'python-leveldb' 'python-scikit-image' 'python-pydotplus'
    # NOTE:
    # python-pydotplus (or python-pydot) is required by python executable draw_net.py
    # https://github.com/BVLC/caffe/blob/eeebdab16155d34ff8f5f42137da7df4d1c7eab0/python/caffe/draw.py#L7-L22
)
makedepends=('git' 'gcc5' 'doxygen' 'texlive-core')
provides=('caffe')
conflicts=('caffe' 'caffe-cpu' 'caffe-cpu-git' 'caffe-dr-git' 'caffe-mnc-dr-git'
           'caffe2' 'caffe2-git' 'caffe2-cpu' 'caffe2-cpu-git')
source=("${pkgname}"::"git+https://github.com/BVLC/caffe.git")
sha256sums=('SKIP')

prepare() {
    cd "$pkgname"
    
    # prepare to configure options in Makefile.config
    cp -f Makefile.config.example Makefile.config
    
    # enable cuDNN acceleration switch
    sed -i '/USE_CUDNN/s/^#[[:space:]]//g' Makefile.config
    
    # enable NCCL acceleration switch
    # sed -i '/USE_NCCL/s/^#[[:space:]]//g' Makefile.config
    
    # strictly enable I/O dependencies
    sed -i '/USE_OPENCV/s/^#[[:space:]]//;/USE_OPENCV/s/0/1/'   Makefile.config
    sed -i '/USE_LEVELDB/s/^#[[:space:]]//;/USE_LEVELDB/s/0/1/' Makefile.config
    sed -i '/USE_LMDB/s/^#[[:space:]]//;/USE_LMDB/s/0/1/'       Makefile.config
    sed -i '/OPENCV_VERSION/s/^#[[:space:]]//g'                 Makefile.config
    
    # use gcc5 (CUDA code requires gcc5)
    sed -i '/CUSTOM_CXX/s/^#[[:space:]]//;/CUSTOM_CXX/s/$/-5/' Makefile.config
    
    # set CUDA directory
    sed -i '/CUDA_DIR/s/\/usr\/local\/cuda/\/opt\/cuda/' Makefile.config
    
    # set OpenBLAS as the BLAS provider and adjust its directories
    sed -i '/BLAS[[:space:]]\:=[[:space:]]atlas/s/atlas/open/'                                 Makefile.config
    sed -i 's/.*BLAS_INCLUDE[[:space:]]\:=[[:space:]]\/path.*/BLAS_INCLUDE := \/usr\/include/' Makefile.config
    sed -i 's/.*BLAS_LIB[[:space:]]\:=[[:space:]]\/path.*/BLAS_LIB := \/usr\/lib/'             Makefile.config
    
    # python3 settings
    _py2inc_line="$(sed -n '/PYTHON_INCLUDE[[:space:]]\:=[[:space:]]\/usr\/include\/python2\.7/='  Makefile.config)"
    _py3inc_line="$(sed -n '/PYTHON_INCLUDE[[:space:]]\:=[[:space:]]\/usr\/include\/python3\.5m/=' Makefile.config)"
    _py3libs_line="$(sed -n '/PYTHON_LIBRARIES/=' Makefile.config)"
    sed -i "$((_py2inc_line))s/^/# /"  Makefile.config # comment python2 lines
    sed -i "$((_py2inc_line+1))s/^/#/" Makefile.config
    sed -i "$((_py3inc_line))s/^#[[:space:]]//"   Makefile.config # uncomment python3 PYTHON_INCLUDE lines
    sed -i "$((_py3inc_line+1))s/^#//"            Makefile.config
    sed -i "$((_py3libs_line))s/^#[[:space:]]//"  Makefile.config # uncomment PYTHON_LIBRARIES line
    sed -i "$((_py3libs_line))s/5/6/"             Makefile.config # change version in PYTHON_LIBRARIES
    sed -i "$((_py3inc_line))s/5/6/"              Makefile.config # change version in python3 PYTHON_INCLUDE
    sed -i "$((_py3inc_line+1))s/5/6/;$((_py3inc_line+1))s/dist/site/" Makefile.config
    
    # use python layers
    sed -i '/WITH_PYTHON_LAYER/s/^#[[:space:]]//g' Makefile.config
    
    # if you want to use python2 _instead_ of python3:
    #     - uncomment this block
    #     - comment the python3 block
    #     - change python3 dependencies to python2
    #     - change python2 directories in package() to python3
    #     - NOTE: do not enable both python2 and python3 blocks. choose only one.
    #     - NOTE: python2 is the Caffe default but this package uses python3 by default
    # python2 settings
    #_py2inc_line="$(sed -n '/PYTHON_INCLUDE[[:space:]]\:=[[:space:]]\/usr\/include\/python2\.7/=' Makefile.config)"
    #sed -i "$((_py2inc_line+1))s/dist/site/" Makefile.config
}

pkgver() {
    cd "$pkgname"
    
    # git, tags available
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
    cd "$pkgname"
    _gcc5_cxxflags="$(printf '%s' "$CXXFLAGS" | sed 's/-fno-plt//')"
    _gcc5_cflags="$(  printf '%s' "$CFLAGS"   | sed 's/-fno-plt//')"
    
    msg2 "Building target 'all'..."
    CXXFLAGS="$_gcc5_cxxflags" CFLAGS="$_gcc5_cflags" make all
    
    msg2 "Building target 'pycaffe'..."
    CXXFLAGS="$_gcc5_cxxflags" CFLAGS="$_gcc5_cflags" make pycaffe
    
    msg2 "Building target 'docs'..."
    rm -rf doxygen
    CXXFLAGS="$_gcc5_cxxflags" CFLAGS="$_gcc5_cflags" make docs
    
    msg2 "Building target 'distribute'..."
    CXXFLAGS="$_gcc5_cxxflags" CFLAGS="$_gcc5_cflags" make distribute
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
    # directories creation
    mkdir -p "${pkgdir}/usr/bin"
    mkdir -p "${pkgdir}/usr/include/caffe/"{layers,proto,test,util}
    mkdir -p "${pkgdir}/usr/lib/python3.6/site-packages/caffe/"{imagenet,proto,test}
    mkdir -p "${pkgdir}/usr/share/"{caffe,doc/"${_srcname}"/search,licenses/"${pkgname}"}
    
    # binaries
    cd "${srcdir}/${pkgname}/distribute/bin"
    install -D -m755 * "${pkgdir}/usr/bin"
    
    # libraries
    cd "${srcdir}/${pkgname}/distribute/lib"
    install -D -m755 *.so "${pkgdir}/usr/lib"
    
    # includes
    cd "${srcdir}/${pkgname}/distribute/include/caffe"
    install -D -m644 *.hpp "${pkgdir}/usr/include/caffe"
    for _dir in layers proto test util
    do
        cd "${srcdir}/${pkgname}/distribute/include/caffe/${_dir}"
        install -D -m644 * "${pkgdir}/usr/include/caffe/${_dir}"
    done
    
    # python
    cd "${srcdir}/${pkgname}/distribute/python"
    install -D -m755 *.py "${pkgdir}/usr/bin"
    rm -rf python # remove duplicated 'python' folder
    
    cd caffe
    for _file in *
    do
        [ -d "$_file" ] && continue # skip directories
        _mode="$(stat --format '%a' "$_file")"
        install -D -m"$_mode" "$_file" "${pkgdir}/usr/lib/python3.6/site-packages/caffe"
    done
    
    for _dir in imagenet proto test
    do
        cd "${srcdir}/${pkgname}/distribute/python/caffe/${_dir}"
        for _file in *
        do
            _mode="$(stat --format '%a' "$_file")"
            install -D -m"$_mode" "$_file" "${pkgdir}/usr/lib/python3.6/site-packages/caffe/${_dir}"
        done
    done
    
    # proto
    cd "${srcdir}/${pkgname}/distribute/proto"
    install -D -m644 * "${pkgdir}/usr/share/caffe"
    
    # docs
    cd "${srcdir}/${pkgname}/doxygen/html"
    for _file in *
    do
        [ -d "$_file" ] && continue # skip directories
        install -D -m644 "$_file" "${pkgdir}/usr/share/doc/${_srcname}"
    done
    cd search
    install -D -m644 * "${pkgdir}/usr/share/doc/${_srcname}/search"
    
    # license
    cd "${srcdir}/${pkgname}"
    install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}"
}
