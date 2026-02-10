pkgname = "xserver-xlibre"
pkgver = "25.1.2"
pkgrel = 0
build_style = "meson"
_fontroot = "/usr/share/fonts"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX libexecdir
    "-Dxorg=true",
    "-Dxephyr=true",
    "-Dxnest=true",
    "-Dxvfb=true",
    "-Dipv6=true",
    "-Dxcsecurity=true",
    "-Ddri3=true",
    "-Dglamor=true",
    "-Dglx=true",
    "-Dseatd_libseat=true",
    "-Dsuid_wrapper=true",
    "-Dlinux_acpi=true",
    "-Dudev=true",
    "-Dlinux_apm=false",
    "-Dhal=false",
    "-Dsystemd_logind=false",
    "-Dxkb_dir=/usr/share/X11/xkb",
    "-Dxkb_output_dir=/var/lib/xkb",
]
hostmakedepends = ["meson", "pkgconf", "xkbcomp", "flex"]
makedepends = [
    "dbus-devel",
    "font-util-devel",
    "libepoxy-devel",
    "libseat-devel",
    "libtirpc-devel",
    "libxcb-devel",
    "libxcvt-devel",
    "libxfont2-devel",
    "libxkbfile-devel",
    "libxkbui-devel",
    "libxrender-devel",
    "libxres-devel",
    "libxshmfence-devel",
    "libxtst-devel",
    "libxv-devel",
    "libxxf86dga-devel",
    "mesa-devel",
    "nettle-devel",
    "openssl3-devel",
    "pixman-devel",
    "xcb-util-devel",
    "xcb-util-image-devel",
    "xcb-util-keysyms-devel",
    "xcb-util-renderutil-devel",
    "xcb-util-wm-devel",
    "xkbcomp-devel",
    "xorgproto",
    "xtrans",
]
checkdepends = ["xkeyboard-config"]
depends = [
    "fonts-xorg",
    "iceauth",
    "setxkbmap",
    "transset",
    "xbacklight",
    "xcmsdb",
    "xcursorgen",
    "xdpyinfo",
    "xev",
    "xeyes",
    "xgamma",
    "xhost",
    "xinput",
    "xkbcomp",
    "xkill",
    "xlsatoms",
    "xlsclients",
    "xlsfonts",
    "xmodmap",
    "xpr",
    "xprop",
    "xrandr",
    "xrdb",
    "xrefresh",
    "xset",
    "xsetroot",
    "xvinfo",
    "xwd",
    "xwininfo",
    "xwud",
    self.with_pkgver("xserver-xlibre-minimal"),
]
provides = ["xserver-xorg"]
provider_priority = 100
replaces = ["xserver-xorg"]
replaces_priority = 100
pkgdesc = "Xlibre X server"
license = "MIT AND BSD-3-Clause"
url = "https://github.com/X11Libre/xserver"
source = f"https://github.com/X11Libre/xserver/archive/refs/tags/xlibre-xserver-{pkgver}.tar.gz"
sha256 = "a5ec231ae78d00aab7edaaf06d6c22fbaf2072eaf6d669a87f491c445efcf57d"
tool_flags = {
    "CFLAGS": ["-D_GNU_SOURCE", "-D__uid_t=uid_t", "-D__gid_t=gid_t"],
    "LDFLAGS": ["-Wl,-z,lazy"],  # must be set for modules to work
}
# FIXME int
hardening = ["!int"]
# test times out
options = ["!check", "empty"]

match self.profile().arch:
    case "x86_64":
        configure_args += ["-Dint10=x86emu"]
    case _:
        configure_args += ["-Dint10=false"]

_fontpaths = []

for _fp in ["misc", "100dpi:unscaled", "75dpi:unscaled", "TTF", "Type1"]:
    _fontpaths.append(f"/usr/share/fonts/{_fp}")

configure_args.append("-Ddefault_font_path=" + ",".join(_fontpaths))


def post_install(self):
    self.install_license("COPYING")

    self.chmod(self.destdir / "usr/lib/Xorg.wrap", mode=0o4755)
    # provided by xserver-xorg-protocol
    self.uninstall("usr/lib/xorg/protocol.txt")
    # from debian: https://salsa.debian.org/xorg-team/xserver/xorg-server
    # check debian/local/xvfb-run for updates as needed
    # note ours is slightly patched (non-GNU fmt(1))
    self.install_bin(self.files_path / "xvfb-run")
    self.install_man(self.files_path / "xvfb-run.1")


