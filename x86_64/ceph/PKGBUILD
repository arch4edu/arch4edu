# Maintainer: Paul Stemmet <aur@luxolus.com>
# Contributor: Thore Bödecker <foxxx0@archlinux.org>
# Contributor: Sébastien "Seblu" Luttringer <seblu@archlinux.org>

pkgbase='ceph'
pkgdesc='Distributed, fault-tolerant storage platform delivering object, block, and file system'
pkgver=18.2.4
pkgrel=3
url='https://ceph.com/'
arch=('x86_64')
license=('GPL-2.0-or-later OR LGPL-2.1-or-later OR LGPL-3.0-or-later')
pkgname=(
  ceph-{common,compressor,crypto,erasure,tools,test,volume,cephadm,node-proxy}
  ceph-{rados,base,mon,mgr,osd,mds,rbd,cephfs,rgw}
  lib{rados,cephfs,rbd,rgw,cephsqlite}
  python-{ceph-common,rados,rbd,cephfs,rgw}
  cephfs-{top,shell}
  java-cephfs

  ceph
  ceph-libs
  ceph-cluster
  ceph-cli
)
makedepends=(
  'bash'            'boost'            'boost-libs'      'cmake'           'coreutils'
  'cryptsetup'      'curl'             'cython'          'expat'           'fmt'
  'fuse3'           'gawk'             'gcc-libs'        'git'             'glibc'
  'gperf'           'gperftools'       'java-runtime'    'jq'              'jre11-openjdk-headless'
  'junit'           'keyutils'         'libaio'          'libatomic_ops'   'libcap'
  'libcap-ng'       'libcurl-compat'   'libedit'         'libgudev'        'libnl'
  'librabbitmq-c'   'librdkafka'       'libutil-linux'   'libuv'           'libxcrypt'
  'lua'             'lz4'              'nss'             'oath-toolkit'    'openssl'
  'pkgconf'         'python'           'snappy'          'sqlite'          'systemd-libs'
  'thrift'          'util-linux'       'xfsprogs'        'zlib'            'zstd'

  'python-bcrypt'     'python-cherrypy'  'python-coverage'     'python-dateutil'  'python-jinja'
  'python-packaging'  'python-pecan'     'python-prettytable'  'python-pyjwt'     'python-pyopenssl'
  'python-requests'   'python-scipy'     'python-setuptools'   'python-sphinx'    'python-typing_extensions'
  'python-werkzeug'   'python-yaml'

  # python-bcrypt makedepends
  'python-build'   'python-installer'   'python-setuptools-rust'   'python-wheel'
)
checkdepends=(
  'inetutils'     'xmlstarlet'

  'python-nose'   'python-pycodestyle'   'python-pylint'   'python-pytest'   'python-pytest-cov'
)
__bcrypt_version='4.1.3'

