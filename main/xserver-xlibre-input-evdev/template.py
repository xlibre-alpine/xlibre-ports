pkgname = "xserver-xlibre-input-evdev"
pkgver = "2.11.0.2"
pkgrel = 1
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
    "xorg-util-macros",
]
makedepends = [
    "libevdev-devel",
    "mtdev-devel",
    "udev-devel",
    "xserver-xlibre-devel",
]
depends = [
    "virtual:xserver-abi-input~24!xserver-xlibre-core",
    "xserver-xlibre-core",
]
provides = ["xserver-xlibre-input-driver", "xserver-xorg-input-evdev"]
provider_priority = 100
replaces = ["xserver-xorg-input-evdev"]
replaces_priority = 100
pkgdesc = "Generic input driver for XLibre server based on evdev"
license = "MIT"
url = "https://github.com/X11Libre/xf86-input-evdev"
source = f"https://github.com/X11Libre/xf86-input-evdev/archive/refs/tags/xlibre-xf86-input-evdev-{pkgver}.tar.gz"
sha256 = "70a8a65ec56cce7057b8491f68744c6883debe8750948bb290ae7b1c3ec28dfc"


def post_install(self):
    self.install_license("COPYING")


@subpackage("xserver-xlibre-input-evdev-devel")
def _(self):
    self.provider_priority = 100
    self.provides = ["xserver-xorg-input-evdev-devel"]
    self.replaces = ["xserver-xorg-input-evdev-devel"]
    return self.default_devel()
