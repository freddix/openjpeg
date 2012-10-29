Summary:	An open-source JPEG 2000 codec
Name:		openjpeg
Version:	1.5
Release:	1
Source0:	http://openjpeg.googlecode.com/files/%{name}_v%{rver}.tar.gz
# Source0-md5:	f9a3ccfa91ac34b589e9bf7577ce8ff9
Patch0:		%{name}-build.patch
License:	BSD
Group:		Libraries
URL:		http://www.openjpeg.org/
BuildRequires:	cmake
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The OpenJPEG library is an open-source JPEG 2000 codec written in C
language. It has been developed in order to promote the use of JPEG
2000, the new still-image comp ession standard from the Joint
Photographic Experts Group (JPEG).

%package devel
Summary:	Development tools for programs using the OpenJPEG library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the header files and libraries needed for
developing programs using the OpenJPEG library.

%prep
%setup -qn %{rname}_v%{rver}
%patch0 -p1

rm -rf jp3d libs

%build
install -d build
cd build
%cmake ..
%{__make} \
	CC="%{__cc}"		\
	OPTFLAGS="%{rpmcflags}"	\
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	CC="%{__cc}"		\
	DESTDIR=$RPM_BUILD_ROOT	\
	LDFLAGS="%{rpmldflags}"	\
	OPTFLAGS="%{rpmcflags}"

cd $RPM_BUILD_ROOT%{_libdir}
ln -sf libopenjpeg.so.? libopenjpeg.so

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopenjpeg-*.*.*.*.so
%attr(755,root,root) %ghost %{_libdir}/libopenjpeg.so.?

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}.h
%{_libdir}/libopenjpeg.so