# Despite the upstream suggesting that LTO is now possible, I still am unable
# to set this. I get SEGVs in tests, and repeated mentions of C++ One Definition Rule
# violations in builds -- probably causing the segfaults. Need to look into this some
# more before I enable it.
# See: https://github.com/ceph/ceph/pull/42602
options=('emptydirs' '!lto')
source=(
  "https://download.ceph.com/tarballs/${pkgbase}-${pkgver}.tar.gz"
  'ceph.sysusers'
  'ceph.sudoers'
  'ceph-13.2.2-dont-install-sysvinit-script.patch'
  'ceph-disable-empty-readable.sh-test.patch'

  # Avoid spurious failures in logrotate when duplicate rule files exist,
  # typically around cephadm auto-generated rotate rules
  'ceph-17.2.5-logrotate-ignore-dups.patch'

  # Test wants to use `git ls-files`, and is sad when it finds itself not running in a
  # git repo
  'ceph-17.2.4-tox-flake8-git-ls-files.patch'

  # Split up a very IO heavy test suite, as otherwise test is liable to timeout
  # NOTE: this is a very large patchset and will guarrented break if/when the upstream
  # touches anything in src/test/objectstore
  'ceph-17.2.4-test-bluefs-split.patch'

  # pybind cython modules seem to have a longstanding issue with incorrectly mocking
  # cythonize calls in setup.py when 'egg_info' is a provided directive
  'ceph-17.2.4-pybind-unmock-cythonize.patch'

  # fixes the few usages of std::iterator which has been deprecated in c++17, quieting
  # a lot of _GLIBCXX17_DEPRECATED line noise during builds
  'ceph-17.2.5-fix-iterator-depreciations.patch'

  # Fixes API changes to boost::beast string_view type def in 1.81
  # https://github.com/boostorg/beast/issues/2594
  'ceph-17.2.5-rgw-client-boost-string-view.patch'

  # Fixes inspect.getargspec errors due to removal in py3.11
  'ceph-17.2.6-mgr-dashboard-cherrypy-18.patch'

  # Fixes inspect.formatargspec errors in pylint2.6->wrapt due to removal in py3.11
  'ceph-17.2.6-mgr-dashboard-pylint-217.patch'

  # Fixes a couple breaking changes from cython v3.0.0
  'ceph-17.2.6-cython-fixes.patch'

  # Fixes fmtlib v10 issues found in v18.2.x
  'ceph-18.2.0-fmt10-fixes.patch'

  # Fix undefined behavior in unit test for erasure coding (SHEC)
  'ceph-18.2.0-fix-ecode-shec-test.patch'

  # Backport https://github.com/ceph/ceph/pull/50216 to fix an assertion failure in
  # test_concurrent_dir_link_and_compact_log_56210 due to the strange mount/umount/mount
  # pattern
  'ceph-18.2.0-backport-log-runway-expansion.patch'

  # Make the mgr import our ceph_bcrypt fork instead of the system bcrypt
  'ceph-18.2.2-mgr-alias-ceph-bcrypt.patch'

  # Backport of https://github.com/ceph/ceph/pull/53327
  'ceph-18.2.2-backport-ceph-volume-unbound-var.patch'

  # Fix a few compile errors when using GCC14
  'ceph-18.2.2-gcc-14-fixes.patch'

  # Switch to using std::atomic<std::shared_ptr<T>> where possible
  'ceph-18.2.2-std-atomic-depreciations.patch'

  # Disable a performance test that regressed, while the upstream is deciding
  # how to fix it
  'ceph-18.2.2-test-mempool-shard-select-disable.patch'

  # Since py3.11, but exacerbated in py3.12 there are a bunch of linting errors
  # that we do not care about, so disable them
  'ceph-18.2.2-disable-mypy-flake8-tests.patch'

  # Fix a host of issues from py3.12 in the pybind / cephadm code
  'ceph-18.2.2-py312-fixes.patch'

  # Fixes for 3 problems found when using boost 1.86
  # - casting uuid to *char
  # - missing header for boost::mt11213b
  # - undef of Boost.MPL header before including <boost/python/*> headers
  'ceph-18.2.4-boost-1.86-fixes.patch'

  # Since fmt 11 we are seeing widespread compile errors because
  # various custom type fmt:formatter::format defintions are not const.
  'ceph-18.2.4-fmt-formatter-const.patch'

  # ===== ceph-python-bcrypt sources ===== #
  "python-bcrypt-${__bcrypt_version}.tar.gz::https://github.com/pyca/bcrypt/archive/${__bcrypt_version}.tar.gz"

  # Rename bcrypt -> ceph_bcrypt
  'python-bcrypt-prefix-ceph.patch'

  # Use our fork of pyo3, reenabling subinterpreter support
  'python-bcrypt-allow-subinterpreters.patch'
)
sha512sums=('a4ebb4e14032e6ab8e1fd8836f39234b771cb0a4b655166e9c69493a2c0d687064af4bb35523d0501629605521854e49f5c53a56279f72810d108c76f4f88c5b'
            '4354001c1abd9a0c385ba7bd529e3638fb6660b6a88d4e49706d4ac21c81b8e829303a20fb5445730bdac18c4865efb10bc809c1cd56d743c12aa9a52e160049'
            '41dbc1c395cdf9b3edf5c5d91bbc90f416b4338ad964fa3471f26a4312d3ec2a5dcebbc351a1640dc4b047b4f71aa134ac7486747e5f62980092b0176e7567f5'
            'ea069b75b786c22166c609b127b512802cc5c6e9512d792d7b7b34d276f5b86d57c8c35cfc7b5c855a59c0ba87ba1aabe2ca26da72b26bff46b6ba8410ddb27e'
            '2234d005df71b3b6013e6b76ad07a5791e3af7efec5f41c78eb1a9c92a22a67f0be9560be59b52534e90bfe251bcf32c33d5d40163f3f8f7e7420691f0f4a222'
            'b12cabda7184721c494edd22250fd05019694d2bc445722d100cdefab5385bd25c2267a029d2f6053932fa6717e38c4314385afd986969ee2744d745b53c8b58'
            '31e578b240ceaaf1216b56cdce654661eed6529ef642ecad164a02669e850100a49a85dc70f3d744671e2c5dad10aee64be7d091fa33007cb8fc6788a4336799'
            '5b43ba48dde8b7371d4b3976aa3a27ab3ad3a10e110479a101b8f222590bbd6aca318f3ac117f851596fc23daafb53aaa566e055dc9694ab16ab1170e8f77763'
            '781a01e622a70d56bf1948bdc0b427ffa95a86cec7dd9d26c6007a9ec024a942a8ca55f2acc3d37344862f1d6bf11cae998d8071754cd841a66bfba4ec9c58bf'
            '612faebfb5eec3651832f349ea3c23b50d2386889ff77592b0acff653049efdc5c2254f63c30d88b9a730813bf1f1945dda0d0beab0db7db3e0708ba8d057a40'
            '02ca1a9bf15f9cd6f474f264ba2bf66ae725bac990a7cac315dabe377c66935a7afd8117f18a1f82c78bdf9ab2c3e5a2a227f2ffc166974dd7bb99b290f1f233'
            '79be1630ae4a599509e5d789d4aefe412ce47e67ad482f853664fa4b01e063c20593e3da668e6a776ad038fb07606ae948eea41bab20776c33c87f9ab49505e0'
            'c767a8e6fd02ea2ab88e99b50b206d0f825acdf177136ded38d93594fc7663b7c9612af7195b85e0b2b501d8ee482af5e088e9abb5ebee7b8a69e0153ce89782'
            '0c5124693bd317a73707dfd34b17664cc05233aec08e07739fe08fc9a73be7a1f4446052b1addde832cba141a382c35f45e60c89a00bb7dab81cee7ed6be07e1'
            '24f0a0e543cb9ee4006340362b43c9927861b3f0403aa929a0713a5a51220b5186f2a8c36d74a36970eeb230bace5239bf471d2f5b463ed3d9c311ad3da5a26c'
            '9a1183c08f8799b14235c9271519203cbf93e48ca3a8607d3a0500910efca5379c8a08421c377227f93d8436a850f5ca99784f28aaa920e55f0457c657511f17'
            'e238b326609636bc7dd10cec59290e22898948ef105c49643c38d2621abf16c2efcf9581b0b6bad65066607510c9827d00a7abdb14f2054701cc33b7101ea054'
            '692b9cea0199366fdfbcaff2d9590e3a1e439b948a1a5030215e81fcc8a22ac562b3261e2057470cc8acc20f404869a5a0c4550177788dc2f824523e5267b1eb'
            '11fae8997e4df4b706245f467dc396d84f1fb48db8e569b1665a4963eb77292415a2493cae033bed23765d82269a3cd6a5bf12c1ba52e3700a63db6ad983ca5a'
            '3f3a4795dfc58910972fa15a7ca8a4c3206d45351a15db66d8e93da64c7726c5f45256114b20f032d8011ab131ee20d2d8373207ad7e188a2978cf50854e10f1'
            '2c90c69b3e236622c9fb83214fe7f781c9fcb0de1b372e7837d9963780ead9c2926c347177c03fb94eb05fd838514f3afab42aa50b7c9ac800c34bf59c48b02e'
            '0ed97f2fb764ec8f7e01be45256377a6b2f451c865348b25b12ca9ef70c7120a0bf62321a9402cc4362618fde3a38ccfcd6eec738fe8cc067f17399700c273f3'
            '3a6d2bee9a403ac7a0a1216fd704bb86337abf2498c1e90be70e8221779705c47cdc994f7147bcac5b99b939aa20dd0359c5eaf02224ae80183fbb7c1b7df792'
            '15c6a1d2bdd524a7836ad9bad12c4103a32274ad1fa5182231bcbc626e44fcfbdba04b6d55c67ef13952821da46df68e0b51ab4534c3a8830eac301e18662195'
            '73f72759a3d628575447b7607b7e27b0bab4a70b206c91daa717d461ada5fd9985c16f5782d9cb4406bd314ae9cf683cca43ab426505ab21f99141518e32533d'
            'a053c2e0abf91528fa39723784f274daeec4ca078464a7e4ebe50c1f2f2264130bf746be59d3899e114c08cf43e5e6af2b84023254a0329670e50a2bca4c51a7'
            '59a5aafc729a6e7ac61121469bbca73809d87cafc1b16dcb0701c33fccc6298eff1071680c364042c46f91d701830a414e6ecf0bff4bee9500e4ce146dcad974'
            '26e4569396005f7461764dbe57634ab6d20ca9bfe777b4eeae3def8e3c887333b4d64470ad1db15a8170979f85372c111abfc043bdc1deae219183cc7539980e'
            '477e9f70c985da94c25bcac21f0f4f148623563a4c97b7249524cd82867ec2042488f37f966e75de636e6f835f9be6a8f9ea435374d714ca7d0d0cd71340b0b8')
