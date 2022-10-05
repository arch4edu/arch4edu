# Maintainer: Paul Stemmet <aur@luxolus.com>
# Contributor: Thore Bödecker <foxxx0@archlinux.org>
# Contributor: Sébastien "Seblu" Luttringer <seblu@archlinux.org>

pkgbase='ceph'
pkgname=('ceph' 'ceph-libs' 'ceph-mgr')
_zstdver=1.5.2
pkgver=16.2.7
pkgrel=1
pkgdesc='Distributed, fault-tolerant storage platform delivering object, block, and file system'
arch=('x86_64')
url='https://ceph.com/'
license=('GPL')
makedepends=("zstd=${_zstdver}" 'bash' 'bc' 'boost' 'boost-libs' 'bzip2' 'c-ares' 'cmake' 'coreutils' 'coffeescript'
             'cpio' 'crypto++' 'cryptsetup' 'cunit' 'curl' 'cython' 'expat'
             'fcgi' 'fontconfig' 'fuse2' 'fuse3' 'fmt' 'gcc' 'gcc-libs' 'git' 'glibc' 'gmock' 'gnutls'
             'gperf' 'gperftools' 'gptfdisk' 'gtest' 'hwloc' 'inetutils' 'java-runtime'
             'jq' 'jre11-openjdk-headless' 'junit' 'keyutils' 'leveldb' 'libaio'
             'libatomic_ops' 'libcap' 'libcap-ng' 'libcroco' 'libcurl-compat'
             'libedit' 'libgudev' 'libnl' 'librabbitmq-c' 'libtool' 'util-linux'
             'libuv' 'libxml2' 'librdkafka' 'libpciaccess' 'lsb-release' 'lua' 'lz4' 'ncurses'
             'nss' 'numactl' 'oath-toolkit' 'openssl' 'parted' 'pcre' 'pcre2' 'pkgconf' 'protobuf'
             'procps-ng' 'python-astroid' 'python-attrs' 'python-bcrypt'
             'python-cheroot' 'python-cherrypy' 'python-coverage' 'python-dateutil'
             'python-elasticsearch' 'python-flask' 'python-flask-restful'
             'python-google-api-python-client' 'python-google-auth'
             'python-google-auth-httplib2' 'python-grpcio' 'python-isort'
             'python-jinja' 'python-lazy-object-proxy' 'python-mccabe'
             'python-isodate' 'python-defusedxml' 'python-pkgconfig' 'python-protobuf'
             'python-lxml' 'python-xmlsec' 'python-yaml'
             'python-more-itertools' 'python-numpy' 'python-pbr' 'python-pecan'
             'python-pip' 'python-pluggy' 'python-portend' 'python-prettytable'
             'python-prometheus_client' 'python-py' 'python-pycparser'
             'python-pyjwt' 'python-pyopenssl' 'python-pytz' 'python-requests'
             'python-routes' 'python-scikit-learn' 'python-scipy'
             'python-setuptools' 'python-six' 'python-sphinx' 'python-tempora'
             'python-virtualenv' 'python-werkzeug' 'python-wrapt' 'rabbitmq'
             'sed' 'snappy' 'socat' 'systemd' 'systemd-libs' 'valgrind'
             'xfsprogs' 'xmlstarlet' 'xmlsec' 'xxhash' 'yaml-cpp' 'yasm' 'zlib' )
checkdepends=('python-mock' 'python-nose' 'python-pycodestyle' 'python-pylint'
              'python-pytest' 'python-pytest-cov')
