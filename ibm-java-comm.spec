Summary:	Java Comm
Summary(pl):	Java Comm
Name:		ibm-java-comm
Version:	1.3
Release:	1
License:	unknown
Group:		Java
Source0:	IBMJava2-JAVACOMM-13.tgz
URL:		http://www.ibm.com/developer
Requires:	jre
Provides:	java-comm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		jredir			%{_libdir}/java-jre

%description
Java Comm.

%description -l pl
Java Comm.

%prep
%setup  -q	-n IBMJava2-13

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{jredir}/lib/{ext,i386}
install jre/bin/*.so $RPM_BUILD_ROOT%{jredir}/lib/i386/
install jre/lib/ext/*.jar $RPM_BUILD_ROOT%{jredir}/lib/ext/ 
install jre/lib/*.properties $RPM_BUILD_ROOT%{jredir}/lib/

gzip -9nf docs/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*.gz
%attr(755,root,root) %{jredir}/lib/i386/*.so
%{jredir}/lib/ext/*.jar
%{jredir}/lib/*.properties