__version="${pkgver}-${pkgrel}"

# -fno-plt causes linker errors (undefined reference to internal methods)
# similar issue: https://bugs.archlinux.org/task/54845
# https://github.com/intel/media-driver/commit/d95d8f7ab7ac94a2e0f4ee6a4b4794898dc2d3b7
# as of today (2019-07-12) the upstream maintainers do not consider this a bug in their code
# (IMHO rightfully so) and thus we strip the option here
export CFLAGS="${CFLAGS/-fno-plt/}"
export CXXFLAGS="${CXXFLAGS/-fno-plt/}"


prepare() {
  cd "${srcdir}/${pkgbase}-${pkgver}"

  _prepare_ceph_python_bcrypt

  # apply patches from the source array
  local filename
  for filename in "${source[@]%%::*}"; do
    if [[ "${filename}" =~ \.patch$ ]] \
    && [[ "${filename}" =~ ^ceph-.* ]]; then
      echo "Applying patch ${filename##*/}"
      patch -p1 -N -i "${srcdir}/${filename##*/}"
    fi
  done

  # fix boost stuff for system-boost
  find . -name '*.cmake' -or -name 'CMakeLists.txt' -print0 | xargs --null \
    sed -r \
    -e 's|Boost::|boost_|g' \
    -e 's|Boost_|boost_|g' \
    -e 's|[Bb]oost_boost|boost_system|g' -i || exit 1

  # fmt 11 moved the FMT_VERSION #define to fmt/base.h
  # there's little point in creating a patch for this,
  # as ceph 19 no longer uses Findfmt.cmake at all
  sed \
    -i \
    -e 's|set(_fmt_version_file "${fmt_INCLUDE_DIR}/fmt/core.h")|set(_fmt_version_file "${fmt_INCLUDE_DIR}/fmt/base.h")|' \
    cmake/modules/Findfmt.cmake

  # remove tests that require root privileges
  rm src/test/cli/ceph-authtool/cap*.t
  sed -i '/add_ceph_test(mgr-dashboard-smoke.sh/d' src/test/mgr/CMakeLists.txt

  # disable/remove broken tests
  sed -i '/add_ceph_test(smoke.sh/d' src/test/CMakeLists.txt
  sed -i '/add_ceph_test(safe-to-destroy.sh/d' src/test/osd/CMakeLists.txt

  # Add our bcrypt build to the tox envs
  for filename in src/pybind/mgr/{,dashboard/}requirements.txt; do
    grep -qiF 'ceph_bcrypt' $filename \
    || printf -- '%s\n' \
        "--find-links=${srcdir}/bcrypt-${__bcrypt_version}/dist" \
        "ceph_bcrypt" \
        >> $filename
  done

  # The mgr C++ daemon injects a 'ceph_module' python module into the context
  # of all python mgr modules, but this is absent from test code.
  #
  # I don't understand how this worked previously, but since py3.12 the machinery
  # the upstream to mock the ceph_module... module doesn't work, so we copy the
  # mocks into a technically real, importable python module.
  #
  # Note: this must be removed from the installed files!
  install -vD src/pybind/mgr/tests/__init__.py src/pybind/ceph_module/__init__.py
}

