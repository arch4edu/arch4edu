# Maintainer:  Drew Noel <drewmnoel@gmail.com>

pkgname=caffe-git
pkgver=rc3.r186.gf28f5ae
pkgrel=1
pkgdesc='A fast framework for deep learning built in C++ for speed with a Python 2 interface'
arch=(x86_64)
url='https://github.com/BVLC/caffe'
license=('custom')

# if using an AWS EC2 make sure to use the community repo for cuda and not the ec2 repo. 
depends=('cuda'
         'opencv'
         'openblas-lapack'
         'google-glog'
         'gflags'
         'lmdb'
         'cython2'
         'ipython2'
         'python2-pillow'
         'python2-numpy'
         'python2-yaml'
         'python2-numpy'
         'python2-scipy'
         'python2-scikit-image'
         'python2-scikit-learn'
         'python2-matplotlib'
         'python2-h5py'
         'python2-leveldb'
         'python2-networkx'
         'python2-nose'
         'python2-pandas'
         'python2-dateutil'
         'python2-protobuf'
         'python2-gflags'
         'python2-pandas'
         'boost'
         'boost-libs'
         'bc'
        )

source=('git+https://github.com/BVLC/caffe.git'
        'classify-print-results.py'
        'Makefile.config')
makedepends=('git' 'python2-setuptools' 'gcc-fortran' 'wget')
provides=('caffe' 'pycaffe' 'python2-pycaffe' )
conflicts=('caffe' 'pycaffe' 'python2-pycaffe' 'pycaffe-git' 'python2-pycaffe-git')
sha256sums=('SKIP'
            'c12ddbd524c1b5871cb42a8775cf17a3ef86ae8a859837a6c6c4e2c19deca3d5'
            '91ac4b31b72c9c6fb8b1242c945d8caf32f1876ef4befa3c81b7d19940b6a143')

pkgver() {
  cd $srcdir/caffe
  set -o pipefail
  git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  # You can modify this file and do some stuff like turn off using the GPU etc
  cp Makefile.config $srcdir/caffe

  # Modified classify.py for testing that will output results
  cp classify-print-results.py $srcdir/caffe/python/

  cd $srcdir/caffe

  # Patch any #!/usr/bin/python to #!/usr/bin/python2
  for file in $(find . -name '*.py' -print); do
    sed -r -i 's_^#!.*/usr/bin/python(\s|$)_#!/usr/bin/python2_' $file
    sed -r -i 's_^#!.*/usr/bin/env(\s)*python(\s|$)_#!/usr/bin/env python2_' $file
  done
 # Do the same for python examples
  for file in $(find . -name '*.py.example' -print); do
    sed -r -i 's_^#!.*/usr/bin/python(\s|$)_#!/usr/bin/python2_' $file
    sed -r -i 's_^#!.*/usr/bin/env(\s)*python(\s|$)_#!/usr/bin/env python2_' $file
  done

  # If the user has colormake installed then use that instead of make.
  if hash colormake 2>/dev/null; then
    colormake all
    colormake pycaffe
  else
    make all
    make pycaffe
  fi

  msg "Downloading the ImageNet Caffe model and labels" 
  python2 scripts/download_model_binary.py models/bvlc_reference_caffenet # 232 MB
  sh data/ilsvrc12/get_ilsvrc_aux.sh # 17 MB

  msg "Downloading the mnist data"
  sh data/mnist/get_mnist.sh #10 MB
}

# check() {
#   cd caffe

#   # Unrem these next two lines to run the 838 tests
#   # make test
#   # make runtest

#   # A simple test to make sure its working (Attempt to classify a picture of a cat)
#   # Expected result: [('tabby', '0.27933'), ('tiger cat', '0.21915'), ('Egyptian cat', '0.16064'), ('lynx', '0.12844'), ('kit fox', '0.05155')]
#   python2 python/classify-print-results.py --print_results examples/images/cat.jpg foo
#   msg "Tested that everything works.. you should see some cat type classifiations above this message"
# }

