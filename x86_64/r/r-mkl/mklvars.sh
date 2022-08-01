#!/bin/sh
#===============================================================================
# Copyright 2003-2019 Intel Corporation.
#
# This software and the related documents are Intel copyrighted  materials,  and
# your use of  them is  governed by the  express license  under which  they were
# provided to you (License).  Unless the License provides otherwise, you may not
# use, modify, copy, publish, distribute,  disclose or transmit this software or
# the related documents without Intel's prior written permission.
#
# This software and the related documents  are provided as  is,  with no express
# or implied  warranties,  other  than those  that are  expressly stated  in the
# License.
#===============================================================================

mkl_help() {
    echo ""
    echo "Syntax:"
    echo "  source $__mkl_tmp_SCRIPT_NAME <arch> [MKL_interface] [${__mkl_tmp_MOD_NAME}]"
    echo ""
    echo "   <arch> must be one of the following"
    echo "       ia32         : Setup for IA-32 architecture"
    echo "       intel64      : Setup for Intel(R) 64 architecture"
    echo ""
    echo "   ${__mkl_tmp_MOD_NAME} (optional) - set path to Intel(R) MKL F95 modules"
    echo ""
    echo "   MKL_interface (optional) - Intel(R) MKL programming interface for intel64"
    echo "                              Not applicable without ${__mkl_tmp_MOD_NAME}"
    echo "       lp64         : 4 bytes integer (default)"
    echo "       ilp64        : 8 bytes integer"
    echo ""
    echo "If the arguments to the sourced script are ignored (consult docs for"
    echo "your shell) the alternative way to specify target is environment"
    echo "variables COMPILERVARS_ARCHITECTURE or MKLVARS_ARCHITECTURE to pass"
    echo "<arch> to the script, MKLVARS_INTERFACE to pass <MKL_interface> and"
    echo "MKLVARS_MOD to pass <${__mkl_tmp_MOD_NAME}>"
    echo ""
}

get_tbb_library_directory() {
    __tbb_tmp_lib_dir="gcc4.1"
    which gcc >/dev/null 2>&1
    if [ $? -eq 0 ]; then
        __tbb_tmp_gcc_version_full=$(gcc --version | grep "gcc" | egrep -o " [0-9]+\.[0-9]+\.[0-9]+.*" | sed -e "s/^\ //")
        if [ $? -eq 0 ]; then
            __tbb_tmp_gcc_version=$(echo "${__tbb_tmp_gcc_version_full}" | egrep -o "^[0-9]+\.[0-9]+\.[0-9]+")
        fi
        if [ -d "${TBBROOT}/lib/${__mkl_tmp_TARGET_ARCH}/gcc4.8" ]; then
            __tbb_tmp_lib_dir="gcc4.8"
        else
            case "${__tbb_tmp_gcc_version}" in
                4.[7-9]*|[5-9]* )
                    __tbb_tmp_lib_dir="gcc4.7";;
                4.[4-6]* )
                    __tbb_tmp_lib_dir="gcc4.4";;
                * )
                    __tbb_tmp_lib_dir="gcc4.1";;
            esac
        fi
    fi
    echo ${__tbb_tmp_lib_dir}
}

set_ld_library_path() {
    __tmp_target_arch_path=$1
    __tmp_ld_library_path="${__compiler_dir}/${__tmp_target_arch_path}:${__mkl_lib_dir}/${__tmp_target_arch_path}"

    __tmp_tbb_arch_path=$2
    __tmp_ld_library_path=${__tmp_tbb_arch_path:+"${__tmp_tbb_arch_path}:"}${__tmp_ld_library_path}

    echo "${__tmp_ld_library_path}"
}

set_library_path() {
    __tmp_target_arch_path=$1
    __tmp_tbb_arch_path=$2

    if [ "${__tmp_target_arch_path}" = "${__subdir_arch_ia32}" ]; then
        __tmp_library_path="${__compiler_dir}/${__tmp_target_arch_path}:${__mkl_lib_dir}/${__tmp_target_arch_path}"
        __tmp_library_path=${__tmp_tbb_arch_path:+"${__tmp_tbb_arch_path}:"}${__tmp_library_path}
    else
        __tmp_library_path="${__compiler_dir}/${__subdir_arch_intel64}:${__mkl_lib_dir}/${__subdir_arch_intel64}"
        __tmp_library_path=${__tmp_tbb_arch_path:+"${__tmp_tbb_arch_path}:"}${__tmp_library_path}
    fi

    echo "${__tmp_library_path}"
}

set_nls_path() {
    __tmp_target_arch_path=$1
    echo "${__mkl_lib_dir}/${__tmp_target_arch_path}/locale/%l_%t/%N"
}

set_c_path() {
    __tmp_target_arch_path=$1
    __tmp_target_comp_model=$2
    echo "${CPRO_PATH}/mkl/include/${__tmp_target_arch_path}/${__tmp_target_comp_model}"
}

set_tbb_path() {
    __tmp_target_arch_path=$1

    __tmp_tbb_subdir="/$(get_tbb_library_directory)"

    __tmp_tbb_path=${__tbb_lib_dir}/${__tmp_target_arch_path}${__tmp_tbb_subdir}
    echo ${__tmp_tbb_path}
}

set_mkl_env() {
    CPRO_PATH=/opt/intel/compilers_and_libraries_2020.0.166/linux
    export MKLROOT=${CPRO_PATH}/mkl

    __mkl_tmp_SCRIPT_NAME="mklvars.sh"
    __mkl_tmp_MOD_NAME=mod

    __mkl_tmp_LP64_ILP64=
    __mkl_tmp_MOD=
    __mkl_tmp_TARGET_ARCH=
    __mkl_tmp_MKLVARS_VERBOSE=
    __mkl_tmp_BAD_SWITCH=

    if [ -z "$1" ] ; then
        if [ -n "$MKLVARS_ARCHITECTURE" ] ; then
            __mkl_tmp_TARGET_ARCH="$MKLVARS_ARCHITECTURE"
        elif [ -n "$COMPILERVARS_ARCHITECTURE" ] ; then
            __mkl_tmp_TARGET_ARCH="$COMPILERVARS_ARCHITECTURE"
        fi
        if [ "${__mkl_tmp_TARGET_ARCH}" != "ia32" -a "${__mkl_tmp_TARGET_ARCH}" != "intel64" ] ; then
            __mkl_tmp_TARGET_ARCH=
        fi
        if [ -n "$MKLVARS_INTERFACE" ] ; then
            __mkl_tmp_LP64_ILP64="$MKLVARS_INTERFACE"
            if [ "${__mkl_tmp_LP64_ILP64}" != "lp64" -a "${__mkl_tmp_LP64_ILP64}" != "ilp64" ] ; then
                __mkl_tmp_LP64_ILP64=
            fi
        fi
        if [ -n "$MKLVARS_MOD" ] ; then
            __mkl_tmp_MOD="$MKLVARS_MOD"
        fi
        if [ -n "$MKLVARS_VERBOSE" ] ; then
            __mkl_tmp_MKLVARS_VERBOSE="$MKLVARS_VERBOSE"
        fi
    else
        while [ -n "$1" ]; do
           if   [ "$1" = "ia32" ]        ; then __mkl_tmp_TARGET_ARCH=ia32;
           elif [ "$1" = "intel64" ]     ; then __mkl_tmp_TARGET_ARCH=intel64;
           elif [ "$1" = "lp64" ]        ; then __mkl_tmp_LP64_ILP64=lp64;
           elif [ "$1" = "ilp64" ]       ; then __mkl_tmp_LP64_ILP64=ilp64;
           elif [ "$1" = "${__mkl_tmp_MOD_NAME}" ] ; then __mkl_tmp_MOD=${__mkl_tmp_MOD_NAME};
           elif [ "$1" = "verbose" ]     ; then __mkl_tmp_MKLVARS_VERBOSE=verbose;
           else
               __mkl_tmp_BAD_SWITCH=$1
               break 10
           fi
           shift;
        done
    fi

    if [ -n "${__mkl_tmp_BAD_SWITCH}" ] ; then

        echo
        echo "ERROR: Unknown option '${__mkl_tmp_BAD_SWITCH}'"
        mkl_help

    else

        if [ -z "${__mkl_tmp_TARGET_ARCH}" ] ; then

            echo
            echo "ERROR: architecture is not defined. Accepted values: ia32, intel64"
            mkl_help

        else
            __compiler_dir="${CPRO_PATH}/compiler/lib"
            __mkl_lib_dir="${MKLROOT}/lib"
            __tbb_lib_dir="${CPRO_PATH}/tbb/lib"
            __cpath="${MKLROOT}/include"

            __subdir_arch_ia32="ia32_lin"
            __subdir_arch_intel64="intel64_lin"

            if   [ "${__mkl_tmp_TARGET_ARCH}" = "ia32" ];     then __target_arch_path="${__subdir_arch_ia32}";
            elif [ "${__mkl_tmp_TARGET_ARCH}" = "intel64" ];  then __target_arch_path="${__subdir_arch_intel64}";
            fi

            __tbb_path_arch=""
            if [ -z "${TBBROOT}" ]; then
                if [ -d "${__tbb_lib_dir}" ]; then
                    if [ "${__target_arch_path}" = "${__subdir_arch_ia32}" ]; then
                        __tbb_path_arch=$(set_tbb_path ${__subdir_arch_ia32} )
                    else
                        __tbb_path_arch=$(set_tbb_path ${__subdir_arch_intel64} )
                    fi
                fi
            fi

            __ld_library_path=$(set_ld_library_path ${__target_arch_path} ${__tbb_path_arch})
            __library_path=$(set_library_path ${__target_arch_path} ${__tbb_path_arch})
            __nlspath=$(set_nls_path ${__target_arch_path})

            if [ "${__mkl_tmp_MOD}" = "${__mkl_tmp_MOD_NAME}" ] ; then
                if [ "${__mkl_tmp_TARGET_ARCH}" = "ia32" ] ; then
                    __mkl_tmp_LP64_ILP64=
                else
                    if [ -z "$__mkl_tmp_LP64_ILP64" ] ; then
                        __mkl_tmp_LP64_ILP64=lp64
                    fi
                fi
                __cpath=$(set_c_path ${__target_arch_path} ${__mkl_tmp_LP64_ILP64}):${__cpath}
            fi

            export LD_LIBRARY_PATH="${__ld_library_path}${LD_LIBRARY_PATH+:${LD_LIBRARY_PATH}}"
            export LIBRARY_PATH="${__library_path}${LIBRARY_PATH+:${LIBRARY_PATH}}"
            export NLSPATH="${__nlspath}${NLSPATH+:${NLSPATH}}"
            export CPATH="${__cpath}${CPATH+:${CPATH}}"
            export PKG_CONFIG_PATH="${MKLROOT}/bin/pkgconfig${PKG_CONFIG_PATH+:${PKG_CONFIG_PATH}}"

            if [ "${__mkl_tmp_MKLVARS_VERBOSE}" = "verbose" ] ; then
                echo LD_LIBRARY_PATH=${LD_LIBRARY_PATH}
                echo LIBRARY_PATH=${LIBRARY_PATH}
                echo NLSPATH=${NLSPATH}
                echo CPATH=${CPATH}
                echo PKG_CONFIG_PATH=${PKG_CONFIG_PATH}
            fi
        fi
    fi
}

set_mkl_env "$@"