build() {
  cd "${srcdir}/${pkgbase}-${pkgver}"

  _build_ceph_python_bcrypt

  export CFLAGS+=" ${CPPFLAGS}"
  export CXXFLAGS+=" ${CPPFLAGS}"
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
    -DENABLE_GIT_VERSION=ON \
    -DWITH_BABELTRACE=OFF \
    -DWITH_LTTNG=OFF \
    -DWITH_BLKIN=OFF \
    -DWITH_JAEGER=OFF \
    -DWITH_FIO=OFF \
    -DWITH_OPENLDAP=OFF \
    -DWITH_RDMA=OFF \
    -DWITH_OCF=OFF \
    -DWITH_DPDK=OFF \
    -DWITH_SPDK=OFF \
    -DWITH_QAT=OFF \
    -DWITH_QATZIP=OFF \
    -DWITH_RBD=ON \
    -DWITH_RBD_RWL=ON \
    -DWITH_RBD_SSD_CACHE=ON \
    -DWITH_RBD_MIRROR=ON \
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
    -DWITH_RADOSGW_BEAST_OPENSSL=ON \
    -DWITH_RADOSGW_AMQP_ENDPOINT=ON \
    -DWITH_RADOSGW_KAFKA_ENDPOINT=ON \
    -DWITH_RADOSGW_LUA_PACKAGES=ON \
    -DWITH_RADOSGW_DBSTORE=OFF \
    -DWITH_RADOSGW_SELECT_PARQUET=OFF \
    -DWITH_RADOSGW_MOTR=OFF \
    -DWITH_RADOSGW_DAOS=OFF \
    -DWITH_SYSTEMD=ON \
    -DWITH_SYSTEM_BOOST=ON \
    -DWITH_SYSTEM_ZSTD=ON \
    -DWITH_SYSTEM_UTF8PROC=ON \
    -DWITH_SYSTEM_GTEST=OFF \
    -DWITH_SYSTEM_NPM=OFF \
    -DENABLE_SHARED=ON \
    -DWITH_TESTS=ON \
    -Wno-dev

  make -C build legacy-option-headers
  make -C build all
}

check() {
  cd "${srcdir}/${pkgbase}-${pkgver}"

  _check_ceph_python_bcrypt

  export CTEST_PARALLEL_LEVEL=$(nproc --ignore=4 || echo "4")
  export CTEST_OUTPUT_ON_FAILURE=1

  make -C build check || true
}

_package() {
  local p="$1" f d; shift
  for f in "$@"; do
    d="$srcdir/__pkg__/$p/${f#${_staging}/}"
    mkdir -p "$(dirname "$d")"
    mv -v "$f" "$d"
    rmdir -p --ignore-fail-on-non-empty "$(dirname "$f")"
  done
}

_print() {
  (
    cd "$pkgdir" && \
    find . -type f,l -print0 \
      | xargs --null -I@ echo '    > @'
  )
}

