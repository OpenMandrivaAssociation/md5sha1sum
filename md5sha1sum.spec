Summary:	Microbrew MD5sum/SHA1sum/RIPEMD160sum
Name:		md5sha1sum
Version:	0.9.5
Release:	%mkrel 1
License:	GPLv2+
Group:		System/Base
URL:		http://www.microbrew.org/tools/md5sha1sum/
Source0:	http://www.microbrew.org/tools/md5sha1sum/%{name}-%{version}.tar.gz
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This toolset provides md5sum, sha1sum, and ripemd160sum. They are intended to
be drop in replacements for the tools from GNU textutils. Since installing
textutils is somewhat excessive for just two utilities, these are meant to be
the more compact and easier to install replacements. This is useful on systems
such as Solaris where most of the tools from textutils are already provided by
the vendor.

%prep

%setup -q


%build
cat > sys-setup.mk << EOF
CC=%{_bindir}/gcc
CFLAGS= %{optflags} -I%{_includedir}
LDFLAGS= %{ldflags} `pkg-config --libs openssl`
BINDIR=%{_bindir}
MD5BINNAME=ubmd5sum
SHA1BINNAME=ubsha1sum
RIPEMD160BINNAME=ubripemd160sum
EOF

%make

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -m0755 ubmd5sum %{buildroot}%{_bindir}/
ln -snf ubmd5sum %{buildroot}%{_bindir}/ubsha1sum
ln -snf ubmd5sum %{buildroot}%{_bindir}/ubripemd160sum

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc ChangeLog LICENSE README
%{_bindir}/ubmd5sum
%{_bindir}/ubsha1sum
%{_bindir}/ubripemd160sum



%changelog
* Mon Sep 26 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.5-1mdv2012.0
+ Revision: 701268
- import md5sha1sum


* Mon Sep 26 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.5-1mdv2010.2
- initial Mandriva package
