// SPDX-License-Identifier: 0BSD

#include <stdio.h>
#include <string.h>

#include "saxonc/SaxonCGlue.h"
#include "saxonc/SaxonCProcessor.h"
#include "saxonc/saxonc_version.h"

#ifndef EXPECTED_SAXONC_VERSION
#error "EXPECTED_SAXONC_VERSION must be defined"
#endif
#ifndef EXPECTED_SAXONC_VERSION_MAJOR
#error "EXPECTED_SAXONC_VERSION_MAJOR must be defined"
#endif
#ifndef EXPECTED_SAXONC_VERSION_MINOR
#error "EXPECTED_SAXONC_VERSION_MINOR must be defined"
#endif
#ifndef EXPECTED_SAXONC_VERSION_PATCH
#error "EXPECTED_SAXONC_VERSION_PATCH must be defined"
#endif
#ifndef EXPECTED_SAXONC_VERSION_TWEAK
#error "EXPECTED_SAXONC_VERSION_TWEAK must be defined"
#endif

int main(void) {
	sxnc_environment *environment = NULL;
	sxnc_processor *processor = NULL;
	sxnc_parameter *parameters = NULL;
	sxnc_property *properties = NULL;

	if (strcmp(get_saxonc_version(), EXPECTED_SAXONC_VERSION) != 0 ||
	    get_saxonc_version_major() != EXPECTED_SAXONC_VERSION_MAJOR ||
	    get_saxonc_version_minor() != EXPECTED_SAXONC_VERSION_MINOR ||
	    get_saxonc_version_patch() != EXPECTED_SAXONC_VERSION_PATCH ||
	    get_saxonc_version_tweak() != EXPECTED_SAXONC_VERSION_TWEAK) {
		return 1;
	}

	initSaxonc(&environment, &processor, &parameters, &properties, 1, 1);
	if (environment == NULL || processor == NULL || parameters == NULL || properties == NULL) {
		return 2;
	}
	if (create_graalvm_isolate(environment) != 0) {
		return 3;
	}
	if (!c_createSaxonProcessor(environment, processor, 0)) {
		graal_tear_down(environment->thread);
		freeSaxonc(&environment, &processor, &parameters, &properties);
		return 4;
	}
	if (strstr(version(environment, processor), "SaxonJ-HE") == NULL) {
		graal_tear_down(environment->thread);
		freeSaxonc(&environment, &processor, &parameters, &properties);
		return 5;
	}

	graal_tear_down(environment->thread);
	freeSaxonc(&environment, &processor, &parameters, &properties);
	return 0;
}
