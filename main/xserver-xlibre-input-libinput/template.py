pkgname = "xserver-xlibre-input-libinput"
pkgver = "1.5.1.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "pkgconf",
    "slibtool",
    "xorg-util-macros",
]
makedepends = ["xserver-xlibre-devel", "libinput-devel"]
depends = ["virtual:xserver-abi-input~24!xserver-xlibre-core"]
provides = [self.with_pkgver("xserver-xorg-input-driver")]
pkgdesc = "Generic input driver for XLibre server based on libinput"
license = "MIT"
url = "https://github.com/X11Libre/xf86-input-libinput"
source = f"https://github.com/X11Libre/xf86-input-libinput/archive/refs/tags/xlibre-xf86-input-libinput-{pkgver}.tar.gz"
sha256 = "f1be5a443af78307af18103a6bb614021fe163380b0eb43dec820a2389fbd6c8"


def post_install(self):
    self.install_license("COPYING")


@subpackage("xserver-xlibre-input-libinput-devel")
def _(self):
    self.provides = ["xserver-xorg-input-libinput-devel"]
    self.replaces = ["xserver-xorg-input-libinput-devel"]
    return self.default_devel()
