routes
=========

Configures Red Hat static routes

Requirements
------------

RHEL/Centos based system

Role Variables
--------------

Configures default gateway or takes a dictionary of routes/settings

e.g. 
    routes_default: 192.168.0.1

    routes_routes:
      "North":
        device: 'bond0'
        target: '10.75.0.0/16'
        gateway: '10.75.8.1'
        metric: 100

    # routes_routes:
    #   comment:
    #     device: name of device to use (e.g. bond0)
    #     target: target (e.g. 10.75.0.0/16)
    #     gateway: gateway to use (e.g. 10.75.8.1)
    #     metric: weight to set (e.g. 100)

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables
passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: routes, x: 42 }

License
-------

BSD

Author Information
------------------

Tom Doherty
