# Use the official Arch Linux base image
# FROM --platform=linux/arm64 archlinux/archlinux:latest for new Macs
FROM archlinux/archlinux:latest

# Update the system and install git (needed for some AUR helpers)
RUN pacman -Syu --noconfirm && \
    pacman -S --noconfirm git sudo base-devel

# Create a non-root user for building packages
RUN useradd -m -G wheel builder && \
    echo "builder ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Switch to the builder user
USER builder
WORKDIR /home/builder

# Install yay (AUR helper)
RUN git clone https://aur.archlinux.org/yay.git && \
    cd yay && \
    makepkg -si --noconfirm && \
    cd .. && \
    rm -rf yay

# Copy the PKGBUILD files
COPY --chown=builder:builder .SRCINFO PKGBUILD ./

# Install build dependencies
RUN yay -S --noconfirm \
    python \
    python-hatch-vcs \
    python-build \
    python-installer \
    python-wheel \
    python-libmambapy \
    python-boltons

# Build the package
RUN makepkg -si --noconfirm

# Test that the package was installed correctly
RUN python -c "import conda_libmamba_solver; print('Package successfully installed!')"
