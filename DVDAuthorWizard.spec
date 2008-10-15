Name:           DVDAuthorWizard
Version:        1.4.6
Release:        2%{?dist}
Summary:        Create a video DVD from MPEG-2 files
Group:          Applications/Multimedia
License:        GPL
URL:            http://dvdauthorwizard.sourceforge.net
Source0:        http://dl.sf.net/dvdauthorwizard/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

BuildRequires:  desktop-file-utils
Requires:       kdebase3, bc, k3b, sox, mjpegtools, transcode, xine
Requires:       dvdauthor >= 0.6.11
Requires:       ImageMagick >= 6.2.0
Requires:       kdewebdev >= 3.3.0


%description
DVD Author Wizard will allow you to create a DVD from one or more DVD
compatible MPEG-2 files. It is designed to be very easy to use. All you need to
do is add one or multiple files to the playlist and answer the questions that
follow.


%prep
%setup -q
sed -i 's/\/\.\.\/share\/apps\/dvdauthorwizard//g' bin/DVDAuthorWizard.kmdr
sed -i 's/..\/share\/apps\/dvdauthorwizard/\/usr\/share\/apps\/DVDAuthorWizard/g' \
       bin/DVDAuthorWizard-Builder.sh

iconv -f iso8859-1 Changelog -t utf8 > Changelog.conv && /bin/mv -f Changelog.conv Changelog


%build
#nothing to build

cat << EOF > dvdauthorwizard
#!/bin/sh
# Simple script for friendly command line launching of dvdauthorwizard
exec %{_bindir}/kmdr-executor %{_datadir}/apps/%{name}/%{name}.kmdr
EOF


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/apps/%{name}
mkdir -p %{buildroot}%{_bindir}

install -pm0644 bin/%{name}.kmdr %{buildroot}%{_datadir}/apps/%{name}
install -pm0755 bin/%{name}-Builder.sh %{buildroot}%{_datadir}/apps/%{name}
install -pm0755 dvdauthorwizard %{buildroot}%{_bindir}
cp -a share/apps/dvdauthorwizard/Pictures %{buildroot}%{_datadir}/apps/%{name}

desktop-file-install --vendor "" \
                     --dir %{buildroot}%{_datadir}/applications \
                     %{SOURCE1}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc Changelog Creating\ Chapters.txt
%{_bindir}/dvdauthorwizard
%{_datadir}/apps/%{name}
%{_datadir}/applications/%{name}.desktop


%changelog
* Tue Sep 09 2008 Xavier Lamien <lxtnow@gmail.com> - 1.4.6-2
- Update files and rebuild for rpmfusion inclusion.

* Sun Jun 03 2007 Ian Chapman <packages@amiga-hardware.com> 1.4.6-1%{?dist}
- Upgrade to 1.4.6

* Tue Mar 13 2007 Ian Chapman <packages@amiga-hardware.com> 1.4.5-1%{?dist}
- Upgrade to 1.4.5
- Fixed loading of wizard decorations

* Sun Mar 04 2007 Ian Chapman <packages@amiga-hardware.com> 1.4.4-1%{?dist}
- Upgrade to 1.4.4

* Thu Jan 25 2007 Ian Chapman <packages@amiga-hardware.com> 1.4.3-1%{?dist}
- Upgrade to 1.4.3

* Wed Jan 03 2007 Ian Chapman <packages@amiga-hardware.com> 1.4.2-1%{?dist}
- Upgrade to 1.4.2

* Wed Oct 18 2006 Ian Chapman <packages@amiga-hardware.com> 1.4.1-2%{?dist}
- Added simple script for easier command line launching

* Sun Oct 01 2006 Ian Chapman <packages@amiga-hardware.com> 1.4.1-1%{?dist}
- Upgrade to 1.4.1

* Mon Sep 04 2006 Ian Chapman <packages@amiga-hardware.com> 1.3.0-2%{?dist}
- Renamed to DVDAuthorWizard

* Sat Aug 26 2006 Ian Chapman <packages@amiga-hardware.com> 1.3.0-1%{?dist}
- Initial release