# need newer version for LTO (https://github.com/ceph/ceph/pull/42602)
options=('emptydirs' '!lto')
source=(
  "https://download.ceph.com/tarballs/${pkgbase}-${pkgver}.tar.gz"
  'ceph.sysusers'
  "zstd-${_zstdver}.tar.gz::https://github.com/facebook/zstd/archive/v${_zstdver}.tar.gz"
  #'glibc2.32-strsignal-compat-backported.patch'
  'ceph-14.2.0-cflags.patch'
  'ceph-12.2.4-boost-build-none-options.patch'
  'ceph-13.2.0-cflags.patch'
  'ceph-13.2.2-dont-install-sysvinit-script.patch'
  # 'ceph-14.2.0-link-crc32-statically.patch'
  'ceph-14.2.0-cython-0.29.patch'
  'ceph-15.2.0-rocksdb-cmake.patch'
  # 'ceph-15.2.4-system-uring.patch'
  # 'ceph-15.2.5-missing-includes.patch'
  'ceph-15.2.14-gcc12.patch'
  'disable-empty-readable.sh-test.patch'
  # 'qa-src-update-mypy-to-0.782.patch'
  # 'fix-mgr-dashboard-partial_dict.patch'

  # snappy 1.1.9 removed major parts from their namespace, including the
  # snappy::uint32 which was an alias for std::uint32_t
  # 'fix_snappy_namespace_uint.patch'

  # Add python >= 3.8 workaround logic for incompatible modules
  # This has been designated for upstream backporting into the octupus (15) and pacific (16) branches.
  # TODO: check if merged and included in next releases
  # https://tracker.ceph.com/issues/45147
  # https://github.com/ceph/ceph/pull/34846
  # 'backport_mgr_disabled_modules_workaround_PR34846.patch'

  # Fix breaking change to PY_SSIZE_T_CLEAN macro defintion requirements in python >= 3.10
  # by defining the macro ahead of any calls.
  # https://tracker.ceph.com/issues/53441
  # https://github.com/ceph/ceph/pull/44112
  'fix-python310-ssize-macro.patch'

  # RGW string header is missing includes that are required when boost is >=1.75
  # https://tracker.ceph.com/issues/50924
  'ceph-16.2.4-rgw-string-missing-includes.patch'

  # Updates more-itertools.py to a version that doesn't depend on removed classes in
  # python >= 3.10
  'fix-python310-update-mgr-more-itertools.patch'

  # Fixes an encoding test's expected output to include the new stuff from c++ 17
  # ... or at least, I think that's what is causing it
  'fix-test-encoding-exception-wording.patch'

  # Add a missing dep to a tox virtualenv (python-nose)
  'fix-test-import-tasks-deps.patch'

  # Remove a test that requires docker, and only tests Prometheus metrics anyway
  # Note this test has been completely removed in 17.2.0, and can be dropped when
  # we update to 17
  'ceph-16.2.7-remove-promtool-test.patch'

  # Test breaks due to ambigous template in src/common/async/bind_like.h when called
  # in src/test/cls/fifo/bench_* and test_*. Not sure how to fix this so disabled for now
  'disable-test-cls-fifo.patch'

  # Test improperly creates librados::async_write templates, in boost 1.80
  # not sure why yet, need to ask upstream for help
  'ceph-16.2.7-delete-test-librados-asio.patch'
)
sha512sums=('eab047e646970d444acf1064d98237b8b1677fb16b5e771082d55880f7bc6d8bdb278c2fe514c82ae12c438878d9ecea29139fa6b8d890f9f737138f10fb740c'
            '4354001c1abd9a0c385ba7bd529e3638fb6660b6a88d4e49706d4ac21c81b8e829303a20fb5445730bdac18c4865efb10bc809c1cd56d743c12aa9a52e160049'
            'e107508a41fca50845cc2494e64adaba93efb95a2fa486fc962510a8ba4b2180d93067cae9870f119e88e5e8b28a046bc2240b0b23cdd8933d1fb1a6a9668c1e'
            '9e6bb46d5bbdc5d93f4f026b2a8d6bdb692d9ea6e7018c1bb0188d95ea8574c76238d968b340fd67ddaa3d8183b310e393e3549dc3a63a795fde696413b0ca94'
            '6ff46a90d76f667fa23be0f9eb1ed2fb7e30af9a2621aec19944d0a22a431a0f5721603c588286e483ff55c14aac920adfccb039c9678a87cc59640dd70367ae'
            '8ec0d668fefee12d2c7f5b5297dd81fc6a559f5823d069e6395d9b4240110eb8f95049d3054697a459948c1f3784b4450539849cf9d7f3b1aa1c7fbd96c475df'
            'ea069b75b786c22166c609b127b512802cc5c6e9512d792d7b7b34d276f5b86d57c8c35cfc7b5c855a59c0ba87ba1aabe2ca26da72b26bff46b6ba8410ddb27e'
            '82c1608928ee669ef60b8930ce82c443152c446e669e7bde9ce32f78571afb19a9620c3818b69ac8cb3ea33e7d7ac40f77c89162c71b19b157336d907fa23e3d'
            '2e62020cce33e3152cdb9a128023ee673124c4bcfdb9ee17718891ba5c9a16d98eb03ed06fe7dc7833c98487c1c1eb67fadfad1aa2f40c2c648829c86b4caab0'
            '69b058e7b215f85f347b1e4528800ed62635864fa32b24b0f9db97b08fe6576f30d260bf6a19bb5166482f43928feb535e9a6dca8f3c2b3ce7700c108db9fb7a'
            '2234d005df71b3b6013e6b76ad07a5791e3af7efec5f41c78eb1a9c92a22a67f0be9560be59b52534e90bfe251bcf32c33d5d40163f3f8f7e7420691f0f4a222'
            'cc9f198692ab67ffdf2071c755ab7369fcaa4e1211d1428bb49db3bca5956ae4fbe98ead80a8f691d61e80402b4a06ce9b046a97cb4a3376334f64a4fd16bfb5'
            '1c43b1d466b39b6ad46dd5eb9e5dea4708142ba911b6e901daff427de7889c2018e69e39d5c6b40dc6f979e8533114716ad57b25f7dc3d57e012b5c47a5efb16'
            '6be59a31f0cad390bf9f40041c05049e7d525c6910eab200a5b2a707d59cb80f5119651a86a865680a074a021ff3be8cc3769eb5bf1978691dc2cd91d96e500c'
            '380ae6d3a768dacaaf2bbe634aa4b1d296da3318553256e4bbae747eb477549968a6c4333b9d212d4ea2db74ae554ac3c4edd7408f46f5f86971d84284748686'
            '7297ec3824815f6f5e534f225ae10f0b0c046713c062adf2cb7af12e44db6f699948a87851fc24b7c038bfa95646a9b66c6256c6bad9253f469b75cd4ed81c7d'
            '49c78ccbd514b22c7de7a72417524d42a8d838275e89d8cf9cf3f7caf54e11e81e86b7ef9a6966a96f30348c45ab7615ac591d66ce2cbe880b77d9015e7fdb8a'
            '3774cbc1a979ee8bf7138b96defcf69499444afe0b7186b21feac3453a3a5ec93741f5942d256d93999e9bc306c8d018206893e04e1a3eb9e03593105d9f5791'
            '66770a80ba4e05ea72d4809cb5819cce7499ea7523b85b1a57370df68de1d7f6f94b1c10d0f9f9a3c8e6a86d0419434c70778c568cd06a0dd2e6126631a3355c')