package() {
  cd $srcdir/caffe

  # Setup Python by hand since no setup.py 
  mkdir -p $pkgdir/usr/lib/python2.7/site-packages/caffe/
  cp -R python/caffe/* $pkgdir/usr/lib/python2.7/site-packages/caffe/

  # Add missing __init__.py file to ensure that the modules are detected.
  find "$pkgdir/usr/lib/python2.7/site-packages/caffe" -type d -exec touch '{}'/__init__.py \;

  # Still leaving a copy of the python code in the main caffe directory since it might be useful for some
  # Though because of that namcap will give this error:
  # caffe-git E: ELF file ('opt/caffe/python/caffe/_caffe.so') outside of a valid path.

  # Install shared libraries
  mkdir -p $pkgdir/usr/lib/
  install -Dm644 build/lib/* "${pkgdir}/usr/lib/"

  ### Install all the execulables ###
  mkdir -p $pkgdir/usr/bin/

  # Primary executable
  install -D -m755 build/tools/caffe.bin "$pkgdir/usr/bin/caffe"

  # Conversion executables 
  install -D -m755 build/examples/cifar10/convert_cifar_data.bin "$pkgdir/usr/bin/convert_cifar_data"
  install -D -m755 build/examples/mnist/convert_mnist_data.bin "$pkgdir/usr/bin/convert_mnist_data"
  install -D -m755 build/examples/siamese/convert_mnist_siamese_data.bin "$pkgdir/usr/bin/convert_mnist_siamese_data"

  # Depreciated executables. All in caffe executable now but included here for backwards compatiblity
  install -D -m755 build/tools/finetune_net.bin "$pkgdir/usr/bin/finetune_net"
  install -D -m755 build/tools/train_net.bin "$pkgdir/usr/bin/train_net"
  install -D -m755 build/tools/device_query.bin "$pkgdir/usr/bin/device_query"
  install -D -m755 build/tools/net_speed_benchmark.bin "$pkgdir/usr/bin/net_speed_benchmark"
  install -D -m755 build/tools/compute_image_mean.bin "$pkgdir/usr/bin/compute_image_mean"
  install -D -m755 build/tools/convert_imageset.bin "$pkgdir/usr/bin/convert_imageset"
  install -D -m755 build/tools/test_net.bin "$pkgdir/usr/bin/test_net"
  install -D -m755 build/tools/upgrade_net_proto_text.bin "$pkgdir/usr/bin/upgrade_net_proto_text"
  # install -D -m755 build/tools/dump_network.bin "$pkgdir/usr/bin/dump_network"
  install -D -m755 build/tools/extract_features.bin "$pkgdir/usr/bin/extract_features"

  # Make main target dir
  mkdir -p $pkgdir/opt/caffe

  # Copy all source files over
  cp .Doxyfile $pkgdir/opt/caffe/
  cp .travis.yml $pkgdir/opt/caffe/
  cp CMakeLists.txt $pkgdir/opt/caffe/
  cp CONTRIBUTING.md $pkgdir/opt/caffe/
  cp CONTRIBUTORS.md $pkgdir/opt/caffe/
  cp INSTALL.md $pkgdir/opt/caffe/
  cp LICENSE $pkgdir/opt/caffe/
  cp Makefile $pkgdir/opt/caffe/
  cp README.md $pkgdir/opt/caffe/
  cp caffe.cloc $pkgdir/opt/caffe/
  cp -r cmake $pkgdir/opt/caffe/
  cp -r data $pkgdir/opt/caffe/
  cp -r distribute $pkgdir/opt/caffe/
  cp -r docker $pkgdir/opt/caffe/
  cp -r docs $pkgdir/opt/caffe/
  cp -r examples $pkgdir/opt/caffe/
  cp -r include $pkgdir/opt/caffe/
  cp -r matlab $pkgdir/opt/caffe/
  cp -r models $pkgdir/opt/caffe/
  cp -r python $pkgdir/opt/caffe/
  cp -r scripts $pkgdir/opt/caffe/
  cp -r src $pkgdir/opt/caffe/
  cp -r tools $pkgdir/opt/caffe/

  # Remove residual git files
  find $pkgdir/opt/caffe/ -name .gitignore -delete

  # Install BSD2 License (not in common licenses so lets make it custom)
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"

  # Install Documentation
  install -D -m644 README.md "${pkgdir}/usr/share/doc/${pkgname}/README.md"
}

# vim:set ts=2 sw=2 et:
