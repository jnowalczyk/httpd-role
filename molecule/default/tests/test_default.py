import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_httpd_is_listening(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening


def test_httpd_is_running(host):
    assert host.service("httpd").is_running
