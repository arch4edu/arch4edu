# Maintainer: @RubenKelevra <rubenkelevra@gmail.com>

pkgname='libsaxonc'
pkgver='12.9.0'
pkgrel=2
pkgdesc='SaxonC-HE XSLT, XQuery and XPath processor library for C/C++'
url='https://github.com/Saxonica/Saxon-HE'
license=('MPL-2.0 AND Apache-2.0 AND BSD-3-Clause AND X11 AND W3C-20150513 AND 0BSD AND (GPL-2.0-only WITH Classpath-exception-2.0)')
arch=(
	'x86_64'
	'aarch64'
)
depends=(
	'gcc-libs'
	'glibc'
	'zlib'
)
makedepends=(
	'jdk21-graalvm-bin'
	'patchelf'
)
checkdepends=('cmake')
_soversion="${pkgver%%.*}"
_version_tail="${pkgver#*.}"
_version_major="${pkgver%%.*}"
_version_minor="${_version_tail%%.*}"
_version_patch="${pkgver##*.}"
_version_tweak='0'
_pkgver_dashed="${pkgver//./-}"
_releasever="${pkgver%.*}"
_releasever_dashed="${_releasever//./-}"
_xmlresolverver='5.3.3'
_jlinever='2.14.6'
source=(
	"SaxonCHE-source-${pkgver}.zip::${url}/releases/download/SaxonHE${_releasever_dashed}/SaxonCHE-source-${_pkgver_dashed}.zip"
	"saxon${_releasever_dashed}source.zip::${url}/releases/download/SaxonHE${_releasever_dashed}/saxon${_releasever_dashed}source.zip"
	"xmlresolver-${_xmlresolverver}.jar::https://repo.maven.apache.org/maven2/org/xmlresolver/xmlresolver/${_xmlresolverver}/xmlresolver-${_xmlresolverver}.jar"
	"xmlresolver-${_xmlresolverver}-data.jar::https://repo.maven.apache.org/maven2/org/xmlresolver/xmlresolver/${_xmlresolverver}/xmlresolver-${_xmlresolverver}-data.jar"
	"jline-${_jlinever}.jar::https://repo.maven.apache.org/maven2/jline/jline/${_jlinever}/jline-${_jlinever}.jar"
	'reflect-config.json'
	'resource-config.json'
	'saxonc_version.c'
	'SaxonCHEConfig.cmake.in'
	'SaxonCHEConfigVersion.cmake.in'
	'saxonc_c_verification.c'
	'saxonc_cpp_verification.cpp'
	'saxonc_cmake_verification.CMakeLists.txt.in'
	"jline-LICENSE-${_jlinever}.txt::https://raw.githubusercontent.com/jline/jline2/jline-${_jlinever}/LICENSE.txt"
	"xmlresolver-LICENSE-${_xmlresolverver}.md::https://raw.githubusercontent.com/xmlresolver/xmlresolver/${_xmlresolverver}/LICENSE.md"
	'JAMESCLARK.txt'
	'LICENSE'
)
noextract=(
	"saxon${_releasever_dashed}source.zip"
	"xmlresolver-${_xmlresolverver}.jar"
	"xmlresolver-${_xmlresolverver}-data.jar"
	"jline-${_jlinever}.jar"
)
b2sums=(
	'1e0d0fa166cbc783038fa21b2f24e64115568bdd482e6657f28c2615f6c96f5bebb1691904778e70033cab9a533a11cf80364f1ee8fb7e202d5c81d2cf408387'
	'34cb9c61c4b1ea726bdf128726efb2593e18878ea4d8f9b421488b30d0657e7a157a9b970ebffaca646e2df052e452f0e6f0da8e7e01bccffffd17e43b719264'
	'91509ea5d61ba288ac6eb60ebe5f3d83a355f838286ecfe0b4e512ff1c821a78c424fbf3354636eec8ba364d65b46c2079273498e00355f2d618206193e9cba3'
	'9e6c3f3fba4c854577c6a97e2c76eaecef0fbdbc0e40c57ba2f754f547285d030ca73ac077a68dd99c56e860119adb6638287a6fb7270348e67803399dd57a92'
	'1d4863a32fc9e926be7cbef1ce15b66a8dffb379993de081186de80f2944d9ba37472ba91a1884fe6c9c33bd6d9c020c58c79326a25e1e92884e4b6d6aa57f04'
	'443042c8826e6cfac9c44b79442186e88514fadadd70406a0a514dc09a4721b0006a1798028c1d3839ac490df98a9f51faa923eeb908100ef974d4b27774bf58'
	'56a707175b101f24d3d1274f5f0c1c98199b3f31a94aa61247c1db9ed486141560e7d259b2e9d5cdca0f5316465ad0b1e763598e78819bde98bc89a769da3675'
	'0e7a4d7959808b39989f0360c9507737b0387c05c1e44af76c07472c91e827fc20bbebc7ed9609d4629f1a3c653869ed8bbb70eacf553a995f3782680592fd02'
	'fc17c4582d43523ccb4aebcc6cb61dab4a95a5820f2ec8e01a80124700a77775e26d96c66479caa5f845571f8913e47a8150f508ae375d960c7771f9897acc44'
	'3a39887a99867bf958016e5c8c273ab0ab65935410cb05e452a2dc2dc8e8f14ac804ac0b2ba6d791135d4a79be9f73fc675ad2d9014365b2d624b04732bd64bf'
	'57fe501860a9db0c336301e5e689b93881bae7a5456e341e9bf38fd796ef4678602505896914cb7f7c90cc78e7f82e4755a5d0ff33175761e64af9337403c0a2'
	'fdd5b019582c4f63832c4bba3e3df6f4116d67e91b9961cf42e6c661e83455db415ef7ad67fec9a2ba4a8f9ce6e76b58ac14af7ce44bf79d2c0e92540282e158'
	'c6105847e639e2ab126dfb634f85a3c6829b2eff6590124b3e04b05f02e62bbb17a8cd44fd50548f853b608d00df33cd9161fe1b1be4b5f5a503261eeb1919b9'
	'a834b583b21d111202b2ab3d75ef4a31fe9a89bbab490c3e5502795c305355d120bd3dccc27b72e3c7c1c6bd1bbbbfe57ab728a12728d04613beb4424da27d68'
	'bc9ff80506c0ab0904a57a6a52547f2e51276c0c6f4cba84ccc6562165d5896743e389bde21c7688628d03d7037f3e9e03e67b051254dc62721dcb5c0e39caaa'
	'4f3df2dbe3766828196839b2329eb362ba1c88f1f2871830b8ac0469feadb13cac0ebaca3c9ce151b2d4a68b6b056871d9a6befbe11fd1863c33593da7098e8d'
	'49f39ce820b3c389734b44687bd14aa8cc5d757bd2de7b185df208a5aa2eb63961415516f792d09551828ee813d1100d9fa706b25ee4c97f930989babb3fc431'
)