# -fno-plt causes linker errors (undefined reference to internal methods)
# similar issue: https://bugs.archlinux.org/task/54845
# https://github.com/intel/media-driver/commit/d95d8f7ab7ac94a2e0f4ee6a4b4794898dc2d3b7
# as of today (2019-07-12) the upstream maintainers do not consider this a bug in their code
# (IMHO rightfully so) and thus we strip the option here
export CFLAGS="${CFLAGS/-fno-plt/}"
export CXXFLAGS="${CXXFLAGS/-fno-plt/}"


prepare() {
  cd "${srcdir}/${pkgbase}-${pkgver}"

  # apply patches from the source array
  local filename
  for filename in "${source[@]%%::*}"; do
    if [[ "${filename}" =~ \.patch$ ]]; then
      echo "Applying patch ${filename##*/}"
      patch -p1 -N -i "${srcdir}/${filename##*/}"
    fi
  done

  # temporarily disable unsubscriptable-object (buggy on Python 3.9)
  # https://github.com/PyCQA/pylint/issues/3882
  sed -i '/^disable=/a\        unsubscriptable-object,' \
    src/pybind/mgr/dashboard/.pylintrc

  # mypy complains about this but the exception is handled; not sure what's up
  sed -i 's/from base64 import encodestring$/&  # type: ignore/' \
    src/pybind/mgr/dashboard/awsauth.py

  # suppress deprecation warnings
  sed -i '/#ifndef CEPH_CONFIG_H/i#define BOOST_ALLOW_DEPRECATED_HEADERS' \
    src/common/config.h
  sed -i '/#ifndef CEPH_TYPES_H/i#define BOOST_ALLOW_DEPRECATED_HEADERS' \
    src/include/types.h

  # fix boost stuff for system-boost
  find . -name '*.cmake' -or -name 'CMakeLists.txt' -print0 | xargs --null \
    sed -r \
    -e 's|Boost::|boost_|g' \
    -e 's|Boost_|boost_|g' \
    -e 's|[Bb]oost_boost|boost_system|g' -i || exit 1

  # remove bundled zstd and replace with newer release
  rm -rf src/zstd
  ln -sf "${srcdir}/zstd-${_zstdver}" src/zstd

  # remove tests that require root privileges
  rm src/test/cli/ceph-authtool/cap*.t

  # disable/remove broken tests
  sed -i '/add_ceph_test(smoke.sh/d' src/test/CMakeLists.txt
  sed -i '/add_ceph_test(safe-to-destroy.sh/d' src/test/osd/CMakeLists.txt
}

