# Maintainer: Nicolas Immelman <archlinux@nicolas.co.za>
# Contributor: Sven-Hendrik Haase <sh@lutzhaase.com>
pkgname=cuda-8.0
pkgver=8.0.61
pkgrel=3
pkgdesc="NVIDIA's GPU programming toolkit. Version 8.0"
arch=('x86_64')
url="http://www.nvidia.com/object/cuda_home.html"
license=('custom:NVIDIA')
depends=('gcc-libs' 'opencl-nvidia' 'gcc5')
replaces=('cuda-toolkit' 'cuda-sdk')
provides=('cuda-toolkit' 'cuda-sdk')
optdepends=('gdb: for cuda-gdb')
options=(!strip staticlibs)
install=cuda.install
source=(https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda_${pkgver}_375.26_linux-run
        cuda.sh
        cuda.conf
        cuda-findgllib_mk.diff)
sha512sums=('d22303719a9feff64f95bf6a966f1caa2bf0cf8c955e475ce08ce54faa5e098d336c2db223ef0185c1f23b9c52b7d2f81a63515485219cfc016d72bda979248b'
            'ce0b8df5d918ec8429da4ab8f9dee463ac04055ee5b0beeb0386b67d765a4c892d314995776a0d695cd06bcfbaf996e4904935ddc898a9d774f6bf965d989dea'
            '66bd93ecab7e1aa07218c3dd1c96e460f63ed4ac47e853ecb313c78a58e5425c8a5772f1c7f73d696bf5f93fc3e556a046a4ed955a53d900976ac525abd1f518'
            '89cbe7ce38039188fa0a0b9554fb938e95aa0ced5bc65479c1bdb6f8e063530a8a7002dbf7c287a8d22aea449014c4502e487fa07ea1efa110db4def02819dfe')

prepare() {
  sh cuda_${pkgver}_375.26_linux-run -extract=${srcdir}
  ./cuda-linux64-rel-*.run --noexec --keep
  ./cuda-samples-linux-*.run --noexec --keep

  # path hacks

  # 1rd sed line: sets right path to install man files
  # 2rd sed line: hack to lie installer, now detect launch script by root
  # 3rd sed line: sets right path in .desktop files and other .desktop stuff (warnings by desktop-file-validate)
  sed -e "s|/usr/share|${srcdir}/../pkg/${pkgname}/usr/share|g" \
      -e 's|can_add_for_all_users;|1;|g' \
      -e 's|=\\"$prefix\\\"|=/opt/cuda|g' -e 's|Terminal=No|Terminal=false|g' -e 's|ParallelComputing|ParallelComputing;|g' \
      -i pkg/install-linux.pl

  # set right path in Samples Makefiles
  sed 's|\$cudaprefix\\|\\/opt\\/cuda\\|g' -i pkg/install-sdk-linux.pl

  # use python2
  find pkg -name '*.py' | xargs sed -i -e 's|env python|env python2|g' -e 's|bin/python|bin/python2|g'

  # Fix up samples tht use findgllib_mk
  for f in pkg/samples/*/*/findgllib.mk; do
    patch $f cuda-findgllib_mk.diff
  done
}

package() {
  cd pkg
  export PERL5LIB=.
  perl install-linux.pl -prefix="${pkgdir}/opt/cuda" -noprompt
  perl install-sdk-linux.pl -cudaprefix="${pkgdir}/opt/cuda" -prefix="${pkgdir}/opt/cuda/samples" -noprompt

  # Hack we need because of glibc 2.26 (https://bugs.archlinux.org/task/55580)
  # without which we couldn't compile anything at all.
  # Super dirty hack. I really hope it doesn't break other stuff!
  # Probably we can remove this for cuda 9.
  sed -i "1 i#define _BITS_FLOATN_H" "${pkgdir}/opt/cuda/include/host_defines.h"

  # Needs Gcc 5.x.x
  ln -s /usr/bin/gcc-5 "${pkgdir}/opt/cuda/bin/gcc"
  ln -s /usr/bin/g++-5 "${pkgdir}/opt/cuda/bin/g++"

  # Install profile and ld.so.config files
  install -Dm755 "${srcdir}/cuda.sh" "${pkgdir}/etc/profile.d/cuda.sh"
  install -Dm644 "${srcdir}/cuda.conf" "${pkgdir}/etc/ld.so.conf.d/cuda.conf"

  mkdir -p "${pkgdir}/usr/share/licenses/${pkgname}"
  ln -s /opt/cuda/doc/pdf/EULA.pdf "${pkgdir}/usr/share/licenses/${pkgname}/EULA.pdf"

  # Remove redundant man and samples
  rm -fr "${pkgdir}/opt/cuda/doc/man"
  rm -fr "${pkgdir}/opt/cuda/cuda-samples"
  rm -fr "${pkgdir}/usr/share/man/man3/deprecated.3"*

  # Remove included copy of java and link to system java
  rm -fr  "${pkgdir}/opt/cuda/jre"
  sed 's|../jre/bin/java|/usr/bin/java|g' \
    -i "${pkgdir}/opt/cuda/libnsight/nsight.ini" \
    -i "${pkgdir}/opt/cuda/libnvvp/nvvp.ini"

  # Remove unused files
  rm -fr "${pkgdir}/opt/cuda/"{bin,samples}"/.uninstall_manifest_do_not_delete.txt"
  rm -fr "${pkgdir}/opt/cuda/samples/uninstall_cuda_samples_8.0.pl"
  rm -fr "${pkgdir}/opt/cuda/bin/cuda-install-samples-8.0.sh"
  rm -fr "${pkgdir}/opt/cuda/bin/uninstall_cuda_toolkit_8.0.pl"
}
