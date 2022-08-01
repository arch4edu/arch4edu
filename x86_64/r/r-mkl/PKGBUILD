# Maintainer: alexanderp <alexisph -at- gmail -dot- com>
# Previous maintainers:
# - halfhorn <mwellsa -at- gmail -dot- com>
# - jdarch <jda -dot- cloud -plus- archlinux -at- gmail -dot- com>

pkgname=r-mkl
pkgver=4.2.1
pkgrel=1
pkgdesc="Language and environment for statistical computing and graphics, linked to the Intel(R) MKL."
arch=('x86_64')
license=('GPL')
url='http://www.r-project.org/'
provides=("r=${pkgver}")
conflicts=('r' 'microsoft-r-open')
depends=('intel-mkl'
         'bzip2'
         'curl'
         'icu'
         'libjpeg'
         'libpng'
         'libtiff'
         'libxmu'
         'libxt'
         'ncurses'
         'openmp'
         'pango'
         'pcre2'
         'perl'
         'readline'
         'unzip'
         'xz'
         'zip'
         'zlib')
makedepends=('java-environment'
             'gcc-fortran'
             'tk')
optdepends=('texlive-bin: LaTeX sty files'
            'gcc-fortran: needed to compile some CRAN packages'
            'tk: tcl-tk interface')
backup=('etc/R/Makeconf'
        'etc/R/Renviron'
        'etc/R/ldpaths'
        'etc/R/repositories'
        'etc/R/javaconf')
options=('!emptydirs')
install=r-mkl.install

source=("http://cran.r-project.org/src/base/R-${pkgver%%.*}/R-${pkgver}.tar.gz"
        'r.desktop'
        'r.png'
        'R.conf'
        'mklvars.sh')

sha1sums=('476347a910a01f0cc311faf5e7261aa2251b7d21'
          'dd214eee232b7aced7366722ad416b6b39be8e1b'
          'af80774f5a8d0e669e8ff90662638a0f4e1105d7'
          '43668da6cfd1b4455a99f23e79e2059294dddac9'
          '2cc0e30ca5de872ea7f5af417b8cac988f3e9f8e')

# Build with the Intel Compiler Suite or GCC/GFortran.
# Comment the following line to build the package with GCC
# _CC="icc"

# update dependencies w.r.t the compiler used
if [[ $_CC = "icc" ]]; then
  depends+=('intel-compiler-base'
            'intel-fortran-compiler'
            'intel-openmp')
fi


prepare() {
  cd R-${pkgver}
  # set texmf dir correctly in makefile
  sed -i 's|$(rsharedir)/texmf|${datarootdir}/texmf|' share/Makefile.in
  # align mklvars.sh with Arch Linux intel-mkl
  cd ..
  sed -i 's|CPRO_PATH=/opt/intel/compilers.*$|CPRO_PATH=/opt/intel|g' mklvars.sh
}


