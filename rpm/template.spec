Name:           ros-melodic-control-toolbox
Version:        1.17.0
Release:        0%{?dist}
Summary:        ROS control_toolbox package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/control_toolbox
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-control-msgs
Requires:       ros-melodic-dynamic-reconfigure
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-realtime-tools
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-std-msgs
Requires:       tinyxml-devel
BuildRequires:  ros-melodic-catkin >= 0.5.68
BuildRequires:  ros-melodic-cmake-modules
BuildRequires:  ros-melodic-control-msgs
BuildRequires:  ros-melodic-dynamic-reconfigure
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-realtime-tools
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-rosunit
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  tinyxml-devel

%description
The control toolbox contains modules that are useful across all controllers.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu Jan 31 2019 Bence Magyar <bence.magyar.robotics@gmail.com> - 1.17.0-0
- Autogenerated by Bloom

* Tue Mar 20 2018 Sachin Chitta <sachinc@willowgarage.com> - 1.16.0-0
- Autogenerated by Bloom

