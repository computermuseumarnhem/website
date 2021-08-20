# website

Website at museum.hack42.nl.

# Getting started

```
cp ssh.inc.example ssh.inc
vi ssh.inc  # configure upload settings
python3 -m venv env
. ./env/bin/activate
pip install -r requirements.txt
make html
```

This generates a preview in the output/ directory.

# Writing content

See [the pelican manual on writing content](https://docs.getpelican.com/en/stable/content.html).

# Deploying

```
make publish
make rsync_upload
```

