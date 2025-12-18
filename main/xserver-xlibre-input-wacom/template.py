pkgname = "xserver-xlibre-input-wacom"
pkgver = "25.0.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "libtool",
    "pkgconf",
    "xorg-util-macros",
]
makedepends = [
    "libx11-devel",
    "libxext-devel",
    "libxi-devel",
    "libxinerama-devel",
    "libxrandr-devel",
    "linux-headers",
    "udev-devel",
    "xserver-xlibre-devel",
]
depends = [
    "virtual:xserver-abi-input~24!xserver-xlibre-core",
    "xserver-xlibre-core",
]
provides = ["xserver-xlibre-input-driver", "xserver-xorg-input-wacom"]
provider_priority = 100
replaces = ["xserver-xorg-input-wacom"]
replaces_priority = 100
pkgdesc = "XLibre Wacom tablet input driver"
license = "GPL-2.0-or-later"
url = "https://github.com/X11Libre/xf86-input-wacom"
source = f"https://github.com/X11Libre/xf86-input-wacom/archive/refs/tags/xlibre-xf86-input-wacom-{pkgver}.tar.gz"
sha256 = "12878547b271f4e59ecd5098f935d4c0bd4560d0c2a3a667385d916bc63d00af"


def post_install(self):
    self.uninstall("usr/lib/systemd/system")


@subpackage("xserver-xlibre-input-wacom-devel")
def _(self):
    self.replaces = ["xserver-xorg-input-wacom-devel"]
    self.provides = ["xserver-xorg-input-wacom-devel"]
    self.provider_priority = 100
    self.replaces_priority = 100
    return self.default_devel()