@subpackage("xserver-xlibre-xnest")
def _(self):
    self.pkgdesc = "Nested X server that runs as an X application"
    self.provides = ["xserver-xorg-xnest"]
    self.replaces = ["xserver-xorg-xnest"]
    self.provider_priority = 100
    self.replaces_priority = 100

    return ["usr/bin/Xnest", "usr/share/man/man1/Xnest.1"]


@subpackage("xserver-xlibre-xephyr")
def _(self):
    self.pkgdesc = "X server outputting to a window on a pre-existing display"
    self.provides = ["xserver-xorg-xephyr"]
    self.replaces = ["xserver-xorg-xephyr"]
    self.provider_priority = 100
    self.replaces_priority = 100
    return ["usr/bin/Xephyr", "usr/share/man/man1/Xephyr.1"]


@subpackage("xserver-xlibre-xvfb")
def _(self):
    self.pkgdesc = "Virtual framebuffer X server"
    self.depends += ["xkeyboard-config", "xauth", "ugetopt"]
    self.provides = ["xserver-xorg-xvfb"]
    self.replaces = ["xserver-xorg-xvfb"]
    self.provider_priority = 100
    self.replaces_priority = 100
    return [
        "usr/bin/Xvfb",
        "usr/bin/xvfb-run",
        "usr/share/man/man1/Xvfb.1",
        "usr/share/man/man1/xvfb-run.1",
    ]


@subpackage("xserver-xlibre-core")
def _(self):
    self.subdesc = "default server"
    # check if this needs to be updated when updating
    self.depends += [
        "so:libEGL.so.1!mesa-egl-libs",
        "xserver-xorg-protocol>=20180227", # https://github.com/xlibre-alpine/xlibre-ports/issues/4
        "xkeyboard-config",
    ]
    self.provides = [
        "xserver-abi-extension=10.0",
        "xserver-abi-input=24.4",
        "xserver-abi-video=25.2",
        "xserver-xorg-core",
    ]
    self.replaces = ["xserver-xorg-core"]
    self.replaces_priority = 100
    self.provider_priority = 100
    self.file_modes = {"usr/lib/Xorg.wrap": ("root", "root", 0o4755)}
    return [
        "usr/bin/X",
        "usr/bin/Xorg",
        "usr/bin/gtf",
        "usr/lib/xorg/modules",
        "usr/lib/Xorg*",
        "usr/share/man",
        "usr/share/X11",
    ]


@subpackage("xserver-xlibre-minimal")
def _(self):
    self.subdesc = "minimal metapackage"
    self.depends += [
        self.with_pkgver("xserver-xlibre-core"),
        "xauth",
        "xinit",
        "virtual:xserver-xlibre-input-driver!xserver-xlibre-input-none",
    ]
    self.options = ["empty"]
    self.provides = ["xserver-xorg-minimal"]
    self.replaces = ["xserver-xorg-minimal"]
    self.provider_priority = 100
    self.replaces_priority = 100
    return []


@subpackage("xserver-xlibre-input-none")
def _(self):
    self.subdesc = "no input driver"
    self.provides = ["xserver-xlibre-input-driver=0"]
    self.options = ["empty"]
    self.provides = ["xserver-xorg-input-none"]
    self.replaces = ["xserver-xorg-input-none"]
    self.provider_priority = 100
    self.replaces_priority = 100
    return []


@subpackage("xserver-xlibre-devel")
def _(self):
    self.depends += [
        "xorgproto",
        "xtrans",
        "libxfont2-devel",
        "libxkbfile-devel",
        "libxshmfence-devel",
        "libxcb-devel",
        "libxrender-devel",
        "libxrandr-devel",
        "libxi-devel",
        "libpciaccess-devel",
    ]
    self.provides = ["xserver-xorg-devel"]
    self.replaces = ["xserver-xorg-devel"]
    self.provider_priority = 100
    self.replaces_priority = 100
    return self.default_devel()
