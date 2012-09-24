rhel6-python2.7-specs
=====================

Spec files for python2.7 for RHEL 6.

Building RPMs for python2.7
---------------------------
    python setup.py bdist_rpm --python=python2.7 --force-arch='%{_arch}'
