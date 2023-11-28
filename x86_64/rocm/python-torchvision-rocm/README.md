# Arch-Linux - AUR Package python-torchvision-rocm

Either build from source, or add

https://github.com/arch4edu/arch4edu

to your package sources, they have (upon other packages)

a prebuild python-torchvision-rocm binary build from this source available.

- This **usually** works for manjaro too
    - but will most likely **break** after every major update to the pytorch underlying libraries until updated in manjaro
    - please refrain from creating issues related to this, thank you!

### Issue Template

Please paste the output of
```sh
/opt/rocm/bin/rocminfo | grep -E "(Name|ID):"
export | grep -E "(GPU_TARGETS|AMDGPU_TARGETS|PYTORCH_ROCM_ARCH|HSA_OVERRIDE_GFX_VERSION)"
```

in your issue, alongside the commandline used to build this package

### Currently supported GPU-Architectures

See https://rocm.docs.amd.com/en/latest/release/gpu_os_support.html for currently supported GPU-Architectures.

Currently (as of ROCM 5.7.1) users with a gfx1103 should set

`export HSA_OVERRIDE_GFX_VERSION=11.0.0`

before building the package.

### Runing pytorch/torchvision on an old/custom build ROCM stack

Since Jan 2023, the whole ROCM stack is now in archlinux and its derivates (eg. manjaro).

If running into trouble with newer pytorch versions,
uninstall **all** ROCM related custom build packages
and reinstall python-pytorch-rocm to get the integrated packages from your distro.
