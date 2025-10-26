# XLibre Ports for Alpine Linux

This repository contains Alpine Linux APKBUILD files for [XLibre](https://github.com/X11Libre) - a modern fork of the X.Org X Window System.

## What is XLibre?

XLibre is a community-driven fork of X.Org that aims to modernize and maintain the X Window System while keeping it backwards compatible with the original X.Org. This repository provides Alpine Linux packages for the XLibre X server and its associated drivers.

## Repository Structure

```
xlibre-ports/
├── pkgs/
│   ├── xlibre/                    # XLibre X server (core package)
│   ├── xlibre-input-*/            # Input drivers (evdev, libinput, synaptics, etc.)
│   └── xlibre-video-*/            # Video drivers (intel, amd, nouveau, etc.)
└── README.md
```

## Packages Included

### Core Server
- **xlibre-xserver** - XLibre X server with subpackages (Xvfb, Xephyr, Xnest)

### Input Drivers
- xlibre-input-evdev - Generic event device input driver
- xlibre-input-libinput - Modern libinput-based input driver
- xlibre-input-synaptics - Synaptics touchpad driver
- xlibre-input-vmmouse - VMware mouse driver
- xlibre-input-wacom - Wacom tablet driver

### Video Drivers
- xlibre-video-amdgpu - AMD Radeon Rx/HDxxxx driver
- xlibre-video-ati - AMD/ATI Radeon driver
- xlibre-video-intel - Intel integrated graphics driver
- xlibre-video-nouveau - Open-source NVIDIA driver
- xlibre-video-nv - Legacy NVIDIA driver
- xlibre-video-qxl - QEMU/KVM QXL driver (with Xspice support)
- xlibre-video-vmware - VMware SVGA driver
- xlibre-video-fbdev - Framebuffer device driver
- xlibre-video-vesa - Generic VESA driver
- xlibre-video-dummy - Dummy/headless driver
- And many more legacy drivers (ark, apm, ast, chips, i128, i740, omap, r128, rendition, s3virge, savage, siliconmotion, sis, tdfx)

## Building Packages

### Prerequisites

1. Alpine Linux build environment
2. `abuild` tools installed
3. Developer signing keys set up

```bash
# Install abuild tools
sudo apk add alpine-sdk

# Set up signing keys (if not already done)
abuild-keygen -a -i
```

### Building Individual Packages

Navigate to any package directory and build:

```bash
cd pkgs/xlibre-input-evdev
abuild -r
```

### Building All Packages

To build all packages in order (respecting dependencies):

```bash
# Build the core server first
cd pkgs/xlibre
abuild -r

# Build input drivers
for pkg in pkgs/xlibre-input-*/; do
    cd "$pkg"
    abuild -r
    cd ../..
done

# Build video drivers
for pkg in pkgs/xlibre-video-*/; do
    cd "$pkg"
    abuild -r
    cd ../..
done
```

### Installing Built Packages

After building, packages will be in `~/packages/<arch>/`:

```bash
# Install the XLibre server
sudo apk add ~/packages/$(uname -m)/xlibre-xserver-*.apk

# Install desired drivers
sudo apk add ~/packages/$(uname -m)/xlibre-input-libinput-*.apk
sudo apk add ~/packages/$(uname -m)/xlibre-video-intel-*.apk
```

## Key Features

- **Drop-in Replacement**: XLibre packages provide and replace standard X.Org packages
- **Version 25.0**: Based on XLibre 25.0.x series
- **Versioned Module Paths**: Drivers install to `/usr/lib/xorg/modules/xlibre-25.0/`
- **Alpine Integration**: Full integration with Alpine's package management

## Build Notes

### Common Build Requirements

Most packages require:
- `xlibre-xserver-dev` - Development headers
- `xorgproto` - X.Org protocol headers
- `util-macros` - X.Org build macros
- `autoconf`, `automake`, `libtool` - Build tools (for GitHub source packages)

### Autotools-based Packages

Packages built from GitHub sources use `autoreconf -vif` in the prepare step to generate configure scripts.

### Meson-based Packages

Some modern packages (libinput, wacom, xlibre-xserver) use Meson build system.

## Architecture Support

- **all**: Most drivers support all architectures
- **x86/x86_64**: Legacy/vintage hardware drivers (ark, apm, i740, etc.)
- **x86_64**: Modern Intel/AMD drivers
- **armv7**: ARM-specific drivers (omap)
- **arm64**: Selected ARM64 drivers for VMWare Fusion on Apple Silicon (vmmouse, vmware)

## License

Individual packages maintain their original licenses pulled from the original [Alpine Linux aports repository](https://gitlab.alpinelinux.org/alpine/aports) (mostly MIT). See each APKBUILD for specific license information.

## Contributing

When adding new packages:
1. Use the existing APKBUILD templates as reference
2. Ensure `builddir` matches GitHub archive extraction path
3. Add `autoconf automake libtool` to makedepends for autotools projects
4. Set correct architecture restrictions
5. Add `provides` and `replaces` for X.Org compatibility

## TODO

- [ ] Build and package Xlibre once a new version is released via GitHub Actions
- [ ] Add support for Chimera Linux

## Related Links

- [X11Libre Organization](https://github.com/X11Libre)
- [Alpine Linux](https://alpinelinux.org/)
- [abuild Documentation](https://wiki.alpinelinux.org/wiki/Abuild)





