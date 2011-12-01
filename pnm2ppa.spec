Name: pnm2ppa
Summary: Drivers for printing to HP PPA printers
Epoch: 1
Version: 1.04
Release: 19%{?dist}
URL: http://sourceforge.net/projects/pnm2ppa 
Source: http://download.sourceforge.net/pnm2ppa/pnm2ppa-%{version}.tar.gz
Source1: http://www.httptech.com/ppa/files/ppa-0.8.6.tar.gz
# Upstream sync.
Patch2: pbm2ppa-20000205.diff
# Use RPM_OPT_FLAGS.
Patch3: pnm2ppa-redhat.patch
License: GPLv2
Group: Applications/Publishing
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%define topdir pnm2ppa-%{version}

%description
Pnm2ppa is a color driver for HP PPA host-based printers such as the
HP710C, 712C, 720C, 722C, 820Cse, 820Cxi, 1000Cse, and 1000Cxi.
Pnm2ppa accepts Ghostscript output in PPM format and sends it to the
printer in PPA format.

Install pnm2ppa if you need to print to a PPA printer.

%prep
%setup -q -n %{topdir}

#pbm2ppa source
%setup -q -T -D -a 1 -n %{topdir}
%patch2 -p0 -b .20000205
%patch3 -p1 -b .rh

%build
make 
cd pbm2ppa-0.8.6
make


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
make INSTALLDIR=$RPM_BUILD_ROOT%{_bindir} CONFDIR=$RPM_BUILD_ROOT%{_sysconfdir} \
    MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 install 
install -m 0755 utils/Linux/detect_ppa $RPM_BUILD_ROOT%{_bindir}
install -m 0755 utils/Linux/test_ppa $RPM_BUILD_ROOT%{_bindir}
install -m 0755 pbm2ppa-0.8.6/pbm2ppa  $RPM_BUILD_ROOT%{_bindir}
install -m 0755 pbm2ppa-0.8.6/pbmtpg   $RPM_BUILD_ROOT%{_bindir}
install -m 0644 pbm2ppa-0.8.6/pbm2ppa.conf $RPM_BUILD_ROOT%{_sysconfdir}
install -m 0644 pbm2ppa-0.8.6/pbm2ppa.1   $RPM_BUILD_ROOT%{_mandir}/man1

chmod 644 docs/en/LICENSE
mkdir -p pbm2ppa
for file in CALIBRATION CREDITS INSTALL INSTALL-MORE LICENSE README ; do
  install -m 0644 pbm2ppa-0.8.6/$file pbm2ppa/$file
done

%clean
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc docs/en/CREDITS docs/en/INSTALL docs/en/LICENSE docs/en/README
%doc docs/en/RELEASE-NOTES docs/en/TODO
%doc docs/en/INSTALL.REDHAT.txt docs/en/COLOR.txt docs/en/CALIBRATION.txt
%doc docs/en/INSTALL.REDHAT.html docs/en/COLOR.html docs/en/CALIBRATION.html
%doc test.ps
%doc pbm2ppa
%{_bindir}/pnm2ppa
%{_bindir}/pbm2ppa
%{_bindir}/pbmtpg
%{_bindir}/calibrate_ppa
%{_bindir}/test_ppa
%{_bindir}/detect_ppa
%{_mandir}/man1/pnm2ppa.1*
%{_mandir}/man1/pbm2ppa.1*
%config(noreplace) %{_sysconfdir}/pnm2ppa.conf
%config(noreplace) %{_sysconfdir}/pbm2ppa.conf

%changelog
* Fri Mar  5 2010 Tim Waugh <twaugh@redhat.com> - 1:1.04-19
- Consistent use of macros.
- Removed ancient obsoletes tag.
- Clean buildroot in install section not prep section.
- Make setup quiet.
- Use noreplace for config files.

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1:1.04-18.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.04-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.04-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 24 2008 Tim Waugh <twaugh@redhat.com> 1:1.04-16
- Removed patch fuzz.

* Wed Feb 13 2008 Tim Waugh <twaugh@redhat.com> 1:1.04-15
- Rebuild for GCC 4.3.

* Wed Aug 29 2007 Tim Waugh <twaugh@redhat.com> 1:1.04-14
- Added dist tag.
- Fixed summary.
- Better buildroot tag.
- More specific license tag.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:1.04-13.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1:1.04-13.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1:1.04-13.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar 16 2005 Tim Waugh <twaugh@redhat.com> 1:1.04-13
- Rebuild for new GCC.

* Wed Feb  9 2005 Tim Waugh <twaugh@redhat.com> 1:1.04-12
- s/Copyright:/License:/.
- s/Serial:/Epoch:/.
- Rebuilt.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 19 2004 Tim Waugh <twaugh@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Nov 20 2002 Tim Powers <timp@redhat.com>
- rebuild in current collinst

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Mon Dec 11 2000 Crutcher Dunnavant <crutcher@redhat.com>
- Upgrade to 1.04, editied the pbm2ppa patch to add <string.h>
- to pbmtpg.c, which uses strmp, edited the redhat patch to
- apply cleanly.

* Thu Aug 16 2000 Bill Nottingham <notting@redhat.com>
- tweak summary

* Thu Aug  3 2000 Bill Nottingham <notting@redhat.com>
- build upstream package

* Tue Jul 11 2000 Duncan Haldane <duncan_haldane@users.sourceforge.net>
- updated for 1.0 release.

* Mon Jul 10 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- remove execute bits from config file and man-page

* Sun Apr 09 2000 <duncan_haldane@users.sourceforge.net>
- added optional updated rhs-printfilter  files

* Thu Feb 10 2000 Bill Nottingham <notting@redhat.com>
- adopt upstream package

* Sun Feb 6 2000 <duncan_haldane@users.sourceforge.net>
- new pnm2ppa release,  and add pbm2ppa driver.

* Thu Jan 7 2000 <duncan_haldane@users.sourceforge.net>
- created rpm



