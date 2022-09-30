# Maintainer: Thore Bödecker <foxxx0@archlinux.org>
# Contributor: Sébastien "Seblu" Luttringer <seblu@archlinux.org>

_pkgbase='ceph'
pkgbase='ceph-pacific'
pkgname=('ceph-pacific' 'ceph-pacific-libs' 'ceph-pacific-mgr')
_zstdver=1.5.2
pkgver=16.2.10
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
  "https://download.ceph.com/tarballs/${_pkgbase}-${pkgver}.tar.gz"
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

  # https://tracker.ceph.com/issues/50952
  'https://patch-diff.githubusercontent.com/raw/ceph/ceph/pull/47304.patch'

  # Add python >= 3.8 workaround logic for incompatible modules
  # This has been designated for upstream backporting into the octupus (15) and pacific (16) branches.
  # TODO: check if merged and included in next releases
  # https://tracker.ceph.com/issues/45147
  # https://github.com/ceph/ceph/pull/34846
  # 'backport_mgr_disabled_modules_workaround_PR34846.patch'
)
sha512sums=('ae164c24462c3e08763d202acc3e2fe86ffc09f312b5059bae07863e804fc47bd158fc130aa2923246ffcfe26ae6d6d9317326aec96373226e6f9030d7123c8b'
            '4354001c1abd9a0c385ba7bd529e3638fb6660b6a88d4e49706d4ac21c81b8e829303a20fb5445730bdac18c4865efb10bc809c1cd56d743c12aa9a52e160049'
            'e107508a41fca50845cc2494e64adaba93efb95a2fa486fc962510a8ba4b2180d93067cae9870f119e88e5e8b28a046bc2240b0b23cdd8933d1fb1a6a9668c1e'
            '9e6bb46d5bbdc5d93f4f026b2a8d6bdb692d9ea6e7018c1bb0188d95ea8574c76238d968b340fd67ddaa3d8183b310e393e3549dc3a63a795fde696413b0ca94'
            '6ff46a90d76f667fa23be0f9eb1ed2fb7e30af9a2621aec19944d0a22a431a0f5721603c588286e483ff55c14aac920adfccb039c9678a87cc59640dd70367ae'
            '8ec0d668fefee12d2c7f5b5297dd81fc6a559f5823d069e6395d9b4240110eb8f95049d3054697a459948c1f3784b4450539849cf9d7f3b1aa1c7fbd96c475df'
            'ea069b75b786c22166c609b127b512802cc5c6e9512d792d7b7b34d276f5b86d57c8c35cfc7b5c855a59c0ba87ba1aabe2ca26da72b26bff46b6ba8410ddb27e'
            '82c1608928ee669ef60b8930ce82c443152c446e669e7bde9ce32f78571afb19a9620c3818b69ac8cb3ea33e7d7ac40f77c89162c71b19b157336d907fa23e3d'
            '2e62020cce33e3152cdb9a128023ee673124c4bcfdb9ee17718891ba5c9a16d98eb03ed06fe7dc7833c98487c1c1eb67fadfad1aa2f40c2c648829c86b4caab0'
            'f1b54767d8d3c12ca9fe9eafd0590efa8560a52b5c18f1121f8fd8b7e69d70578bdeae9a1803612a8a8d0032f039f8786b5152a889ba359850e3d3d30a6af8c7'
            '2234d005df71b3b6013e6b76ad07a5791e3af7efec5f41c78eb1a9c92a22a67f0be9560be59b52534e90bfe251bcf32c33d5d40163f3f8f7e7420691f0f4a222'
            '686a80cc00efae855988a087bace7ff94b33b069c87e2455a57126085e21e104e53e97835cda3493ceebfd0dc6ead1b5e6a08dd3c29884d1cb70ca4451577ef0')


# -fno-plt causes linker errors (undefined reference to internal methods)
# similar issue: https://bugs.archlinux.org/task/54845
# https://github.com/intel/media-driver/commit/d95d8f7ab7ac94a2e0f4ee6a4b4794898dc2d3b7
# as of today (2019-07-12) the upstream maintainers do not consider this a bug in their code
# (IMHO rightfully so) and thus we strip the option here
export CFLAGS="${CFLAGS/-fno-plt/}"
export CXXFLAGS="${CXXFLAGS/-fno-plt/}"


prepare() {
  cd "${srcdir}/${_pkgbase}-${pkgver}"

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
  cd "${srcdir}/${_pkgbase}-${pkgver}"

  # https://tracker.ceph.com/issues/56610
  # https://salsa.debian.org/ceph-team/ceph/-/merge_requests/9
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
    -DDASHBOARD_FRONTEND_LANGS="ALL" \
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
    -DWITH_TESTS=OFF \
    -Wno-dev

  VERBOSE=1 make -C build all
}

