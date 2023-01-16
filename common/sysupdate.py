import subprocess

def update_system():
    subprocess.run(["apt-get", "update"])
    subprocess.run(["apt-get", "upgrade", "-y"])

update_system()
