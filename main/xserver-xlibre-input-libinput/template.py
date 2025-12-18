pkgname = "xserver-xlibre-input-libinput"
pkgver = "25.0.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
    "xorg-util-macros",
]
makedepends = ["xserver-xlibre-devel", "libinput-devel"]
depends = [
    "virtual:xserver-abi-input~24!xserver-xlibre-core",
    "xserver-xlibre-core",
]
provides = ["xserver-xlibre-input-driver", "xserver-xorg-input-libinput"]
provider_priority = 100
replaces = ["xserver-xorg-input-libinput"]
replaces_priority = 100
pkgdesc = "Generic input driver for XLibre server based on libinput"
license = "MIT"
url = "https://github.com/X11Libre/xf86-input-libinput"
source = f"https://github.com/X11Libre/xf86-input-libinput/archive/refs/tags/xlibre-xf86-input-libinput-{pkgver}.tar.gz"
sha256 = "aa7369a0a3834876ba11659cc663105a1511651d7ac2be2338e5d195283fbd00"


def post_install(self):
    self.install_license("COPYING")


@subpackage("xserver-xlibre-input-libinput-devel")
def _(self):
    self.provider_priority = 100
    self.provides = ["xserver-xorg-input-libinput-devel"]
    self.replaces = ["xserver-xorg-input-libinput-devel"]
    return self.default_devel()