###
### testsuite currently broken, needs some debugging
###
# check() {
#   cd "${srcdir}/${_pkgbase}-${pkgver}"
# 
#   export CTEST_PARALLEL_LEVEL=8
#   export CTEST_OUTPUT_ON_FAILURE=1
#   VERBOSE=1 make -C build check
# 
#   # sometimes processes are not properly terminated...
#   for process in ceph-mon ceph-mgr ceph-osd; do
#     pkill -9 "${process}" || true
#   done
# }

package_ceph-pacific-libs() {
  depends=('boost-libs' 'curl' 'glibc' 'keyutils' 'libutil-linux' 'bzip2' 'lz4' 'nss'
           'oath-toolkit' 'python' 'snappy' 'systemd-libs' 'fmt')
  provides=("ceph-libs=${pkgver}")
  conflicts=("ceph-libs")

  cd "${srcdir}/${_pkgbase}-${pkgver}"

  # main install
  VERBOSE=1 make DESTDIR="${pkgdir}" -C build install

  # remove stuff that goes into the ceph package
  rm -rf "${pkgdir}"/usr/lib/{ceph/mgr,systemd,sysusers.d,tmpfiles.d}
  rm -rf "${pkgdir}/usr/share"
  rm -rf "${pkgdir}/usr/sbin"
  rm -rf "${pkgdir}/usr/bin"
  rm -rf "${pkgdir}/etc"
  rm -rf "${pkgdir}/var"
}

package_ceph-pacific() {
  depends=("ceph-pacific-libs=${pkgver}-${pkgrel}"
           'boost-libs' 'curl' 'fuse2' 'fuse3' 'fmt' 'glibc' 'gperftools' 'java-runtime'
           'keyutils' 'leveldb' 'libaio' 'libutil-linux' 'librdkafka'
           'lsb-release' 'ncurses'
           'nss' 'oath-toolkit' 'python' 'python-bcrypt' 'python-setuptools'
           'python-prettytable' 'python-cmd2' 'python-dateutil' 'snappy' 'sudo' 'systemd-libs'
           'python-flask' 'python-pecan' 'python-pyopenssl' 'python-requests' 'python-werkzeug' 'xfsprogs'
           'python-yaml' 'python-pyaml')
  provides=("ceph=${pkgver}")
  conflicts=("ceph")

  cd "${srcdir}/${_pkgbase}-${pkgver}"

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
  rm -rf "${pkgdir}"/usr/lib/{ceph/{compressor,crypto,erasure-code},rados-classes}
  rm -rf "${pkgdir}"/usr/lib/python*
  rm -rf "${pkgdir}/usr/include"

  # remove stuff that is in the ceph-mgr package
  rm -rf "${pkgdir}"/usr/{bin/ceph-mgr,share/ceph/mgr,lib/systemd/system/ceph-mgr*}

  # remove _test_ binaries from the package, not needed
  find "${pkgdir}/usr/bin" -maxdepth 1 -type f -iname 'ceph_test_*' -delete

  # install tmpfiles.d and sysusers.d stuff
  install -Dm644 "${srcdir}/${_pkgbase}-${pkgver}/systemd/ceph.tmpfiles.d" \
    "${pkgdir}/usr/lib/tmpfiles.d/${_pkgbase}.conf"
  install -Dm644 "${srcdir}/ceph.sysusers" \
    "${pkgdir}/usr/lib/sysusers.d/${_pkgbase}.conf"

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
  install -D -d -m750 -o   0 -g 340 "${pkgdir}/etc/ceph"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/log/ceph"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph/bootstrap-mds"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph/bootstrap-osd"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph/bootstrap-rgw"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph/mon"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph/osd"
}

package_ceph-pacific-mgr() {
  depends=("ceph-pacific=${pkgver}-${pkgrel}" "ceph-pacific-libs=${pkgver}-${pkgrel}"
           'bash' 'boost-libs' 'coffeescript' 'curl' 'gperftools' 'nodejs' 'nss'
           'python' 'python-cherrypy' 'python-flask-restful' 'python-pecan'
           'python-pyjwt' 'python-routes' 'python-jsonpatch' 'python-more-itertools' 'python-numpy'
           'python-scipy' 'python-six')
  optdepends=('python-influxdb: influx module'
              'python-kubernetes: rook module'
              'python-prometheus_client: prometheus module'
              'python-remoto: ssh module')
  provides=("ceph-mgr=${pkgver}")
  conflicts=('ceph-mgr')

  cd "${srcdir}/${_pkgbase}-${pkgver}"

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
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph/mgr"
}

# vim:set ts=2 sw=2 et:
