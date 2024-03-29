#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-Fenzo
Version  : 0.10.1
Release  : 1
URL      : https://github.com/Netflix/Fenzo/archive/0.10.1.tar.gz
Source0  : https://github.com/Netflix/Fenzo/archive/0.10.1.tar.gz
Source1  : https://repo1.maven.org/maven2/com/netflix/fenzo/fenzo-core/0.10.1/fenzo-core-0.10.1.jar
Source2  : https://repo1.maven.org/maven2/com/netflix/fenzo/fenzo-core/0.10.1/fenzo-core-0.10.1.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-Fenzo-data = %{version}-%{release}
BuildRequires : buildreq-mvn
BuildRequires : gradle

%description
# Fenzo
## Overview
Fenzo is a scheduler Java library for Apache Mesos frameworks that supports plugins for scheduling
optimizations and facilitates cluster autoscaling.

%package data
Summary: data components for the mvn-Fenzo package.
Group: Data

%description data
data components for the mvn-Fenzo package.


%prep
%setup -q -n Fenzo-0.10.1

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/netflix/fenzo/fenzo-core/0.10.1
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/netflix/fenzo/fenzo-core/0.10.1/fenzo-core-0.10.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/netflix/fenzo/fenzo-core/0.10.1
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/netflix/fenzo/fenzo-core/0.10.1/fenzo-core-0.10.1.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/netflix/fenzo/fenzo-core/0.10.1/fenzo-core-0.10.1.jar
/usr/share/java/.m2/repository/com/netflix/fenzo/fenzo-core/0.10.1/fenzo-core-0.10.1.pom
