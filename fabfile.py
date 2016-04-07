from fabric.api import local


def run_manage(command):
    local('/home/vagrant/.virtualenvs/le-code-test/bin/python /vagrant/testsite/manage.py %s' % command)


def web():
    run_manage('runserver 0.0.0.0:8888')

def migrate():
    run_manage('migrate')

def make_migrations():
    run_manage('makemigrations')

def requirements():
    local('/home/vagrant/.virtualenvs/le-code-test/bin/pip install -r requirements.txt ')

# clear down DB and load sample fixtures
def load_sample_data():
    run_manage('flush')  # prompts for confirmation
    run_manage('loaddata fixtures/test_fixtures.json')
