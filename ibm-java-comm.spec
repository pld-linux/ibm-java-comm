Summary:	Java Communications API
Summary(pl):	Java Communications API
Name:		ibm-java-comm
Version:	1.3
Release:	1
License:	unknown
Group:		Development/Languages/Java
Source0:	IBMJava2-JAVACOMM-13.tgz
URL:		http://www-106.ibm.com/developerworks/java/jdk/linux130/othpkgs.html
Requires:	jre
Provides:	java-comm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		jredir			%{_libdir}/java-jre

%description
Java Communications API gives Java applications a platform-independent
way of performing serial and parallel port communications for
technologies such as voice mail, fax, and smartcards. You can use Java
Communications API to write Java programs that access serial or
parallel ports. Java Communications API supports Electronic Industries
Association EIA-232 (RS232) serial ports and Institute of Electrical
and Electronics Engineers (IEEE) 1284 parallel ports.

%description -l pl
Java Communications API daje aplikacjom Javy niezale¿ny od platformy
sposób komunikacji przez port szeregowy i równoleg³y dla potrzeb
poczty g³osowej, faksów i smartcardów. Java Communications API mo¿e
byæ u¿ywane do pisania w Javie programów u¿ywaj±cych portów
szeregowych lub równoleg³ych. API to obs³uguje porty szeregowe EIA-232
(RS232) oraz równoleg³e IEEE 1284.

%prep
%setup  -q -n IBMJava2-13

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
