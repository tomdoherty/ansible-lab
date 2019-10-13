import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_ntp_file(host):
    f = host.file('/etc/ntp.conf')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_ntp_is_installed(host):
    ntp = host.package("ntp")
    assert ntp.is_installed


def test_ntp_running_and_enabled(host):
    ntp = host.service("ntpd")
    assert ntp.is_running
    assert ntp.is_enabled