build() {
  cd "${srcdir}/${pkgbase}-${pkgver}"

  # workaround for boost 1.74 -- similar fix exists upstream but I could
  # not get it to work: https://github.com/ceph/ceph/commit/3d708219092d
  CPPFLAGS+=' -DBOOST_ASIO_USE_TS_EXECUTOR_AS_DEFAULT'
  # 2022-09-27 fmt>9 has deprecated an API that is used extensively throughout
  # the code base. See:
  # Upstream: https://tracker.ceph.com/issues/56610
  # Debian: https://salsa.debian.org/ceph-team/ceph/-/merge_requests/9
  CPPFLAGS+=' -DFMT_DEPRECATED_OSTREAM'

  export CFLAGS+=" ${CPPFLAGS}"
  export CXXFLAGS+=" ${CPPFLAGS}"
  export PYTHON_VERSION="$(python --version | awk '{print $2}')"
  export PYTHON_INCLUDE_DIR="$(python -c "from sysconfig import get_path; print(get_path('include'))")"
  export CMAKE_BUILD_TYPE='RelWithDebInfo'
  export CMAKE_WARN_UNUSED_CLI=no

  cmake \
    -B build \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_SYSCONFDIR=/etc \
    -DCMAKE_INSTALL_SBINDIR=/usr/bin \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DCEPH_SYSTEMD_ENV_DIR=/etc/default \
    -DCMAKE_INSTALL_LIBEXECDIR=/usr/lib \
    -DCMAKE_INSTALL_SYSTEMD_SERVICEDIR=/usr/lib/systemd/system \
    -DCMAKE_VERBOSE_MAKEFILE=ON \
    -DENABLE_GIT_VERSION=ON \
    -DWITH_PYTHON2=OFF \
    -DWITH_PYTHON3="${PYTHON_VERSION}" \
    -DMGR_PYTHON_VERSION=3 \
    -DPYTHON_INCLUDE_DIR="${PYTHON_INCLUDE_DIR:?}" \
    -DWITH_BABELTRACE=OFF \
    -DWITH_LTTNG=OFF \
    -DWITH_OPENLDAP=OFF \
    -DWITH_RDMA=OFF \
    -DWITH_OCF=OFF \
    -DWITH_DPDK=OFF \
    -DWITH_SPDK=OFF \
    -DWITH_CEPHFS=ON \
    -DWITH_CEPHFS_JAVA=ON \
    -DWITH_CEPHFS_SHELL=ON \
    -DWITH_FUSE=ON \
    -DWITH_LZ4=ON \
    -DWITH_XFS=ON \
    -DWITH_MGR=ON \
    -DWITH_MGR_DASHBOARD_FRONTEND=ON \
    -DDASHBOARD_FRONTEND_LANGS="en-US" \
    -DWITH_RADOSGW=ON \
    -DWITH_RADOSGW_FCGI_FRONTEND=OFF \
    -DWITH_RADOSGW_BEAST_FRONTEND=ON \
    -DWITH_RADOSGW_BEAST_OPENSSL=ON \
    -DWITH_RADOSGW_AMQP_ENDPOINT=OFF \
    -DWITH_SYSTEMD=ON \
    -DWITH_SYSTEM_BOOST=ON \
    -DWITH_BOOST_CONTEXT=ON \
    -DWITH_SYSTEM_GTEST=OFF \
    -DWITH_SYSTEM_NPM=OFF \
    -DENABLE_SHARED=ON \
    -DWITH_TESTS=ON \
    -Wno-dev

  VERBOSE=1 make -C build all
}

