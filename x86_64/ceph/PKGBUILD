# Maintainer: Paul Stemmet <aur@luxolus.com>
# Contributor: Thore Bödecker <foxxx0@archlinux.org>
# Contributor: Sébastien "Seblu" Luttringer <seblu@archlinux.org>

pkgbase='ceph'
pkgdesc='Distributed, fault-tolerant storage platform delivering object, block, and file system'
pkgver=18.2.0
pkgrel=1
url='https://ceph.com/'
arch=('x86_64')
license=('GPL')
pkgname=(
  ceph-{common,compressor,crypto,erasure,tools,test,volume,cephadm}
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

  'python-bcrypt'   'python-cherrypy'      'python-coverage'   'python-dateutil'            'python-jinja'
  'python-pecan'    'python-prettytable'   'python-pyjwt'      'python-pyopenssl'           'python-requests'
  'python-scipy'    'python-setuptools'    'python-sphinx'     'python-typing_extensions'   'python-werkzeug'
  'python-yaml'
)
checkdepends=(
  'inetutils'     'xmlstarlet'

  'python-mock'   'python-nose'   'python-pycodestyle'   'python-pylint'   'python-pytest'
  'python-pytest-cov'
)

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
  'disable-empty-readable.sh-test.patch'

  # Avoid spurious failures in logrotate when duplicate rule files exist,
  # typically around cephadm auto-generated rotate rules
  'ceph-17.2.5-logrotate-ignore-dups.patch'

  # Test wants to use `git ls-files`, and is sad when it finds itself not running in a
  # git repo
  'ceph-17.2.4-tox-flake8-git-ls-files.patch'

  # A problem with mypy versions <= 0.981 causes a false postive around numpy imports.
  # See: https://github.com/python/mypy/issues/13627
  'ceph-17.2.4-tox-mypy-false-postive.patch'

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

  # Fixes node-gyp errors due to py3.11 incompatibilities
  'ceph-17.2.6-mgr-dashboard-node-version.patch'

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
)
sha512sums=('fe6a3ca4227cc05b5effc33a02670c466583ec9e4c7c025241248223992254e6e6551d7db486d5ead36bf0ba922d54e0aabc2aaf456d4593679376ec88bd971a'
            '4354001c1abd9a0c385ba7bd529e3638fb6660b6a88d4e49706d4ac21c81b8e829303a20fb5445730bdac18c4865efb10bc809c1cd56d743c12aa9a52e160049'
            '41dbc1c395cdf9b3edf5c5d91bbc90f416b4338ad964fa3471f26a4312d3ec2a5dcebbc351a1640dc4b047b4f71aa134ac7486747e5f62980092b0176e7567f5'
            'ea069b75b786c22166c609b127b512802cc5c6e9512d792d7b7b34d276f5b86d57c8c35cfc7b5c855a59c0ba87ba1aabe2ca26da72b26bff46b6ba8410ddb27e'
            '2234d005df71b3b6013e6b76ad07a5791e3af7efec5f41c78eb1a9c92a22a67f0be9560be59b52534e90bfe251bcf32c33d5d40163f3f8f7e7420691f0f4a222'
            'b12cabda7184721c494edd22250fd05019694d2bc445722d100cdefab5385bd25c2267a029d2f6053932fa6717e38c4314385afd986969ee2744d745b53c8b58'
            '31e578b240ceaaf1216b56cdce654661eed6529ef642ecad164a02669e850100a49a85dc70f3d744671e2c5dad10aee64be7d091fa33007cb8fc6788a4336799'
            'f1f549c5da829db787ee6ee3cf47912d5b48efb2533de05fd9735736e9218a78cf79c5958e1409a2c8adcca51460eb3ae7e73b5c1ec6cf73d4f07670c9934c3b'
            '5b43ba48dde8b7371d4b3976aa3a27ab3ad3a10e110479a101b8f222590bbd6aca318f3ac117f851596fc23daafb53aaa566e055dc9694ab16ab1170e8f77763'
            '781a01e622a70d56bf1948bdc0b427ffa95a86cec7dd9d26c6007a9ec024a942a8ca55f2acc3d37344862f1d6bf11cae998d8071754cd841a66bfba4ec9c58bf'
            '612faebfb5eec3651832f349ea3c23b50d2386889ff77592b0acff653049efdc5c2254f63c30d88b9a730813bf1f1945dda0d0beab0db7db3e0708ba8d057a40'
            '02ca1a9bf15f9cd6f474f264ba2bf66ae725bac990a7cac315dabe377c66935a7afd8117f18a1f82c78bdf9ab2c3e5a2a227f2ffc166974dd7bb99b290f1f233'
            'd9729c33f2b8c03ab918919e3b62cbc0825314ad09596dc12984ac5964f8b421db3376b84fa26e0952e0781deb218f8aff6ba32f9c8e5a22bd27afac8dcaf6d3'
            '79be1630ae4a599509e5d789d4aefe412ce47e67ad482f853664fa4b01e063c20593e3da668e6a776ad038fb07606ae948eea41bab20776c33c87f9ab49505e0'
            'c767a8e6fd02ea2ab88e99b50b206d0f825acdf177136ded38d93594fc7663b7c9612af7195b85e0b2b501d8ee482af5e088e9abb5ebee7b8a69e0153ce89782'
            '0c5124693bd317a73707dfd34b17664cc05233aec08e07739fe08fc9a73be7a1f4446052b1addde832cba141a382c35f45e60c89a00bb7dab81cee7ed6be07e1'
            '4613232e5a0003c08d233e40fe3ac1cd00e1195d29bdd9892188587b4a782d6979004232927c0a1bff554eabf2fb9b18eb751682b7ad90762292b63891f3b301'
            '9a1183c08f8799b14235c9271519203cbf93e48ca3a8607d3a0500910efca5379c8a08421c377227f93d8436a850f5ca99784f28aaa920e55f0457c657511f17'
            'e238b326609636bc7dd10cec59290e22898948ef105c49643c38d2621abf16c2efcf9581b0b6bad65066607510c9827d00a7abdb14f2054701cc33b7101ea054')
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

  # apply patches from the source array
  local filename
  for filename in "${source[@]%%::*}"; do
    if [[ "${filename}" =~ \.patch$ ]]; then
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

  # remove tests that require root privileges
  rm src/test/cli/ceph-authtool/cap*.t
  sed -i '/add_ceph_test(mgr-dashboard-smoke.sh/d' src/test/mgr/CMakeLists.txt

  # disable/remove broken tests
  sed -i '/add_ceph_test(smoke.sh/d' src/test/CMakeLists.txt
  sed -i '/add_ceph_test(safe-to-destroy.sh/d' src/test/osd/CMakeLists.txt
}

build() {
  cd "${srcdir}/${pkgbase}-${pkgver}"

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
    -DCMAKE_VERBOSE_MAKEFILE=ON \
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

  VERBOSE=1 make -C build legacy-option-headers
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

    'python-requests'    'python-typing_extensions'   'python-pyjwt'        'python-coverage'      'python-jinja'
    'python-pyopenssl'   'python-cherrypy'            'python-werkzeug'     'python-prettytable'   'python-pecan'
    'python-scipy'       'python-yaml'                'python-setuptools'   'python-bcrypt'        'python-dateutil'
    'python-cheroot'     'python-urllib3'             'python-jsonpatch'    'python-cryptography'

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

# vim:set ts=2 sw=2 et:
