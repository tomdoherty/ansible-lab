# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure('2') do |config|
  config.vm.box = 'centos/7'
  config.ssh.insert_key = false
  config.vm.synced_folder '.', '/vagrant', disabled: 'true'
  config.vm.provider :virtualbox do |v|
    v.memory = 256
    v.linked_clone = true
  end

  config.vm.define 'app1' do |app|
    app.vm.hostname = 'app1'
    app.vm.network 'private_network', ip: '192.168.33.10'
  end

  config.vm.define 'app2' do |app|
    app.vm.hostname = 'app2'
    app.vm.network 'private_network', ip: '192.168.33.11'
  end

  config.vm.define 'db' do |app|
    app.vm.hostname = 'db'
    app.vm.network 'private_network', ip: '192.168.33.12'
  end
  config.vm.provision 'ansible' do |ansible|
    ansible.playbook = 'playbooks/main.yml'
    ansible.become = true
  end
end
