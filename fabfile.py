from fabric import task
import os

# https://gist.github.com/search?l=Python&o=desc&q=from+fabric+import+task&s=updated

LOCAL_APP_PATH = os.path.dirname(__file__)
LOCAL_VENV_PATH = os.path.join(LOCAL_APP_PATH, 'venv')

VIRTUAL_ENV = os.environ['VIRTUAL_ENV']

default_hosts = os.environ['COMPUTERNAME']
code_dir = 'c:\\repos\\flasktaskr\project/'

@task
def test(c):
    # c.local(".\\venv\\Scripts\\nosetests.exe -v")
    # c.local(f'{VIRTUAL_ENV}\\Scripts\\nosetests.exe -v')
    # c.local(f'{VIRTUAL_ENV}\\Scripts\\activate.bat && {VIRTUAL_ENV}\\Scripts\\python.exe -V')
    # c.local(f'type {VIRTUAL_ENV}\\Scripts\\activate.bat')
    invoke.run(f'{VIRTUAL_ENV}\\Scripts\\python.exe -V')
    c.local(f'{VIRTUAL_ENV}\\Scripts\\nosetests.exe -V')
    '''
    with c.cd(code_dir):
        # c.local("nosetests -v")
        c.local('echo %cd%')
        # c.local(f'echo {LOCAL_VENV_PATH}')
        c.local(f'echo {VIRTUAL_ENV}')
        c.local(f'{VIRTUAL_ENV}\\Scripts\\nosetests.exe -v')
    '''

@task
def commit(c):
    message = raw_input("Enter a git commit message: ")
    c.local(f"git add . && git commit -am '{message}'")

@task
def push(c):
    c.local("git push origin master")

@task(hosts=default_hosts)
def prepare(c):
    test(c)
    # commit(c)
    # push(c)
