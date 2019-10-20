import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

def test_network_file(host):
    f = host.file('/etc/sysconfig/network')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.contains('GATEWAY=192.168.0.1')


def test_routes_file(host):
    f = host.file('/etc/sysconfig/network-scripts/routes-en0')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.contains('192.168.1.0/16 via 10.75.8.1 dev en0 metric 100')
