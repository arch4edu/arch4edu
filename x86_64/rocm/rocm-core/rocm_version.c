#include "rocm-core/rocm_version.h"

VerErrors getROCmVersion(unsigned int *Major, unsigned int *Minor,
                         unsigned int *Patch) {
  *Major = ROCM_VERSION_MAJOR;
  *Minor = ROCM_VERSION_MINOR;
  *Patch = ROCM_VERSION_PATCH;

  return 0;
}
