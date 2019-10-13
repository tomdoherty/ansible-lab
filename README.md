# ansible-lab


messing about with ansible


    virtualenv --python=python3 virtualenv
    . virtualenv/bin/activate
    pip install -r requirements.txt

    cd roles/ntp
    molecule test
    cd ../..

    vagrant up
    ansible-playbook playbook.yml

    vagrant destroy -f
