%define major 0
%define libname %mklibname %name %major
%define develname %mklibname -d %name
%define svnrel 127150

Summary: Port of WebKit to EFL
Name: webkit-efl
Version: 0.1.0
Release: %mkrel -c r%svnrel 6
License: LGPLv2+
Group: Graphical desktop/Enlightenment
URL: http://trac.enlightenment.org/e/wiki/EWebKit
Source0: http://packages.profusion.mobi/webkit-efl/%name-svn-r%{svnrel}.tar.bz2
Patch0: webkit-efl-svn-r98964-libinstall.patch
Patch1: webkit-efl-svn-r98964-curl-link.patch
Patch2: webkit-efl-remove-minor-in-dep.patch
Patch3: webkit-efl-fix-lib64-install-v2.patch
Patch4: webkit-efl-0000-fix-include-hb-h.patch
Patch5: webkit-efl-svn-r127150-link.patch
BuildRequires: cmake
BuildRequires: bison
BuildRequires: flex
BuildRequires: gperf
BuildRequires: ecore-devel
BuildRequires: edje
BuildRequires: embryo
BuildRequires: edje-devel
BuildRequires: evas-devel
BuildRequires: eina-devel
BuildRequires: e_dbus-devel
BuildRequires: e_dbus
BuildRequires: eeze-devel
BuildRequires: efreet-devel
BuildRequires: pkgconfig(icu-i18n)
BuildRequires: jpeg-devel
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(libcurl)
BuildRequires: libgstreamer0.10-plugins-base-devel
BuildRequires: fontconfig-devel
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libxslt)
BuildRequires: libsoup-devel
BuildRequires: harfbuzz-devel
BuildRequires: pkgconfig(x11)
BuildRequires: gtest-devel


%description
Also known as WebKit-EFL, this is the port of WebKit to EFL. In order to
keep it general and as independent as possible it uses (directly) a small
subset of EFL libraries: Evas, Ecore and Edje. Complex non-HTML elements
such as menus are delegated by means of callbacks that one should implement
as desired, probably using Elementary as Eve does.

%package -n %libname
Summary: Enlightenment WebKit Library
Group: System/Libraries

%description -n %libname
Enlightenment WebKit Library.

%package -n %develname
Summary: Enlightenment WebKit Library - devel files
Group: System/Libraries
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release
Provides: ewebkit-devel = %version-%release

%description -n %develname
ewebkit development headers and development libraries.

%prep
%setup -qn %name-svn-r%svnrel
%patch4 -p1
%patch5 -p1

%build
%cmake .. -DPORT=Efl -DSHARED_CORE=ON -DCMAKE_BUILD_TYPE=Release -DNETWORK_BACKEND=curl
%make

%install
%makeinstall_std -C build

%files -n %libname
%{_datadir}/ewebkit-0
%{_libdir}/libewebkit.so.0
%{_libdir}/libewebkit.so.0.*
%{_libdir}/libjavascriptcore_efl.so.0
%{_libdir}/libjavascriptcore_efl.so.0.*
%{_libdir}/libwebcore_efl.so.0
%{_libdir}/libwebcore_efl.so.0.*

%files -n %develname
%{_libdir}/*.so
%{_prefix}/lib/pkgconfig/*.pc
%{_includedir}/ewebkit-0