check() {
  cd "${srcdir}/${pkgbase}-${pkgver}"

  export CTEST_PARALLEL_LEVEL=7
  export CTEST_OUTPUT_ON_FAILURE=1
  VERBOSE=1 make -C build check || true

  # sometimes processes are not properly terminated...
  for process in ceph-mon ceph-mgr ceph-osd; do
    pkill -9 "${process}" || true
  done
}

package_ceph-libs() {
  depends=('boost-libs' 'curl' 'glibc' 'keyutils' 'libutil-linux' 'bzip2' 'lz4' 'nss'
           'oath-toolkit' 'python' 'snappy' 'systemd-libs' 'fmt' 'cryptsetup'
           'lua' 'librdkafka'
           'python-prettytable' 'python-yaml' 'python-setuptools')
  provides=("ceph-libs=${pkgver}-${pkgrel}")
  conflicts=('ceph-libs-bin')

  cd "${srcdir}/${pkgbase}-${pkgver}"

  # main install
  VERBOSE=1 make DESTDIR="${pkgdir}" -C build install

  # remove stuff that goes into the ceph package
  rm -rf "${pkgdir}"/usr/lib/{ceph/mgr,systemd,sysusers.d,tmpfiles.d}
  rm -rf "${pkgdir}/usr/share"
  rm -rf "${pkgdir}/usr/sbin"
  rm -rf "${pkgdir}/usr/bin"
  rm -rf "${pkgdir}/etc"
  rm -rf "${pkgdir}/var"

  # Remove misc. test files
  find "${pkgdir}" -depth -type d -name 'tests' -exec rm -vr '{}' \+
}

