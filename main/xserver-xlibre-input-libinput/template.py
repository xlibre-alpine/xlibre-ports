pkgname = "xserver-xlibre-input-libinput"
pkgver = "25.0.1"
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
sha256 = "d7d9246b6f9a03459a5b603b726aa4e4c0ec8ea669fff2f38976bc81eec96a44"


def post_install(self):
    self.install_license("COPYING")


@subpackage("xserver-xlibre-input-libinput-devel")
def _(self):
    self.provider_priority = 100
    self.provides = ["xserver-xorg-input-libinput-devel"]
    self.replaces = ["xserver-xorg-input-libinput-devel"]
    return self.default_devel()
