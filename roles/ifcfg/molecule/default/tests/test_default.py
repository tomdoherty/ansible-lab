import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_package(host):
    f = host.package('bridge-utils')

    assert f.is_installed


def test_directory(host):
    f = host.file('/etc/sysconfig/network-scripts/')

    assert f.exists
    assert f.is_directory


def test_ifcfg_file(host):
    f = host.file('/etc/sysconfig/network-scripts/ifcfg-bridge0')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.contains('DEVICE="bridge0"')
    assert f.contains('TYPE="Bridge"')
    assert f.contains('ONBOOT="yes"')
    assert f.contains('IPADDR="192.168.1.1"')
    assert f.contains('NETMASK="255.255.255.0"')
