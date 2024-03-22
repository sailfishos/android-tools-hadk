Name:       android-tools-hadk

Summary:    Minimal set of android tools
Version:    5.1.1_r38
Release:    1
License:    Apache 2.0
Source0:    android-tools-hadk-%{version}.tar.gz
Recommends: android-tools-mkbootimg

%description
android-tools for HADK

%package -n sudo-for-abuild
Summary:    Install this to allow OBS abuild user to use sudo in build
Requires:   %{name} = %{version}-%{release}
Requires:   sudo

%description -n sudo-for-abuild
Allow abuild user to execute sudo in an OBS build root.

%prep
%autosetup

%build

%install
install -dm755 %{buildroot}%{_bindir}
sed -e 's/@VERSION@/%{version}/' mer-android-chroot > %{buildroot}%{_bindir}/ubu-chroot
chmod 755 %{buildroot}%{_bindir}/ubu-chroot
install -D -m 755  mer-ubusdk-bash-setup %{buildroot}%{_datadir}/ubu-chroot/mer-ubusdk-bash-setup
# For sudo-for-abuild
install -D -m 755  sudoers.abuild %{buildroot}%{_sysconfdir}/sudoers.d/abuild

%files
%{_bindir}/ubu-chroot
%{_datadir}/ubu-chroot/*

%files -n sudo-for-abuild
%{_sysconfdir}/sudoers.d/abuild