# Real packaging function, make sure to call this in the *first*
# package_() function makepkg calls
#
# Keep in mind that adding _package lines here does nothing unless
# that package is:
# 1. Referenced in pkgname=()
# 2. Has a package_<name>() function defined for it
_make_ceph_packages() {

  # Main install
  local install="${pkgdir}/staging" ; mkdir "${install}"
  make DESTDIR="${install}" -C "${srcdir}/${pkgbase}-${pkgver}/build" install

  # Clear _package cache
  rm -rf "${srcdir}/__pkg__" || :

  (
    cd "${install}"

    pyv=$(python -c 'import sys ; v = sys.version_info ; print("%d.%d" %(v[0], v[1]))')

    lib=usr/lib
    inc=usr/include
    bin=usr/bin
    sbin=usr/sbin
    share=usr/share
    etc=etc
    python=$lib/python${pyv}/site-packages
    systemd=$lib/systemd/system
    man=$share/man

    ###############################################
    #         Print install files                 #
    ###############################################

    printf '##### CEPH INSTALL ' ; printf '%0.s#' {1..29} ; printf '\n'
    find . | sed -e 's|^\./||'
    printf '##### CEPH INSTALL ' ; printf '%0.s#' {1..29} ; printf '\n'

    ###############################################
    #         Install pruning                     #
    ###############################################

    # Remove 'tests' directories
    find . -depth -type d -name 'tests' -exec rm -vr '{}' \+

    # Remove most common test bins/scripts
    find . -depth -type f,l -name '*test*' -exec rm -v '{}' \+

    # $share/ceph/mgr/test_orchestrator
    find . -depth -type d -name 'test_orchestrator' -exec rm -vr '{}' \+

    # Live test tools
    rm -v  $bin/ceph_scratchtool{,pp}
    rm -rv $bin/ceph_psim
    rm -rv $bin/ceph-run $man/man8/ceph-run.8
    rm -rv $bin/ceph_multi_stress_watch
    rm -rv $bin/ceph-coverage

    # Old ssh key stuff
    rm -vf $share/ceph/*drop.ceph*

    # TODO: Move this into a patch
    # Fix EnvironmentFile location in systemd service files
    sed -i -e 's|/etc/sysconfig/|/etc/conf.d/|g' $systemd/*.service

    # Fix bash completions path
    install -d -m 755 "$share/bash-completion"
    mv -v $etc/bash_completion.d $share/bash-completion/completions

    # TODO: Move this into a patch
    # Fix sbin dir (cmake opt seems to have no effect)
    mv -v $sbin/* $bin/
    rm -vrf $sbin

    ###############################################
    #         Ceph core libraries                 #
    ###############################################

    _package ceph-compressor \
      $lib/ceph/compressor/*

    _package ceph-crypto \
      $lib/ceph/crypto/*

    _package ceph-erasure \
      $lib/ceph/erasure-code/*

    _package ceph-common \
      $bin/crushtool \
      $bin/ceph-authtool \
      $bin/ceph-conf \
      $lib/ceph/ceph_common.sh \
      $lib/ceph/libceph-common.so.2 \
      $lib/ceph/extblkdev/libceph_ebd_vdo.so \
      $lib/ceph/denc/* \
      $share/doc/ceph/sample.ceph.conf \
      $man/man8/crushtool.8 \
      $man/man8/ceph-{conf,authtool}.8

    _package librados \
      $inc/rados/* \
      $inc/radosstriper/* \
      $lib/librados.so{,.2,.2.0.0} \
      $lib/libradosstriper.so{,.1,.1.0.0} \
      $lib/rados-classes/* \
      $bin/librados-config \
      $bin/ceph-clsinfo \
      $man/man8/librados-config.8 \
      $man/man8/ceph-clsinfo.8

    _package ceph-rados \
      $bin/rados \
      $bin/ceph_radosacl \
      $share/bash-completion/completions/rados \
      $man/man8/rados.8

    _package libcephsqlite \
      $inc/libcephsqlite.h \
      $lib/libcephsqlite.so

    ###############################################
    #         Ceph cluster components             #
    ###############################################

    _package ceph-base \
      $bin/ceph \
      $bin/ceph-crash \
      $share/bash-completion/completions/ceph \
      $systemd/ceph-crash.service \
      $systemd/ceph.target \
      $man/man8/ceph.8

    _package ceph-mon \
      $bin/ceph-mon \
      $bin/ceph-monstore-tool \
      $bin/monmaptool \
      $bin/ceph-create-keys \
      $lib/ceph/ceph-monstore-update-crush.sh \
      $systemd/ceph-mon{.target,@.service} \
      $man/man8/{ceph-mon,monmaptool}.8 \
      $man/man8/ceph-create-keys.8

    _package ceph-mgr \
      $bin/ceph-mgr \
      $bin/ceph-exporter \
      $systemd/ceph-mgr{.target,@.service} \
      $systemd/ceph-exporter.service \
      $share/ceph/mgr/*

    _package ceph-osd \
      $bin/ceph-osd \
      $bin/ceph-{osdomap,bluestore}-tool \
      $bin/osdmaptool \
      $bin/crushdiff \
      $bin/ceph-objectstore-tool \
      $lib/ceph/ceph-osd-prestart.sh \
      $systemd/ceph-osd{.target,@.service} \
      $systemd/ceph-volume@.service \
      $man/man8/{ceph-{osd,bluestore-tool},osdmaptool,crushdiff}.8

    _package ceph-mds \
      $bin/ceph-mds \
      $systemd/ceph-mds{.target,@.service} \
      $man/man8/ceph-mds.8

    _package ceph-rgw \
      $bin/ceph_rgw_{jsonparser,multiparser} \
      $bin/rgw-* \
      $bin/radosgw* \
      $bin/ceph-diff-sorted \
      $systemd/ceph-radosgw{.target,@.service} \
      $share/bash-completion/completions/radosgw-admin \
      $man/man8/radosgw{,-admin}.8 \
      $man/man8/rgw-orphan-list.8 \
      $man/man8/ceph-diff-sorted.8 \
      $man/man8/rgw-policy-check.8

    ###############################################
    #         Ceph clients / applications         #
    ###############################################

    _package librbd \
      $inc/rbd/* \
      $lib/librbd.so{,.1,.1.18.0} \
      $lib/ceph/librbd/*

    _package ceph-rbd \
      $bin/ceph-rbdnamer \
      $bin/rbd{,map,-{fuse,mirror,nbd,replay,replay-many}} \
      $bin/ceph-immutable-object-cache \
      $systemd/ceph-rbd-mirror{.target,@.service} \
      $systemd/ceph-immutable-object-cache{.target,@.service} \
      $systemd/rbdmap.service \
      $share/bash-completion/completions/rbd \
      $man/man8/ceph-rbdnamer.8 \
      $man/man8/ceph-immutable-object-cache.8 \
      $man/man8/rbd*

    _package libcephfs \
      $inc/cephfs/* \
      $lib/libcephfs.so{,.2,.2.0.0}

    _package ceph-cephfs \
      $bin/cephfs-{data-scan,{journal,table}-tool,mirror} \
      $bin/ceph-fuse \
      $bin/mount.{ceph,fuse.ceph} \
      $bin/ceph-client-debug \
      $systemd/cephfs-mirror{.target,@.service} \
      $systemd/ceph-fuse{.target,@.service} \
      $man/man8/ceph-fuse.8 \
      $man/man8/mount.{ceph,fuse.ceph}.8 \
      $man/man8/cephfs-*

    _package librgw \
      $lib/librgw.so{,.2,.2.0.0}

    _package ceph-cephadm \
      $bin/cephadm \
      $man/man8/cephadm.8

    _package ceph-volume \
      $bin/ceph-volume{,-systemd} \
      $python/ceph_volume \
      $python/ceph_volume-*egg-info* \
      $man/man8/ceph-volume{,-systemd}.8

    _package cephfs-shell \
      $bin/cephfs-shell \
      $python/cephfs_shell-*

    _package cephfs-top \
      $bin/cephfs-top \
      $python/cephfs_top-*

    _package ceph-node-proxy \
      $bin/ceph-node-proxy \
      $python/ceph_node_proxy \
      $python/ceph_node_proxy-*egg-info*

    ###############################################
    #         Ceph misc. utils                    #
    ###############################################

    _package ceph-tools \
      $bin/ceph-post-file \
      $bin/ceph-dedup-tool \
      $bin/ceph-erasure-code-tool \
      $bin/ceph-kvstore-tool \
      $bin/ceph-debugpack \
      $bin/ceph-dencoder \
      $man/man8/ceph-{post-file,dencoder}.8 \
      $man/man8/ceph-{debugpack,kvstore-tool}.8

    _package ceph-test \
      $bin/ceph_perf_local \
      $bin/ceph_perf_msgr_client \
      $bin/ceph_perf_msgr_server \
      $bin/ceph_erasure_code_benchmark \
      $bin/ceph_objectstore_bench \
      $bin/ceph_bench_log \
      $bin/ceph_perf_objectstore \
      $bin/ceph_omapbench \
      $bin/ceph-syn \
      $man/man8/ceph-syn.8

    _package java-cephfs \
      $lib/libcephfs_jni.so{,.1,.1.0.0} \
      $share/java/libcephfs.jar

    ###############################################
    #         Ceph python packages                #
    ###############################################

    _package python-ceph-common \
      $python/ceph \
      $python/ceph-*egg-info* \
      $python/ceph_argparse.py \
      $python/ceph_daemon.py

    _package python-rados \
      $python/rados-* \
      $python/rados.cpython-*

    _package python-rbd \
      $python/rbd-* \
      $python/rbd.cpython-*

    _package python-cephfs \
      $python/cephfs-* \
      $python/cephfs.cpython-*

    _package python-rgw \
      $python/rgw-* \
      $python/rgw.cpython-*

  )

  local -i _ret=$(find "${install}" -type f,l | wc -l)
  if (( _ret > 0 )) ; then
    echo "[ERROR] Files were found after packaging! Bailing out!"
    echo "        Please ensure all files are either moved or"
    echo "        deleted before package_ceph-common() completes."
    ( cd "${install}" && find . -type f,l | sed -e 's|^\./||' )
    return 1
  else
    rm -rf "${install}"
  fi

  return 0
}

###############################################
#         Ceph core libraries                 #
###############################################

package_ceph-common() {
  pkgdesc='Ceph Storage common libraries and dependencies'
  depends=(
    "ceph-compressor=${__version}"   "ceph-crypto=${__version}"   "ceph-erasure=${__version}"

    'boost-libs'   'curl'           'glibc'    'keyutils'     'libutil-linux'
    'nss'          'systemd-libs'   'bash'     'fmt'          'cryptsetup'
    'libxcrypt'    'libaio'         'libcap'   'gperftools'
  )
  provides=(
    'libceph-common.so'    'libceph_ebd_vdo.so'
  )

  #============================================#
  # This section needs to be run in the first  #
  # package function makepkg calls to populate #
  # the contents of each package function.     #
  _make_ceph_packages
  #============================================#

  mv __pkg__/$pkgname/* "$pkgdir"

  # sysusers
  install -Dm644 "${srcdir}/ceph.sysusers" \
    "${pkgdir}/usr/lib/sysusers.d/${pkgbase}.conf"

  # Prepare conf dir
  install -D -d -m755 -o   0 -g 340 "${pkgdir}/etc/ceph"

  _print
}

package_ceph-compressor() {
  pkgdesc='Ceph Storage compressor libs'
  depends=(
    'gcc-libs' 'lz4' 'snappy' 'zlib' 'zstd'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_ceph-crypto() {
  pkgdesc='Ceph Storage crypto libs'
  depends=(
    'gcc-libs' 'openssl'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_ceph-erasure() {
  pkgdesc='Ceph Storage erasure coding libs'
  depends=(
    'gcc-libs'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_librados() {
  pkgdesc='Ceph Storage client library to the RADOS distributed object store'
  depends=(
    "ceph-common=${__version}"

    'bash'   'boost-libs'   'fmt'   'lua'   'oath-toolkit'
  )
  provides=(
    'libradosstriper.so'   'librados.so'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_ceph-rados() {
  pkgdesc='Ceph Storage utilities and tools for librados'
  depends=(
    "librados=${__version}"

    'gcc-libs'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_libcephsqlite() {
  pkgdesc='Ceph Storage client library for a RADOS backed sqlite3 VFS extension'
  depends=(
    "librados=${__version}"

    'fmt'
  )
  provides=(
    'libcephsqlite.so'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

###############################################
#         Ceph cluster components             #
###############################################

package_ceph-base() {
  pkgdesc='Ceph Storage cluster base utilities and configuration'
  depends=(
    "ceph-common=${__version}" "librados=${__version}" "python-ceph-common=${__version}" "python-rados=${__version}"

    'python'
  )
  backup=(
    'etc/logrotate.d/ceph'
    'etc/sudoers.d/90-ceph'
  )

  mv __pkg__/$pkgname/* "$pkgdir"

  # tmpfiles
  install -Dm644 "${srcdir}/${pkgbase}-${pkgver}/systemd/ceph.tmpfiles.d" \
    "${pkgdir}/usr/lib/tmpfiles.d/${pkgbase}.conf"
  # logrotate
  install -Dm644 "${srcdir}/${pkgbase}-${pkgver}/src/logrotate.conf" \
    "${pkgdir}/etc/logrotate.d/ceph"
  # sudoers (for disk monitoring)
  install -Dm640 "${srcdir}/ceph.sudoers" \
    "${pkgdir}/etc/sudoers.d/90-ceph"
  chmod 750 "${pkgdir}/etc/sudoers.d"

  # Prepare log, state dirs
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/log/ceph"
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph"

  _print
}

package_ceph-mon() {
  pkgdesc='Ceph Storage cluster monitor daemon, for distributed state storage via PAXOS'
  depends=(
    "ceph-base=${__version}"

    'bash'   'boost-libs'   'fmt'   'gperftools'   'snappy'
  )

  mv __pkg__/$pkgname/* "$pkgdir"

  # Prepare state dir
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph/mon"

  _print
}

package_ceph-mgr() {
  pkgdesc='Ceph Storage cluster manager daemon, the API gateway for cluster management'
  depends=(
    "ceph-base=${__version}"   "python-cephfs=${__version}"   "python-rbd=${__version}"   "libcephsqlite=${__version}"

    'sqlite'   'python'   'boost-libs'   'fmt'   'gperftools'

    'python-bcrypt'     'python-cheroot'    'python-cherrypy'   'python-coverage'    'python-dateutil'
    'python-jinja'      'python-jsonpatch'  'python-packaging'  'python-pecan'       'python-prettytable'
    'python-pyopenssl'  'python-requests'   'python-scipy'      'python-setuptools'  'python-typing_extensions'
    'python-urllib3'    'python-werkzeug'   'python-yaml'
  )
  optdepends=(
    'cephadm: Required if cluster is managed via cephadm'
    'python-kubernetes: For mgr/module:rook,k8sevents'
    'python-numpy: For mgr/module:diskprediction_local'
    'python-influxdb: For mgr/module:influx'
  )

  # Prepare state dir
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph/mgr"

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_ceph-osd() {
  pkgdesc='Ceph Storage cluster object storage daemon, for managing block devices'
  depends=(
    "ceph-base=${__version}"

    'fuse3'    'bash'     'boost-libs'     'fmt'      'gperftools'
    'libaio'   'snappy'   'systemd-libs'   'python'
  )
  optdepends=(
    'ceph-volume: For preparing block devices for OSD daemons'
    'ceph-node-proxy: For RedFishAPI hardware metrics'
    'smartmontools: disk monitoring via S.M.A.R.T'
    'nvme-cli: disk monitoring for NVMe drives'
  )
  backup=(
    'etc/sysctl.d/90-ceph-osd.conf'
  )

  mv __pkg__/$pkgname/* "$pkgdir"

  # Prepare state dirs
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph/bootstrap-osd"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph/osd"

  # sysctls
  sed -i -e '/kernel.pid_max/d' \
    "${srcdir}/${pkgbase}-${pkgver}/etc/sysctl/90-ceph-osd.conf"
  install -Dm644 "${srcdir}/${pkgbase}-${pkgver}/etc/sysctl/90-ceph-osd.conf" \
    "${pkgdir}/etc/sysctl.d/90-ceph-osd.conf"

  _print
}

package_ceph-mds() {
  pkgdesc='Ceph Storage cluster metadata server, the API gateway for CephFS'
  depends=(
    "ceph-base=${__version}"

    'lua'   'fmt'   'gperftools'
  )

  mv __pkg__/$pkgname/* "$pkgdir"

  # Prepare state dirs
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph/bootstrap-mds"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph/mds"

  _print
}

package_ceph-rgw() {
  pkgdesc='Ceph Storage cluster RADOS Object Gateway daemon, for serving RESTful traffic'
  depends=(
    "librgw=${__version}"

    'gawk'            'oath-toolkit'   'boost-libs'   'expat'   'gperftools'
    'librabbitmq-c'   'librdkafka'     'lua'
  )

  # Prepare state dirs
  install -D -d -m755 -o 340 -g 340 "${pkgdir}/var/lib/ceph"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph/bootstrap-rgw"
  install -D -d -m750 -o 340 -g 340 "${pkgdir}/var/lib/ceph/rgw"

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

###############################################
#         Ceph clients / applications         #
###############################################

package_librbd() {
  pkgdesc='Ceph Storage client library for RADOS block devices'
  depends=(
    "librados=${__version}"

    'cryptsetup' 'fmt'
  )
  provides=(
    'librbd.so' 'libceph_librbd_parent_cache.so'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_ceph-rbd() {
  pkgdesc='Ceph Storage utilities and tooling for librbd'
  depends=(
    "librbd=${__version}"

    'libnl'   'fmt'          'fuse3'   'gperftools'   'boost-libs'
    'bash'    'cryptsetup'

  )
  backup=(
    'etc/udev/rules.d/50-ceph-rbd.rules'
  )

  # rbd udev rules
  install -Dm644 "${srcdir}/${pkgbase}-${pkgver}/udev/50-rbd.rules" \
    "${pkgdir}/etc/udev/rules.d/50-ceph-rbd.rules"

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_libcephfs() {
  pkgdesc='Ceph Storage client library for CephFS, a distributed POSIX filesystem'
  depends=(
    "librados=${__version}"

    'fmt'
  )
  provides=(
    'libcephfs.so'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_ceph-cephfs() {
  pkgdesc='Ceph Storage utilities and tooling for libcephfs'
  depends=(
    "libcephfs=${__version}"

    'fuse3'   'fmt'   'gperftools'   'libcap-ng'   'lua'   'python'
  )
  optdepends=(
    "cephfs-shell: Shell access to a CephFS filesystem"
    "cephfs-top: Usage and metrics for CephFS, inspired by top(1)"
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_librgw() {
  pkgdesc='Ceph Storage client library to RADOS Object Gateway, a S3 and Swift compatible REST API'
  depends=(
    "librados=${__version}"

    'librabbitmq-c'   'lua'   'librdkafka'   'expat'   'boost-libs'   'gperftools'
  )
  provides=(
    'librgw.so'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_ceph-volume() {
  pkgdesc='Ceph Storage utility for preparing block devices for use as OSDs'
  depends=(
    "python-ceph-common=${__version}" "ceph-osd=${__version}"

    'python' 'lvm2'

    'python-setuptools' 'python-importlib-metadata'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_cephfs-shell() {
  pkgdesc='Ceph Storage utility for accessing a CephFS filesystem shell'
  depends=(
    "python-ceph-common=${__version}" "python-cephfs=${__version}"

    'python' 'python-cmd2' 'python-colorama'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_cephfs-top() {
  pkgdesc='Ceph Storage utility for a top(1) inspired curses TUI for CephFS metrics'
  depends=(
    "python-ceph-common=${__version}" "python-cephfs=${__version}"

    'python'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_ceph-node-proxy() {
  pkgdesc='Ceph Storage daemon for cephadm deployments to collect RedFishAPI hardware metrics'
  depends=(
    'python'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_ceph-cephadm() {
  pkgdesc='Ceph Storage adminstration and configuration utility'
  provides=('cephadm')
  conflicts=('cephadm')
  depends=(
    'python' 'podman'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

###############################################
#         Ceph misc. utils                    #
###############################################

package_ceph-tools() {
  pkgdesc='Ceph Storage miscellaneous tooling and utilities'
  depends=(
    "ceph-base=${__version}"

    'bash'   'boost-libs'   'gperftools'   'libaio'   'libcap'
    'snappy'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_ceph-test() {
  pkgdesc='Ceph Storage tools for benchmarking and testing live clusters'
  depends=(
    "ceph-base=${__version}"

    'libcap'   'libaio'   'boost-libs'   'fmt'   'gperftools'
    'snappy'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_java-cephfs() {
  pkgdesc='Ceph Storage JNI bindings for CephFS'
  depends=(
    "libcephfs=${__version}"

    'java-runtime'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

###############################################
#         Ceph python packages                #
###############################################

package_python-ceph-common() {
  pkgdesc='Ceph Storage python module for common classes, objects and types'
  depends=(
    "ceph-common=${__version}"

    'python'

    'python-setuptools'   'python-prettytable'   'python-yaml'
  )

  mv __pkg__/$pkgname/* "$pkgdir"

  _package_ceph_python_bcrypt

  _print
}

package_python-rados() {
  pkgdesc='Ceph Storage python library for librados'
  depends=(
    "python-ceph-common=${__version}" "librados=${__version}"

    'libxcrypt'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_python-rbd() {
  pkgdesc='Ceph Storage python library for librbd'
  depends=(
    "python-ceph-common=${__version}" "python-rados=${__version}" "librbd=${__version}"

    'libxcrypt'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_python-cephfs() {
  pkgdesc='Ceph Storage python library for libcephfs'
  depends=(
    "python-ceph-common=${__version}" "python-rados=${__version}" "libcephfs=${__version}"

    'libxcrypt'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

package_python-rgw() {
  pkgdesc='Ceph Storage python library for librgw'
  depends=(
    "python-ceph-common=${__version}" "python-rados=${__version}" "librgw=${__version}"

    'libxcrypt'
  )

  mv __pkg__/$pkgname/* "$pkgdir"
  _print
}

###############################################
#         Ceph virtual targets                #
###############################################

# No package (excluding other virtual targets) should depend on any of these;
# these are convenience targets for other packagers

package_ceph-libs() {
  pkgdesc='Ceph Storage client libraries [VIRTUAL]'
  depends=(
    "librados=${__version}"
    "librbd=${__version}"
    "libcephfs=${__version}"
    "librgw=${__version}"
    "libcephsqlite=${__version}"
  )
}

package_ceph-cluster() {
  pkgdesc='Ceph Storage cluster daemons and components [VIRTUAL]'
  depends=(
    "ceph-mon=${__version}"
    "ceph-mgr=${__version}"
    "ceph-osd=${__version}"
    "ceph-mds=${__version}"
    "ceph-rgw=${__version}"
    "ceph-volume=${__version}"
  )
}

package_ceph-cli() {
  pkgdesc='Ceph Storage CLI utility [VIRTUAL]'
  depends=("ceph-base=${__version}")
}

package_ceph() {
  pkgdesc='Ceph Storage full install [VIRTUAL]'
  depends=(
    "ceph-libs=${__version}"
    "ceph-cluster=${__version}"
    "ceph-rados=${__version}"
    "ceph-rbd=${__version}"
    "ceph-cephfs=${__version}"
    "ceph-tools=${__version}"
    "ceph-test=${__version}"
    "python-rados=${__version}"
    "python-rbd=${__version}"
    "python-cephfs=${__version}"
    "python-rgw=${__version}"
  )
}

#======================================================================================#
#======================================================================================#

_prepare_ceph_python_bcrypt() {
  (
    cd "${srcdir}/bcrypt-${__bcrypt_version}"

    # apply patches from the source array
    local filename
    for filename in "${source[@]%%::*}"; do
      if [[ "${filename}" =~ \.patch$ ]] \
      && [[ "${filename}" =~ ^python-bcrypt-.* ]]; then
        echo "Applying patch ${filename##*/}"
        patch -p1 -N -i "${srcdir}/${filename##*/}"
      fi
    done

    mv -v src/{bcrypt,ceph_bcrypt}
  )
}

_build_ceph_python_bcrypt() {
  (
    cd "${srcdir}/bcrypt-${__bcrypt_version}"

    python -m build --wheel --no-isolation
  )
}

_check_ceph_python_bcrypt() {
  (
    cd "${srcdir}/bcrypt-${__bcrypt_version}"

    local _site_packages=$(python -c "import site; print(site.getsitepackages()[0])")

    python -m installer --destdir=test_dir dist/*.whl
    PYTHONPATH="test_dir/$_site_packages:$PYTHONPATH" pytest
  )
}

_package_ceph_python_bcrypt() {
  (
    cd "${srcdir}/bcrypt-${__bcrypt_version}"

    python -m installer --destdir="${pkgdir}" dist/*.whl
  )
}
#======================================================================================#
#======================================================================================#

# vim:set ts=2 sw=2 et:
