#!/bin/sh
#shellcheck shell=sh
#===============================================================================
# Copyright 2003-2022 Intel Corporation.
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

# ############################################################################

# Get absolute path to this script.
# Uses `readlink` to remove links and `pwd -P` to turn into an absolute path.

# Usage:
#   script_dir=$(get_script_path "$script_rel_path")
#
# Inputs:
#   script/relative/pathname/scriptname
#
# Outputs:
#   /script/absolute/pathname

# executing function in a *subshell* to localize vars and effects on `cd`
get_script_path() (
  script="$1"
  while [ -L "$script" ] ; do
    # combining next two lines fails in zsh shell
    script_dir=$(command dirname -- "$script")
    script_dir=$(cd "$script_dir" && command pwd -P)
    script="$(readlink "$script")"
    case $script in
      (/*) ;;
       (*) script="$script_dir/$script" ;;
    esac
  done
  # combining next two lines fails in zsh shell
  script_dir=$(command dirname -- "$script")
  script_dir=$(cd "$script_dir" && command pwd -P)
  printf "%s" "$script_dir"
)


# ############################################################################

# Determine if we are being executed or sourced. Need to detect being sourced
# within an executed script, which can happen on a CI system. We also must
# detect being sourced at a shell prompt (CLI). The setvars.sh script will
# always source this script, but this script can also be called directly.

# We are assuming we know the name of this script, which is a reasonable
# assumption. This script _must_ be named "vars.sh" or it will not work
# with the top-level setvars.sh script. Making this assumption simplifies
# the process of detecting if the script has been sourced or executed. It
# also simplifies the process of detecting the location of this script.

# Using `readlink` to remove possible symlinks in the name of the script.
# Also, "ps -o comm=" is limited to a 15 character result, but it works
# fine here, because we are only looking for the name of this script or the
# name of the execution shell, both always fit into fifteen characters.

# Edge cases exist when executed by way of "/bin/sh setvars.sh"
# Most shells detect or fall thru to error message, sometimes ksh does not.
# This is an odd and unusual situation; not a high priority issue.

_vars_get_proc_name() {
  if [ -n "${ZSH_VERSION:-}" ] ; then
    script="$(ps -p "$$" -o comm=)"
  else
    script="$1"
    while [ -L "$script" ] ; do
      script="$(readlink "$script")"
    done
  fi
  basename -- "$script"
}

_vars_this_script_name="vars.sh"
if [ "$_vars_this_script_name" = "$(_vars_get_proc_name "$0")" ] ; then
  echo "   ERROR: Incorrect usage: this script must be sourced."
  echo "   Usage: . path/to/${_vars_this_script_name}"
  return 255 2>/dev/null || exit 255
fi


# ############################################################################

mkl_help() {
    __mkl_help=1
    echo ""
    echo "oneAPI MKL vars.sh syntax:"
    echo "  source $__mkl_tmp_SCRIPT_NAME [<arch>] [<MKL_interface>] [mod]"
    echo ""
    echo "   <arch> (optional) - oneAPI MKL architecture: "
    echo "       ia32         : Setup for IA-32 architecture"
    echo "       intel64      : Setup for Intel(R) 64 architecture (default)"
    echo ""
    echo "   <MKL_interface> (optional) - oneAPI MKL programming interface for intel64"
    echo "                                Not applicable without \"mod\""
    echo "       lp64         : 4 bytes integer (default)"
    echo "       ilp64        : 8 bytes integer"
    echo ""
    echo "   mod (optional) - set path to oneAPI MKL F95 modules"
    echo ""
    echo "If the arguments to the sourced script are ignored (consult docs for"
    echo "your shell) the alternative way to specify target is environment"
    echo "variables COMPILERVARS_ARCHITECTURE or MKLVARS_ARCHITECTURE to pass"
    echo "<arch> to the script, MKLVARS_INTERFACE to pass <MKL_interface> and"
    echo "MKLVARS_MOD to pass \"mod\""
    echo ""
}

# ############################################################################

# Extract the name and location of this sourced script.

# Generally, "ps -o comm=" is limited to a 15 character result, but it works
# fine for this usage, because we are primarily interested in finding the name
# of the execution shell, not the name of any calling script.

vars_script_name=""
vars_script_shell="$(ps -p "$$" -o comm=)"
# ${var:-} needed to pass "set -eu" checks
# see https://unix.stackexchange.com/a/381465/103967
# see https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_06_02
if [ -n "${ZSH_VERSION:-}" ] && [ -n "${ZSH_EVAL_CONTEXT:-}" ] ; then     # zsh 5.x and later
  # shellcheck disable=2249
  case $ZSH_EVAL_CONTEXT in (*:file*) vars_script_name="${(%):-%x}" ;; esac ;
elif [ -n "${KSH_VERSION:-}" ] ; then                                     # ksh, mksh or lksh
  if [ "$(set | grep -Fq "KSH_VERSION=.sh.version" ; echo $?)" -eq 0 ] ; then # ksh
    vars_script_name="${.sh.file}" ;
  else # mksh or lksh or [lm]ksh masquerading as ksh or sh
    # force [lm]ksh to issue error msg; which contains this script's path/filename, e.g.:
    # mksh: /home/ubuntu/intel/oneapi/vars.sh[137]: ${.sh.file}: bad substitution
    vars_script_name="$( (echo "${.sh.file}") 2>&1 )" || : ;
    vars_script_name="$(expr "${vars_script_name:-}" : '^.*sh: \(.*\)\[[0-9]*\]:')" ;
  fi
elif [ -n "${BASH_VERSION:-}" ] ; then        # bash
  # shellcheck disable=2128,3028
  (return 0 2>/dev/null) && vars_script_name="${BASH_SOURCE}" ;
elif [ "dash" = "$vars_script_shell" ] ; then # dash
  # force dash to issue error msg; which contains this script's rel/path/filename, e.g.:
  # dash: 146: /home/ubuntu/intel/oneapi/vars.sh: Bad substitution
  vars_script_name="$( (echo "${.sh.file}") 2>&1 )" || : ;
  vars_script_name="$(expr "${vars_script_name:-}" : '^.*dash: [0-9]*: \(.*\):')" ;
elif [ "sh" = "$vars_script_shell" ] ; then   # could be dash masquerading as /bin/sh
  # force a shell error msg; which should contain this script's path/filename
  # sample error msg shown; assume this file is named "vars.sh"; as required by setvars.sh
  vars_script_name="$( (echo "${.sh.file}") 2>&1 )" || : ;
  if [ "$(printf "%s" "$vars_script_name" | grep -Eq "sh: [0-9]+: .*vars\.sh: " ; echo $?)" -eq 0 ] ; then # dash as sh
    # sh: 155: /home/ubuntu/intel/oneapi/vars.sh: Bad substitution
    vars_script_name="$(expr "${vars_script_name:-}" : '^.*sh: [0-9]*: \(.*\):')" ;
  fi
else  # unrecognized shell or dash being sourced from within a user's script
  # force a shell error msg; which should contain this script's path/filename
  # sample error msg shown; assume this file is named "vars.sh"; as required by setvars.sh
  vars_script_name="$( (echo "${.sh.file}") 2>&1 )" || : ;
  if [ "$(printf "%s" "$vars_script_name" | grep -Eq "^.+: [0-9]+: .*vars\.sh: " ; echo $?)" -eq 0 ] ; then # dash
    # .*: 164: intel/oneapi/vars.sh: Bad substitution
    vars_script_name="$(expr "${vars_script_name:-}" : '^.*: [0-9]*: \(.*\):')" ;
  else
    vars_script_name="" ;
  fi
fi

if [ "" = "$vars_script_name" ] ; then
  >&2 echo "   ERROR: Unable to proceed: possible causes listed below."
  >&2 echo "   This script must be sourced. Did you execute or source this script?" ;
  >&2 echo "   Unrecognized/unsupported shell (supported: bash, zsh, ksh, m/lksh, dash)." ;
  >&2 echo "   May fail in dash if you rename this script (assumes \"vars.sh\")." ;
  >&2 echo "   Can be caused by sourcing from ZSH version 4.x or older." ;
  return 255 2>/dev/null || exit 255
fi


# ############################################################################

# Setup environment.

my_script_name=$(basename -- "${vars_script_name:-}")
my_script_path=$(get_script_path "${vars_script_name:-}")
MKLROOT=$(dirname -- "${my_script_path}") ; export MKLROOT

__mkl_tmp_SCRIPT_NAME="$my_script_name"
__mkl_tmp_MOD_NAME=mod
__mkl_tmp_TARGET_ARCH=intel64
__mkl_tmp_LP64_ILP64=
__mkl_tmp_MOD=
__mkl_tmp_MKLVARS_VERBOSE=
__mkl_help=

if [ -z "$1" ] ; then
    if [ -n "$MKLVARS_ARCHITECTURE" ] ; then
        __mkl_tmp_TARGET_ARCH="$MKLVARS_ARCHITECTURE"
    elif [ -n "$COMPILERVARS_ARCHITECTURE" ] ; then
        __mkl_tmp_TARGET_ARCH="$COMPILERVARS_ARCHITECTURE"
    fi
    if [ "${__mkl_tmp_TARGET_ARCH}" != "ia32" ] && [ "${__mkl_tmp_TARGET_ARCH}" != "intel64" ] ; then
        __mkl_tmp_TARGET_ARCH=intel64
    fi
    if [ -n "$MKLVARS_INTERFACE" ] ; then
        __mkl_tmp_LP64_ILP64="$MKLVARS_INTERFACE"
        if [ "${__mkl_tmp_LP64_ILP64}" != "lp64" ] && [ "${__mkl_tmp_LP64_ILP64}" != "ilp64" ] ; then
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
    while [ -n "${1:-}" ]; do
        if   [ "$1" = "ia32" ]        ; then __mkl_tmp_TARGET_ARCH=ia32;
        elif [ "$1" = "intel64" ]     ; then __mkl_tmp_TARGET_ARCH=intel64;
        elif [ "$1" = "lp64" ]        ; then __mkl_tmp_LP64_ILP64=lp64;
        elif [ "$1" = "ilp64" ]       ; then __mkl_tmp_LP64_ILP64=ilp64;
        elif [ "$1" = "${__mkl_tmp_MOD_NAME}" ] ; then __mkl_tmp_MOD=${__mkl_tmp_MOD_NAME};
        elif [ "$1" = "verbose" ]     ; then __mkl_tmp_MKLVARS_VERBOSE=verbose;
        elif [ "$1" = "help" ]        ; then mkl_help;
        fi
        shift;
    done
fi

if [ -z "${__mkl_help}" ] ; then
    __mkl_lib_dir="${MKLROOT}/lib"
    __cpath="${MKLROOT}/include"
    __mkl_bin_dir="${MKLROOT}/bin"

    __ld_library_path="${__mkl_lib_dir}/${__mkl_tmp_TARGET_ARCH}"
    __library_path="${__mkl_lib_dir}/${__mkl_tmp_TARGET_ARCH}"
    __path="${__mkl_bin_dir}/${__mkl_tmp_TARGET_ARCH}"
    __nlspath="${__mkl_lib_dir}/${__mkl_tmp_TARGET_ARCH}/locale/%l_%t/%N"

    if [ "${__mkl_tmp_MOD}" = "${__mkl_tmp_MOD_NAME}" ] ; then
        if [ "${__mkl_tmp_TARGET_ARCH}" = "ia32" ] ; then
            __mkl_tmp_LP64_ILP64=
        else
            if [ -z "$__mkl_tmp_LP64_ILP64" ] ; then
                __mkl_tmp_LP64_ILP64=lp64
            fi
        fi
        __cpath="${MKLROOT}/include/${__mkl_tmp_TARGET_ARCH}/${__mkl_tmp_LP64_ILP64}:${__cpath}"
    fi

    export LD_LIBRARY_PATH="${__ld_library_path}${LD_LIBRARY_PATH+:${LD_LIBRARY_PATH}}"
    export LIBRARY_PATH="${__library_path}${LIBRARY_PATH+:${LIBRARY_PATH}}"
    export NLSPATH="${__nlspath}${NLSPATH+:${NLSPATH}}"
    export CPATH="${__cpath}${CPATH+:${CPATH}}"
    export PATH="${__path}${PATH+:${PATH}}"
    export PKG_CONFIG_PATH="${MKLROOT}/lib/pkgconfig${PKG_CONFIG_PATH+:${PKG_CONFIG_PATH}}"

    if [ "${__mkl_tmp_MKLVARS_VERBOSE}" = "verbose" ] ; then
        echo MKLROOT=${MKLROOT}
        echo LD_LIBRARY_PATH=${LD_LIBRARY_PATH}
        echo LIBRARY_PATH=${LIBRARY_PATH}
        echo NLSPATH=${NLSPATH}
        echo CPATH=${CPATH}
        echo PKG_CONFIG_PATH=${PKG_CONFIG_PATH}
    fi
fi
