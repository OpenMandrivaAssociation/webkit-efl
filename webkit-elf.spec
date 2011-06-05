%define major 0
%define libname %mklibname %name %major
%define develname %mklibname -d %name
%define svnrel 72693

Summary: Port of WebKit to EFL
Name: webkit-efl
Version: 0.1.0
Release: %mkrel -c %svnrel 3
License: LGPLv2+
Group: Graphical desktop/Enlightenment
URL: http://trac.enlightenment.org/e/wiki/EWebKit
Source: http://packages.profusion.mobi/webkit-efl/webkit-efl-svn-r%{svnrel}.tar.bz2
Patch0: webkit-efl-svn-r72693-libinstall.patch
Patch1: webkit-efl-svn-r72693-curl-link.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
BuildRequires: icu-devel
BuildRequires: jpeg-devel
BuildRequires: png-devel
BuildRequires: sqlite3-devel
BuildRequires: curl-devel
BuildRequires: libgstreamer0.10-plugins-base-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype2-devel
BuildRequires: cairo-devel
BuildRequires: gtk+2-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel

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
%setup -q -n webkit-efl-svn-r%{svnrel}
%patch0 -p0
%patch1 -p0

%build
%cmake -DPORT=Efl -DNETWORK_BACKEND=curl
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-,root,root)
%{_datadir}/ewebkit-0
%{_libdir}/libewebkit.so.0
%{_libdir}/libewebkit.so.0.*

%files -n %develname
%defattr(-,root,root)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/ewebkit-0
