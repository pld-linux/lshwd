Summary:	Lists hardware devices and their approp modules
Name:		lshwd
Version:	1.1.3
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://user-contributions.org/projects/lshwd/source/%{name}-%{version}.tar.gz
# Source0-md5:	493ae06aada341f0bde063aab3c4167f
URL:		http://user-contributions.org/projects/lshwd/
BuildRequires:	libusb-devel
BuildRequires:	pciutils-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lshwd - lists hardware devices and their approp modules. currently
supports pci, usb, pcmcia, and firewire devices. lshwd uses pcitable &
usbtable files (can be located at same directory or /usr/share/hwdata)
for displaying extended description and module names. module names are
then parsed for generic names and changes accordingly.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
install lshwd $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
