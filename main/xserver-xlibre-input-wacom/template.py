pkgname = "xserver-xlibre-input-wacom"
pkgver = "1.2.3.2"
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
depends = ["virtual:xserver-abi-input~24!xserver-xlibre-core"]
pkgdesc = "XLibre Wacom tablet input driver"
license = "GPL-2.0-or-later"
url = "https://github.com/X11Libre/xf86-input-wacom"
source = f"https://github.com/X11Libre/xf86-input-wacom/archive/refs/tags/xlibre-xf86-input-wacom-{pkgver}.tar.gz"
sha256 = "8c1942cbf90ee80d6505d115bab27461680c623d7acddf6be931224ea8176c36"


def post_install(self):
    self.uninstall("usr/lib/systemd/system")


@subpackage("xserver-xlibre-input-wacom-devel")
def _(self):
    self.provides = ["xserver-xorg-input-wacom-devel"]
    self.replaces = ["xserver-xorg-input-wacom-devel"]
    return self.default_devel()