_gcc_target_options() {
	local _output

	_output="$("${CC:-gcc}" "$@" -Q --help=target -x c -S /dev/null -o /dev/null 2>&1)" || return 1
	awk '$1 ~ /^-m/ && $NF == "[enabled]" { sub(/^-m/, "", $1); print $1 }' <<< "${_output}" | sort -u
}

_gcc_preprocessor_defines() {
	local _output

	_output="$("${CC:-gcc}" "$@" -dM -E -x c /dev/null 2>&1)" || return 1
	awk '$1 == "#define" { print $2 }' <<< "${_output}"
}

_native_image_march_x86_64() {
	local _graal=$1
	local _candidate
	local _current
	local _current_target
	local _description
	local _feature
	local _feature_key
	local _feature_key_dot
	local _feature_key_no_one
	local _line
	local _output
	local _parent
	local _remainder
	local _matches
	local _package_target
	local -a _cflags=()
	local -a _candidates=()
	local -a _required_features=()
	local -A _effective=()
	local -A _feature_descriptions=()
	local -A _supported=()

	_output="$("${_graal}/bin/native-image" -march=list 2>&1)" || return 1
	while IFS= read -r _line; do
		if [[ "${_line}" =~ ^\'([^\']+)\'$ ]]; then
			_current_target="${BASH_REMATCH[1]}"
			_supported["${_current_target}"]=1
		elif [[ -n "${_current_target:-}" && "${_line}" =~ ^[[:space:]]*CPU[[:space:]]features:[[:space:]](.*)$ ]]; then
			_feature_descriptions["${_current_target}"]="${BASH_REMATCH[1]}"
		fi
	done <<< "${_output}"
	[[ -n "${_supported[compatibility]:-}" ]] || {
		printf 'GraalVM does not provide the compatibility machine target\n' >&2
		return 1
	}
	if [[ -n "${PACKAGECARCH:-}" ]]; then
		if [[ "${PACKAGECARCH}" == 'x86_64' ]]; then
			_package_target='compatibility'
		elif [[ "${PACKAGECARCH}" =~ ^x86_64_v([1-9][0-9]*)$ ]]; then
			_package_target="x86-64-v${BASH_REMATCH[1]}"
		else
			printf 'Unsupported PACKAGECARCH for GraalVM Native Image: %s\n' "${PACKAGECARCH}" >&2
			return 1
		fi
		[[ -n "${_supported[${_package_target}]:-}" ]] || {
			printf 'GraalVM does not support the PACKAGECARCH-derived machine target: %s\n' "${_package_target}" >&2
			return 1
		}
		printf '%s\n' "${_package_target}"
		return 0
	fi

	read -r -a _cflags <<< "${CFLAGS:-}"
	mapfile -t _candidates < <(
		printf '%s\n' "${!_supported[@]}" \
			| grep -E '^x86-64-v([2-9]|[1-9][0-9]+)$' \
			| sort -Vr
	)

	_output="$(_gcc_target_options "${_cflags[@]}")" || return 1
	while IFS= read -r _feature; do
		[[ -n "${_feature}" ]] && _effective["${_feature}"]=1
	done <<< "${_output}"

	for _candidate in "${_candidates[@]}"; do
		_required_features=()
		_current="${_candidate}"
		while [[ "${_current}" =~ ^x86-64-v[0-9]+$ ]]; do
			_description="${_feature_descriptions[${_current}]:-}"
			[[ -n "${_description}" ]] || break
			_parent=''
			_remainder="${_description}"
			if [[ "${_description}" =~ ^all[[:space:]]of[[:space:]]\'([^\']+)\'(.*)$ ]]; then
				_parent="${BASH_REMATCH[1]}"
				_remainder="${BASH_REMATCH[2]}"
			fi
			_remainder="${_remainder# + }"
			_remainder="${_remainder// + / }"
			if [[ -n "${_remainder}" ]]; then
				read -r -a _required_features <<< "${_required_features[*]} ${_remainder}"
			fi
			[[ "${_parent}" =~ ^x86-64-v[0-9]+$ ]] || break
			_current="${_parent}"
		done

		_matches=1
		for _feature in "${_required_features[@]}"; do
			_feature_key="${_feature,,}"
			_feature_key_dot="${_feature_key//_/.}"
			_feature_key_no_one="${_feature_key%1}"
			if [[ -z "${_effective[${_feature_key}]:-}" \
				&& -z "${_effective[${_feature_key_dot}]:-}" \
				&& -z "${_effective[${_feature_key_no_one}]:-}" ]]; then
				_matches=0
				break
			fi
		done
		if (( _matches )); then
			printf '%s\n' "${_candidate}"
			return 0
		fi
	done

	printf '%s\n' 'compatibility'
}

_native_image_march_aarch64() {
	local _graal=$1
	local _base_target
	local _line
	local _macro
	local _modifier
	local _modifier_list
	local _output
	local _target
	local -a _cflags=()
	local -A _defined=()
	local -A _supported=()
	local -A _supported_modifiers=()

	_output="$("${_graal}/bin/native-image" -march=list 2>&1)" || return 1
	while IFS= read -r _line; do
		if [[ "${_line}" =~ ^\'([^\']+)\'$ ]]; then
			_supported["${BASH_REMATCH[1]}"]=1
		elif [[ "${_line}" == *'feature modifiers are available:'* ]]; then
			_modifier_list="${_line#*feature modifiers are available:}"
			while IFS= read -r _modifier; do
				[[ -n "${_modifier}" ]] && _supported_modifiers["${_modifier}"]=1
			done < <(grep -oE "'[^']+'" <<< "${_modifier_list}" | tr -d "'")
		fi
	done <<< "${_output}"
	[[ -n "${_supported[compatibility]:-}" ]] || {
		printf 'GraalVM does not provide the compatibility machine target\n' >&2
		return 1
	}

	if [[ -n "${PACKAGECARCH:-}" ]]; then
		[[ "${PACKAGECARCH}" == 'aarch64' ]] || {
			printf 'Unsupported PACKAGECARCH for GraalVM Native Image on aarch64: %s\n' "${PACKAGECARCH}" >&2
			return 1
		}
		printf '%s\n' 'compatibility'
		return 0
	fi

	read -r -a _cflags <<< "${CFLAGS:-}"
	_output="$(_gcc_preprocessor_defines "${_cflags[@]}")" || return 1
	while IFS= read -r _macro; do
		[[ -n "${_macro}" ]] && _defined["${_macro}"]=1
	done <<< "${_output}"

	[[ -n "${_defined[__ARM_FP]:-}" && -n "${_defined[__ARM_NEON]:-}" ]] || {
		printf 'Effective aarch64 CFLAGS disable FP or Advanced SIMD, which GraalVM Native Image requires\n' >&2
		return 1
	}

	if [[ -n "${_defined[__ARM_FEATURE_CRC32]:-}" \
		&& -n "${_defined[__ARM_FEATURE_ATOMICS]:-}" \
		&& -n "${_supported[armv8.1-a]:-}" ]]; then
		_base_target='armv8.1-a'
	elif [[ -n "${_supported[armv8-a]:-}" ]]; then
		_base_target='armv8-a'
	else
		_base_target='compatibility'
	fi

	_target="${_base_target}"
	if [[ -n "${_defined[__ARM_FEATURE_AES]:-}" && -n "${_supported_modifiers[aes]:-}" ]]; then
		_target+='+aes'
	fi
	if [[ "${_base_target}" != 'armv8.1-a' \
		&& -n "${_defined[__ARM_FEATURE_ATOMICS]:-}" \
		&& -n "${_supported_modifiers[lse]:-}" ]]; then
		_target+='+lse'
	fi

	printf '%s\n' "${_target}"
}

_native_image_march() {
	local _graal=$1

	case "${CARCH}" in
		x86_64)
			_native_image_march_x86_64 "${_graal}"
			;;
		aarch64)
			_native_image_march_aarch64 "${_graal}"
			;;
		*)
			printf 'Unsupported CARCH for GraalVM Native Image: %s\n' "${CARCH}" >&2
			return 1
			;;
	esac
}

prepare() {
	local _saxonj_src="${srcdir}/saxonj-source-${_releasever_dashed}"

	mkdir -p -- "${_saxonj_src}"
	bsdtar -xf "${srcdir}/saxon${_releasever_dashed}source.zip" -C "${_saxonj_src}"

	sed \
		-e "s/@PKGVER@/${pkgver}/g" \
		-e "s/@SOVERSION@/${_soversion}/g" \
		"${srcdir}/SaxonCHEConfig.cmake.in" > "${srcdir}/SaxonCHEConfig.cmake"
	sed \
		-e "s/@PKGVER@/${pkgver}/g" \
		-e "s/@SOVERSION@/${_soversion}/g" \
		"${srcdir}/SaxonCHEConfigVersion.cmake.in" > "${srcdir}/SaxonCHEConfigVersion.cmake"
	sed \
		-e "s/@PKGVER@/${pkgver}/g" \
		"${srcdir}/saxonc_cmake_verification.CMakeLists.txt.in" > "${srcdir}/saxonc_cmake_verification.CMakeLists.txt"
}

build() {
	local _src="${srcdir}/SaxonCHE-source-${_pkgver_dashed}"
	local _saxonj_src="${srcdir}/saxonj-source-${_releasever_dashed}"
	local _graal='/usr/lib/jvm/java-21-graalvm'
	local _saxonj_classes="${srcdir}/saxonj-java-classes"
	local _saxonc_classes="${srcdir}/saxonc-java-classes"
	local _native="${srcdir}/saxonc-native"
	local _objects="${srcdir}/saxonc-objects"
	local _lib="${srcdir}/saxonc-lib"
	local _resolver_jar="${srcdir}/xmlresolver-${_xmlresolverver}.jar"
	local _resolver_data_jar="${srcdir}/xmlresolver-${_xmlresolverver}-data.jar"
	local _jline_jar="${srcdir}/jline-${_jlinever}.jar"
	local _svm_jar="${_graal}/lib/svm/builder/svm.jar"
	local _module_path="${_graal}/jmods"
	local _source
	local _resource
	local _relative
	local _object
	local -a _saxonj_sources
	local -a _saxonc_sources
	local -a _c_sources
	local -a _cpp_sources
	local -a _library_objects=()
	local -a _cppflags=()
	local -a _cflags=()
	local -a _cxxflags=()
	local -a _ldflags=()
	local _native_march
	local -a _native_image_march_args=()
	local -a _version_defines=(
		"-DSAXONC_VERSION_STRING=\"${pkgver}\""
		"-DSAXONC_VERSION_MAJOR=${_version_major}"
		"-DSAXONC_VERSION_MINOR=${_version_minor}"
		"-DSAXONC_VERSION_PATCH=${_version_patch}"
		"-DSAXONC_VERSION_TWEAK=${_version_tweak}"
	)

	for _source in \
		"${_src}" \
		"${_saxonj_src}" \
		"${_resolver_jar}" \
		"${_resolver_data_jar}" \
		"${_jline_jar}" \
		"${_svm_jar}"; do
		[[ -e "${_source}" ]] || {
			printf 'Missing required build input: %s\n' "${_source}" >&2
			return 1
		}
	done
	[[ -x "${_graal}/bin/javac" ]] || {
		printf 'Missing GraalVM javac: %s\n' "${_graal}/bin/javac" >&2
		return 1
	}
	[[ -x "${_graal}/bin/native-image" ]] || {
		printf 'Missing GraalVM native-image: %s\n' "${_graal}/bin/native-image" >&2
		return 1
	}
	[[ -d "${_module_path}" ]] || {
		printf 'Missing GraalVM module path: %s\n' "${_module_path}" >&2
		return 1
	}

	_native_march="$(_native_image_march "${_graal}")" || return 1
	_native_image_march_args=("-march=${_native_march}")
	if [[ -n "${PACKAGECARCH:-}" ]]; then
		printf 'GraalVM machine target derived from PACKAGECARCH=%s: %s\n' "${PACKAGECARCH}" "${_native_march}"
	else
		printf 'GraalVM machine target derived from CFLAGS: %s\n' "${_native_march}"
	fi

	mkdir -p -- "${_saxonj_classes}" "${_saxonc_classes}" "${_native}" "${_objects}" "${_lib}"

	mapfile -d '' -t _saxonj_sources < <(
		find "${_saxonj_src}" -type f -name '*.java' \
			! -path '*/net/sf/saxon/option/axiom/*' \
			! -path '*/net/sf/saxon/option/dom4j/*' \
			! -path '*/net/sf/saxon/option/jdom2/*' \
			! -path '*/net/sf/saxon/option/xom/*' \
			-print0 | sort -z
	)
	(( ${#_saxonj_sources[@]} > 0 )) || {
		printf 'No SaxonJ Java sources found below %s\n' "${_saxonj_src}" >&2
		return 1
	}

	"${_graal}/bin/javac" \
		-cp "${_resolver_jar}:${_resolver_data_jar}:${_jline_jar}" \
		-d "${_saxonj_classes}" \
		"${_saxonj_sources[@]}"

	while IFS= read -r -d '' _resource; do
		_relative="${_resource#"${_saxonj_src}"/}"
		install -Dm644 -- "${_resource}" "${_saxonj_classes}/${_relative}"
	done < <(find "${_saxonj_src}/net/sf/saxon/data" -type f ! -name '*.java' -print0)
	install -d -- "${_saxonj_classes}/META-INF/services"
	printf '%s\n' 'net.sf.saxon.TransformerFactoryImpl' \
		> "${_saxonj_classes}/META-INF/services/javax.xml.transform.TransformerFactory"

	mapfile -d '' -t _saxonc_sources < <(find "${_src}/src/main/java" -type f -name '*.java' -print0 | sort -z)
	(( ${#_saxonc_sources[@]} > 0 )) || {
		printf 'No SaxonC Java sources found below %s\n' "${_src}/src/main/java" >&2
		return 1
	}

	"${_graal}/bin/javac" \
		--module-path "${_module_path}" \
		--add-modules org.graalvm.nativeimage \
		-cp "${_saxonj_classes}:${_resolver_jar}:${_resolver_data_jar}:${_jline_jar}:${_svm_jar}" \
		-d "${_saxonc_classes}" \
		"${_saxonc_sources[@]}"

	"${_graal}/bin/native-image" --shared --no-fallback "${_native_image_march_args[@]}" \
		--initialize-at-build-time=net.sf.saxon.option.cpp.SaxonCCurrentException \
		-H:ConfigurationFileDirectories="${srcdir}" \
		-H:NativeLinkerOption=-Wl,-z,relro \
		-H:NativeLinkerOption=-Wl,-z,now \
		-o "${_native}/libsaxonc-core-he" \
		-cp "${_saxonc_classes}:${_saxonj_classes}:${_resolver_jar}:${_resolver_data_jar}:${_jline_jar}:${_svm_jar}"

	patchelf --set-soname "libsaxonc-core-he.so.${_soversion}" "${_native}/libsaxonc-core-he.so"
	ln -sfn -- 'libsaxonc-core-he.h' "${_native}/saxonc-core-he.h"
	install -Dm755 -- "${_native}/libsaxonc-core-he.so" "${_lib}/libsaxonc-core-he.so.${pkgver}"
	ln -sfn -- "libsaxonc-core-he.so.${pkgver}" "${_lib}/libsaxonc-core-he.so.${_soversion}"
	ln -sfn -- "libsaxonc-core-he.so.${_soversion}" "${_lib}/libsaxonc-core-he.so"

	mapfile -d '' -t _c_sources < <(find "${_src}/src/main/c/lib" -maxdepth 1 -type f -name '*.c' -print0 | sort -z)
	mapfile -d '' -t _cpp_sources < <(find "${_src}/src/main/c/lib" -maxdepth 1 -type f -name '*.cpp' -print0 | sort -z)
	_c_sources+=("${srcdir}/saxonc_version.c")
	(( ${#_c_sources[@]} + ${#_cpp_sources[@]} > 0 )) || {
		printf 'No SaxonC C/C++ library sources found below %s\n' "${_src}/src/main/c/lib" >&2
		return 1
	}

	read -r -a _cppflags <<< "${CPPFLAGS:-}"
	read -r -a _cflags <<< "${CFLAGS:-}"
	read -r -a _cxxflags <<< "${CXXFLAGS:-}"
	read -r -a _ldflags <<< "${LDFLAGS:-}"

	for _source in "${_c_sources[@]}"; do
		_object="${_objects}/$(basename -- "${_source%.c}").o"
		"${CC:-gcc}" "${_cppflags[@]}" "${_cflags[@]}" "${_version_defines[@]}" \
			-fPIC -fvisibility=hidden \
			-I"${_src}/src/main/c/include" -I"${_native}" \
			-c "${_source}" -o "${_object}"
		_library_objects+=("${_object}")
	done
	for _source in "${_cpp_sources[@]}"; do
		_object="${_objects}/$(basename -- "${_source%.cpp}").o"
		"${CXX:-g++}" "${_cppflags[@]}" "${_cxxflags[@]}" \
			-fPIC -fvisibility=hidden \
			-I"${_src}/src/main/c/include" -I"${_native}" \
			-c "${_source}" -o "${_object}"
		_library_objects+=("${_object}")
	done

	"${CXX:-g++}" "${_ldflags[@]}" -shared \
		-Wl,--no-undefined \
		-Wl,-soname,"libsaxonc-he.so.${_soversion}" \
		-o "${_lib}/libsaxonc-he.so.${pkgver}" \
		"${_library_objects[@]}" \
		-L"${_lib}" -Wl,-rpath-link,"${_lib}" "-l:libsaxonc-core-he.so.${_soversion}"
	ln -sfn -- "libsaxonc-he.so.${pkgver}" "${_lib}/libsaxonc-he.so.${_soversion}"
	ln -sfn -- "libsaxonc-he.so.${_soversion}" "${_lib}/libsaxonc-he.so"
}

check() {
	local _src="${srcdir}/SaxonCHE-source-${_pkgver_dashed}"
	local _native="${srcdir}/saxonc-native"
	local _lib="${srcdir}/saxonc-lib"
	local _check="${srcdir}/saxonc-check"
	local _cmake_root="${_check}/prefix"
	local _cmake_project="${_check}/cmake-project"
	local _cmake_build="${_check}/cmake-build"
	local -a _expected_version_defines=(
		"-DEXPECTED_SAXONC_VERSION=\"${pkgver}\""
		"-DEXPECTED_SAXONC_VERSION_MAJOR=${_version_major}"
		"-DEXPECTED_SAXONC_VERSION_MINOR=${_version_minor}"
		"-DEXPECTED_SAXONC_VERSION_PATCH=${_version_patch}"
		"-DEXPECTED_SAXONC_VERSION_TWEAK=${_version_tweak}"
	)

	mkdir -p -- "${_check}"

	"${CC:-gcc}" "${_expected_version_defines[@]}" \
		-I"${_src}/src/main/c/include" -I"${_native}" \
		"${srcdir}/saxonc_c_verification.c" \
		-L"${_lib}" -Wl,-rpath,"${_lib}" -lsaxonc-he \
		-o "${_check}/saxonc-c-verification"
	LD_LIBRARY_PATH="${_lib}" "${_check}/saxonc-c-verification"

	"${CXX:-g++}" \
		-I"${_src}/src/main/c/include" -I"${_native}" \
		"${srcdir}/saxonc_cpp_verification.cpp" \
		-L"${_lib}" -Wl,-rpath,"${_lib}" -lsaxonc-he \
		-o "${_check}/saxonc-cpp-verification"
	LD_LIBRARY_PATH="${_lib}" "${_check}/saxonc-cpp-verification"

	for _source in \
		get_saxonc_version \
		get_saxonc_version_major \
		get_saxonc_version_minor \
		get_saxonc_version_patch \
		get_saxonc_version_tweak; do
		nm -D --defined-only "${_lib}/libsaxonc-he.so.${pkgver}" | awk '{print $3}' | grep -Fxq -- "${_source}" || {
			printf 'Missing public SaxonC symbol: %s\n' "${_source}" >&2
			return 1
		}
	done
	if nm -D --defined-only "${_lib}/libsaxonc-he.so.${pkgver}" | awk '{print $3}' | grep -Fxq -- 'failure'; then
		printf 'Unexpected private symbol exported: failure\n' >&2
		return 1
	fi

	install -d -- "${_cmake_root}/lib/cmake/SaxonCHE" "${_cmake_root}/include/saxonc" "${_cmake_project}"
	install -m755 -- "${_lib}/libsaxonc-core-he.so.${pkgver}" "${_cmake_root}/lib/libsaxonc-core-he.so.${pkgver}"
	ln -s -- "libsaxonc-core-he.so.${pkgver}" "${_cmake_root}/lib/libsaxonc-core-he.so.${_soversion}"
	install -m755 -- "${_lib}/libsaxonc-he.so.${pkgver}" "${_cmake_root}/lib/libsaxonc-he.so.${pkgver}"
	ln -s -- "libsaxonc-he.so.${pkgver}" "${_cmake_root}/lib/libsaxonc-he.so.${_soversion}"
	install -m644 -- "${_src}"/src/main/c/include/saxonc/*.h "${_cmake_root}/include/saxonc/"
	install -m644 -- "${_src}/src/main/c/include/saxonc_export.h" "${_cmake_root}/include/"
	install -m644 -- "${_native}/libsaxonc-core-he.h" "${_cmake_root}/include/saxonc-core-he.h"
	install -m644 -- "${_native}/graal_isolate.h" "${_cmake_root}/include/graal_isolate.h"
	install -m644 -- "${srcdir}/SaxonCHEConfig.cmake" "${srcdir}/SaxonCHEConfigVersion.cmake" \
		"${_cmake_root}/lib/cmake/SaxonCHE/"
	install -m644 -- "${srcdir}/saxonc_cpp_verification.cpp" "${_cmake_project}/"
	install -m644 -- "${srcdir}/saxonc_cmake_verification.CMakeLists.txt" "${_cmake_project}/CMakeLists.txt"

	cmake -S "${_cmake_project}" -B "${_cmake_build}" \
		-DCMAKE_PREFIX_PATH="${_cmake_root}"
	cmake --build "${_cmake_build}"
	LD_LIBRARY_PATH="${_cmake_root}/lib" "${_cmake_build}/saxonc-cmake-verification"
}

package() {
	local _src="${srcdir}/SaxonCHE-source-${_pkgver_dashed}"
	local _graal='/usr/lib/jvm/java-21-graalvm'
	local _native="${srcdir}/saxonc-native"
	local _lib="${srcdir}/saxonc-lib"
	local _license_dir="${pkgdir}/usr/share/licenses/${pkgname}"

	install -Dm755 -- "${_lib}/libsaxonc-core-he.so.${pkgver}" \
		"${pkgdir}/usr/lib/libsaxonc-core-he.so.${pkgver}"
	ln -s -- "libsaxonc-core-he.so.${pkgver}" "${pkgdir}/usr/lib/libsaxonc-core-he.so.${_soversion}"
	ln -s -- "libsaxonc-core-he.so.${_soversion}" "${pkgdir}/usr/lib/libsaxonc-core-he.so"

	install -Dm755 -- "${_lib}/libsaxonc-he.so.${pkgver}" \
		"${pkgdir}/usr/lib/libsaxonc-he.so.${pkgver}"
	ln -s -- "libsaxonc-he.so.${pkgver}" "${pkgdir}/usr/lib/libsaxonc-he.so.${_soversion}"
	ln -s -- "libsaxonc-he.so.${_soversion}" "${pkgdir}/usr/lib/libsaxonc-he.so"

	install -d -- "${pkgdir}/usr/include/saxonc"
	install -m644 -- "${_src}"/src/main/c/include/saxonc/*.h "${pkgdir}/usr/include/saxonc/"
	install -Dm644 -- "${_src}/src/main/c/include/saxonc_export.h" \
		"${pkgdir}/usr/include/saxonc_export.h"
	install -Dm644 -- "${_native}/libsaxonc-core-he.h" \
		"${pkgdir}/usr/include/saxonc-core-he.h"
	install -Dm644 -- "${_native}/graal_isolate.h" \
		"${pkgdir}/usr/include/graal_isolate.h"

	install -Dm644 -- "${srcdir}/SaxonCHEConfig.cmake" \
		"${pkgdir}/usr/lib/cmake/SaxonCHE/SaxonCHEConfig.cmake"
	install -Dm644 -- "${srcdir}/SaxonCHEConfigVersion.cmake" \
		"${pkgdir}/usr/lib/cmake/SaxonCHE/SaxonCHEConfigVersion.cmake"

	install -Dm644 -- "${_src}/notices/LICENSE.txt" "${_license_dir}/SaxonC-MPL-2.0.txt"
	install -Dm644 -- "${srcdir}/xmlresolver-LICENSE-${_xmlresolverver}.md" \
		"${_license_dir}/XMLResolver-Apache-2.0.md"
	install -Dm644 -- "${srcdir}/jline-LICENSE-${_jlinever}.txt" \
		"${_license_dir}/JLine-BSD-3-Clause.txt"
	install -Dm644 -- "${srcdir}/JAMESCLARK.txt" "${_license_dir}/X11-James-Clark.txt"
	install -Dm644 -- "${srcdir}/LICENSE" "${_license_dir}/0BSD-local.txt"
	install -Dm644 -- "${_graal}/LICENSE_NATIVEIMAGE.txt" \
		"${_license_dir}/GraalVM-Native-Image-GPL-2.0-with-Classpath-exception-2.0.txt"
	install -d -- "${_license_dir}"
	bsdtar -xOf "${srcdir}/xmlresolver-${_xmlresolverver}-data.jar" \
		org/xmlresolver/notices/w3c-license.txt > "${_license_dir}/XMLResolver-W3C.txt"
	chmod 644 "${_license_dir}/XMLResolver-W3C.txt"
}
