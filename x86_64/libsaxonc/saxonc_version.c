// SPDX-License-Identifier: 0BSD

#include "saxonc/saxonc_version.h"

#ifndef SAXONC_VERSION_STRING
#error "SAXONC_VERSION_STRING must be defined"
#endif
#ifndef SAXONC_VERSION_MAJOR
#error "SAXONC_VERSION_MAJOR must be defined"
#endif
#ifndef SAXONC_VERSION_MINOR
#error "SAXONC_VERSION_MINOR must be defined"
#endif
#ifndef SAXONC_VERSION_PATCH
#error "SAXONC_VERSION_PATCH must be defined"
#endif
#ifndef SAXONC_VERSION_TWEAK
#error "SAXONC_VERSION_TWEAK must be defined"
#endif

static char saxonc_version[] = SAXONC_VERSION_STRING;

char *get_saxonc_version(void) {
	return saxonc_version;
}

unsigned get_saxonc_version_major(void) {
	return SAXONC_VERSION_MAJOR;
}

unsigned get_saxonc_version_minor(void) {
	return SAXONC_VERSION_MINOR;
}

unsigned get_saxonc_version_patch(void) {
	return SAXONC_VERSION_PATCH;
}

unsigned get_saxonc_version_tweak(void) {
	return SAXONC_VERSION_TWEAK;
}