package_ceph() {
  depends=("ceph-libs=${pkgver}-${pkgrel}"
           'boost-libs' 'curl' 'fuse2' 'fuse3' 'fmt' 'glibc' 'gperftools' 'java-runtime'
           'keyutils' 'leveldb' 'libaio' 'libutil-linux' 'librdkafka' 'cryptsetup' 'libnl'
           'ncurses'
           'nss' 'oath-toolkit' 'python'
           'snappy' 'sudo' 'systemd-libs' 'lua' 'gawk'
           'xfsprogs')
  provides=("ceph=${pkgver}-${pkgrel}")
  conflicts=('ceph-bin')

  cd "${srcdir}/${pkgbase}-${pkgver}"

  # main install
  VERBOSE=1 make DESTDIR="${pkgdir}" -C build install

  # fix sbin dir (cmake opt seems to have no effect)
  mv "${pkgdir}"/usr/sbin/* "${pkgdir}/usr/bin/"
  rm -rf "${pkgdir}/usr/sbin"

  # remove stuff that is in the ceph-libs package
  find "${pkgdir}/usr/lib" -maxdepth 1 -type f -delete
  find "${pkgdir}/usr/lib" -maxdepth 1 -type l -delete
  find "${pkgdir}/usr/lib/ceph" -maxdepth 1 -type f -delete
  find "${pkgdir}/usr/lib/ceph" -maxdepth 1 -type l -delete
  rm -rf "${pkgdir}"/usr/lib/{ceph/{compressor,crypto,erasure-code,librbd},rados-classes}
  rm -rf "${pkgdir}"/usr/lib/python*
  rm -rf "${pkgdir}/usr/include"

  # remove stuff that is in the ceph-mgr package
  rm -rf "${pkgdir}"/usr/{bin/ceph-mgr,share/ceph/mgr,lib/systemd/system/ceph-mgr*}

  # remove _test_ binaries from the package, not needed
  find "${pkgdir}/usr/bin" -maxdepth 1 -type f -iname 'ceph_test_*' -delete

  # install tmpfiles.d and sysusers.d stuff
  install -Dm644 "${srcdir}/${pkgbase}-${pkgver}/systemd/ceph.tmpfiles.d" \
    "${pkgdir}/usr/lib/tmpfiles.d/${pkgbase}.conf"
  install -Dm644 "${srcdir}/ceph.sysusers" \
    "${pkgdir}/usr/lib/sysusers.d/${pkgbase}.conf"

  # remove debian init script
  rm -rf "${pkgdir}/etc/init.d"

  # remove drop.ceph.com ssh stuff
  rm -f "${pkgdir}"/usr/share/ceph/id_rsa_drop.ceph.com
  rm -f "${pkgdir}"/usr/share/ceph/id_rsa_drop.ceph.com.pub
  rm -f "${pkgdir}"/usr/share/ceph/known_hosts_drop.ceph.com

  # fix bash completions path
  install -d -m 755 "${pkgdir}/usr/share/bash-completion"
  mv "${pkgdir}"/{etc/bash_completion.d,usr/share/bash-completion/completions}

  # fix EnvironmentFile location in systemd service files
  sed -i 's|/etc/sysconfig/|/etc/conf.d/|g' "${pkgdir}"/usr/lib/systemd/system/*.service

  # prepare some paths and set correct permissions
  install -D -d -m755 -o   0 -g 340 "${pkgdir}/etc/ceph"
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/log/ceph"
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph"
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph/bootstrap-mds"
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph/bootstrap-osd"
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph/bootstrap-rgw"
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph/mon"
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph/osd"
}

package_ceph-mgr() {
  depends=("ceph=${pkgver}-${pkgrel}" "ceph-libs=${pkgver}-${pkgrel}"
           'bash' 'boost-libs' 'coffeescript' 'curl' 'gperftools' 'nodejs' 'nss' 'fmt'
           'python' 'python-cherrypy' 'python-pecan' 'python-pyjwt' 'python-more-itertools'
           'python-numpy' 'python-scipy' 'python-six' 'python-coverage' 'python-pytest' 'python-dateutil'
           'python-prettytable' 'python-requests' 'python-pyopenssl' 'python-bcrypt' 'python-yaml'
           'python-werkzeug' 'python-jinja')
  optdepends=('python-influxdb: influx module'
              'python-kubernetes: rook module'
              'python-prometheus_client: prometheus module'
              'python-remoto: ssh module')
  provides=("ceph-mgr=${pkgver}-${pkgrel}")
  conflicts=('ceph<15.2.1-1' 'ceph-mgr-bin')

  cd "${srcdir}/${pkgbase}-${pkgver}"

  # main install
  VERBOSE=1 make DESTDIR="${pkgdir}" -C build install

  # fix sbin dir (cmake opt seems to have no effect)
  mv "${pkgdir}"/usr/sbin/* "${pkgdir}/usr/bin/"
  rm -rf "${pkgdir}/usr/sbin"

  # remove everything except mgr related stuff, rest is in ceph/ceph-libs
  rm -rf "${pkgdir}"/usr/lib/{ceph/{compressor,crypto,erasure-code},rados-classes}
  rm -rf "${pkgdir}/usr/include"
  find "${pkgdir}/usr/bin" -maxdepth 1 -type f -not -name 'ceph-mgr' -delete
  find "${pkgdir}"/usr/lib/systemd/system -maxdepth 1 -type f -not -iname 'ceph-mgr*' -delete
  find "${pkgdir}"/usr/lib -maxdepth 1 -type f -delete
  find "${pkgdir}"/usr/lib -maxdepth 1 -type l -delete
  rm -rf "${pkgdir}"/etc
  rm -rf "${pkgdir}"/var
  rm -rf "${pkgdir}"/usr/lib/{ceph,sysusers.d,tmpfiles.d}
  rm -rf "${pkgdir}"/usr/lib/python*
  rm -rf "${pkgdir}"/usr/share/{bash-completion,doc,java,man}

  # remove debian init script
  rm -rf "${pkgdir}/etc/init.d"

  # remove drop.ceph.com ssh stuff
  rm -f "${pkgdir}"/usr/share/ceph/id_rsa_drop.ceph.com
  rm -f "${pkgdir}"/usr/share/ceph/id_rsa_drop.ceph.com.pub
  rm -f "${pkgdir}"/usr/share/ceph/known_hosts_drop.ceph.com

  # fix EnvironmentFile location in systemd service files
  sed -i 's|/etc/sysconfig/|/etc/conf.d/|g' "${pkgdir}"/usr/lib/systemd/system/*.service

  # prepare some paths and set correct permissions
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph/mgr"
}

# vim:set ts=2 sw=2 et:
