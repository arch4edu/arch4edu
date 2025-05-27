# Arch-Linux - AUR Package python-torchvision-rocm

Either build from source,

or add https://github.com/arch4edu/arch4edu to your package sources

- they have (upon other packages) a prebuild python-torchvision-rocm binary build from this source available.
- This **usually** works for manjaro too but will most likely **break** after every major update to the pytorch underlying libraries until updated in manjaro
- please refrain from creating issues related to this, thank you!

### Issue Template

Please paste the output of

```sh
/opt/rocm/bin/rocminfo | grep -E "(Name|ID):"
export | grep -E "(GPU_TARGETS|AMDGPU_TARGETS|\
PYTORCH_ROCM_ARCH|HSA_OVERRIDE_GFX_VERSION|ROCR_VISIBLE_DEVICES)"
python -c 'import torch.version as v; \
  print("torch: {}\nrocm: {}\n".format(v.git_version, v.hip))'
```

in the issue, alongside the commandline used to build this package.

### Supported GPU-Architectures, python-pytorch and ROCM stack

This packages uses the gpu-architectures list from the corresponding python-pytorch package which in turn relies on the ROCM Version it is build with. See https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.0.0/reference/system-requirements.html for the current supported GPU-Architectures.

At the moment, users with a gfx1103 should set `export HSA_OVERRIDE_GFX_VERSION=11.0.0` before building the package.

To build only for a specific architecture, `export PYTORCH_ROCM_ARCH=gfx01234` before starting the build. GPU_TARGETS, AMDGPU_TARGETS will be used in addition to PYTORCH_ROCM_ARCH, the later overriding the ealier if more than one is set.

Please don't open issues for unsupported GPU-Architectures.