build() {
  cd R-${pkgver}

  # https://software.intel.com/sites/products/mkl/mkl_link_line_advisor.htm
  # Interface Layer: LP64 (R uses 32-bit integers)

  _intel_arch=intel64
  _intel_lib=mkl_intel_lp64
  _gfortran_lib=mkl_gf_lp64

  # Set up the environment for MKL
  if [ -z ${MKLROOT+x} ]; then
    echo -e "\nError: MKLROOT is unset\n"
    exit
  fi
  if [ -f /opt/intel/mkl/bin/mklvars.sh ]; then
    echo "Sourcing /opt/intel/mkl/bin/mklvars.sh"
    source /opt/intel/mkl/bin/mklvars.sh ${_intel_arch}
  elif [ -f /usr/bin/mklvars.sh ]; then
    echo "Sourcing /usr/bin/mklvars.sh"
    source /usr/bin/mklvars.sh ${_intel_arch}
  else
    echo "Sourcing mklvars.sh"
    source ../mklvars.sh ${_intel_arch}
  fi

  if [[ $_CC = "icc" ]]; then
    source ${MKLROOT}/../bin/compilervars.sh ${_intel_arch}
    _intel_cc_opt=" -O3 -fPIC -m64 -march=native -fp-model precise -fp-model source -I${MKLROOT}/include"
    # export LDFLAGS=" -qopenmp"
    export FLIBS=" -lgfortran -lifcore -lifport"

    # Dynamic Linking
    _mkllibs=" -L${MKLROOT}/lib/${_intel_arch} \
      -l${_intel_lib} \
      -lmkl_intel_thread \
      -lmkl_core \
      -liomp5 \
      -lpthread \
      -lm \
      -ldl"

    export CC="icc"
    export CXX="icpc"
    export AR="xiar"
    export LD="xild"
    export F77="ifort"
    export FC="ifort"
    export CFLAGS="${_intel_cc_opt}"
    export CXXFLAGS="${_intel_cc_opt}"
    export FFLAGS="${_intel_cc_opt}"
    export FCFLAGS="${_intel_cc_opt}"
  else
    _gcc_opt=" -m64 -I${MKLROOT}/include"
    # export LDFLAGS=" -fopenmp"

    # Dynamic Linking
    _mkllibs=" -L${MKLROOT}/lib/${_intel_arch} \
      -Wl,--no-as-needed \
      -l${_gfortran_lib} \
      -lmkl_gnu_thread \
      -lmkl_core \
      -lgomp \
      -lpthread \
      -lm \
      -ldl"

    export CC="gcc"
    export CXX="g++"
    export AR="ar"
    export LD="ld"
    export F77="gfortran"
    export FC="gfortran"
    export CFLAGS="${_gcc_opt} $CFLAGS"
    export CXXFLAGS="${_gcc_opt} $CXXFLAGS"
    export FFLAGS="${_gcc_opt} $FFLAGS"
    export FCFLAGS="${_gcc_opt} $FCFLAGS"
  fi

  ./configure  --prefix=/usr \
    --libdir=/usr/lib \
    --sysconfdir=/etc/R \
    --datarootdir=/usr/share \
    rsharedir=/usr/share/R/ \
    rincludedir=/usr/include/R/ \
    rdocdir=/usr/share/doc/R/ \
    --with-x \
    --with-blas="${_mkllibs}" \
    --with-lapack \
    --enable-R-shlib \
    LIBnn=lib

  # Place Intel's basic math library prior to GLIBC libm
  # sed -i "s/\(^\| \)-lm\( \|$\)/\1-limf -lm\2/g" {./,etc/}Makeconf

  # Build the package
  make

  # make libRmath.so
  cd src/nmath/standalone
  make shared
}


check() {
  cd R-${pkgver}
  make check-recommended
}


package() {
  cd R-${pkgver}
  make DESTDIR="${pkgdir}" install

  # install libRmath.so
  cd src/nmath/standalone
  make DESTDIR="${pkgdir}" install

  # Fix R wrapper scripts.
  sed -i "s|${pkgdir} ||" "${pkgdir}/usr/bin/R"
  rm "${pkgdir}/usr/lib/R/bin/R"
  cd "${pkgdir}/usr/lib/R/bin"
  ln -s ../../../bin/R

  # install some freedesktop.org compatibility
  install -Dm644 "${srcdir}/r.desktop" \
    "${pkgdir}/usr/share/applications/r.desktop"
  install -Dm644 "${srcdir}/r.png" \
    "${pkgdir}/usr/share/pixmaps/r.png"

  # move the config directory to /etc and create symlinks
  install -d "${pkgdir}/etc/R"
  cd "${pkgdir}/usr/lib/R/etc"
  for i in *; do
    mv -f ${i} "${pkgdir}/etc/R"
    ln -s /etc/R/${i} ${i}
  done

  # Install ld.so.conf.d file to ensure other applications access the shared lib
  install -Dm644 "${srcdir}/R.conf" "${pkgdir}/etc/ld.so.conf.d/R.conf"
}

