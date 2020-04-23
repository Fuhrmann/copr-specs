%define SHA256SUM0 5891ca1525bae21d60604d1feb35a26ede0217ec02d75f5ff16febee7e9f3430
%define debug_package %nil
%define base_name i3

Name:           i3-gaps
Version:        4.18.1
Release:        4%{?dist}
Summary:        i3 with more features
License:        BSD
URL:            https://github.com/Airblader/%{base_name}
Source0:        https://github.com/Airblader/%{base_name}/archive/%{version}.tar.gz

BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: asciidoc
BuildRequires: bison
BuildRequires: flex
BuildRequires: libev-devel
BuildRequires: libX11-devel
BuildRequires: libxcb-devel
BuildRequires: libXcursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libxkbfile-devel
BuildRequires: pango-devel
BuildRequires: pcre-devel
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Data::Dumper::Names)
BuildRequires: startup-notification-devel
BuildRequires: xcb-proto
BuildRequires: xcb-util-cursor-devel
BuildRequires: xcb-util-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: xmlto
BuildRequires: yajl-devel
BuildRequires: git
BuildRequires: pkgconfig(xcb-xrm)
BuildRequires: pkgconfig(pangocairo)
BuildRequires: pkgconfig(cairo-xcb)

Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))
Requires:       xorg-x11-fonts-misc


Conflicts:      otherproviders(i3)
Provides:       i3 = %{version}


%description
Key features of i3 are correct implementation of XrandR, horizontal and vertical
columns (think of a table) in tiling. Also, special focus is on writing clean,
readable and well documented code. i3 uses xcb for asynchronous communication
with X11, and has several measures to be very fast.

Please be aware that i3 is primarily targeted at advanced users and developers.

%package        doc
Summary:        Documentation for %{name}
BuildRequires:  doxygen
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
Asciidoc and doxygen generated documentations for %{name}.

%prep
echo "%SHA256SUM0 %SOURCE0" | sha256sum -c -
%autosetup -n %{base_name}-%{version}

# Drop /usr/bin/env lines in those which will be installed to %%_bindir.
find . -maxdepth 1 -type f -name "i3*" -exec sed -i -e '1s;^#!/usr/bin/env perl;#!/usr/bin/perl;' {} + -print

# 1. Drop dwarf-2, -g3 in CFLAGS recommended by gcc maintainer. Since upstream
# uses -pipe and -g only, we can safely ignore these, but ldflags needs
# override still.
# 2. Preserve the timestamps.
#sed -i -e 's|LDFLAGS ?=|override LDFLAGS +=|g' \
#       -e 's|INSTALL=.*|INSTALL=install -p|g' \
#       common.mk

%build
autoreconf -fi
%configure --disable-sanitizers
%make_build -C *-redhat-linux-gnu CFLAGS+="-U_FORTIFY_SOURCE"

doxygen pseudo-doc.doxygen
mv pseudo-doc/html pseudo-doc/doxygen

%install
%make_install -C *-redhat-linux-gnu

mkdir -p %{buildroot}%{_mandir}/man1/
install -Dpm0644 *-redhat-linux-gnu/man/*.1 \
        %{buildroot}%{_mandir}/man1/

#check
#ifnarch s390 s390x
## TODO: with xorg dummy to test the package.
##cd testcases/ && ./complete-run.pl -p 1
#endif

%files
%doc RELEASE-NOTES-%{version}
%license LICENSE
%{_bindir}/%{base_name}*
%{_includedir}/%{base_name}/
%dir %{_sysconfdir}/%{base_name}/
%config(noreplace) %{_sysconfdir}/%{base_name}/config
%config(noreplace) %{_sysconfdir}/%{base_name}/config.keycodes
%{_datadir}/xsessions/%{base_name}.desktop
%{_datadir}/xsessions/%{base_name}-with-shmlog.desktop
%{_mandir}/man*/%{base_name}*
%{_datadir}/applications/%{base_name}.desktop
%exclude %{_docdir}/%{base_name}/

%files doc
%doc docs/*.{html,png} pseudo-doc/doxygen/

%changelog
* Thu Apr 23 2020 Ricardo Fuhrmann <fuhrmanns+copr@gmail.com> - 4.18.1-4
- 4.18.1

