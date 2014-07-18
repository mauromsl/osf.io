# OSF 


- `master` Build Status: [![Build Status](https://magnum.travis-ci.com/CenterForOpenScience/osf.svg?token=QSc1BQcS2TSL63LmWF7Y&branch=master)](https://magnum.travis-ci.com/CenterForOpenScience/osf)
- `develop` Build Status: [![Build Status](https://magnum.travis-ci.com/CenterForOpenScience/osf.svg?token=QSc1BQcS2TSL63LmWF7Y&branch=develop)](https://magnum.travis-ci.com/CenterForOpenScience/osf)
- Public Repo: https://github.com/CenterForOpenScience/openscienceframework.org/
- Issues: https://github.com/CenterForOpenScience/openscienceframework.org/issues?state=open
- Huboard: https://huboard.com/CenterForOpenScience/openscienceframework.org#/
- Wiki: https://osf.io/a92ji/wiki/home/

## Help

Solutions to many common issues may be found at the [OSF Wiki](https://osf.io/a92ji/wiki/home/).

## Quickstart

These instructions should work on Mac OSX >= 10.7

- Create your virtualenv.

- Copy `website/settings/local-dist.py` to `website/settings/local.py.`  NOTE: This is your local settings file, which overrides the settings in `website/settings/defaults.py`. It will not be added to source control, so change it as you wish.

```bash
$ cp website/settings/local-dist.py website/settings/local.py
```

- You will need to:
    - Create local.py files for addons that need them.
    - Install MongoDB.
    - Install libxml2 and libxslt (required for installing lxml).
    - Install elasticsearch.
    - Install GPG.
    - Install requirements.
    - Create a GPG key.

- To do so, on MacOSX with [homebrew](http://brew.sh/) (click link for homebrew installation instructions), run:

```bash
$ pip install invoke
$ invoke setup
```


- If you don't have bower installed (see below for more details)
```bash
$ npm install -g bower
```


- If the bower installation complains about permissions
```bash
$ sudo npm install -g bower
```


- To install all of our bower-managed Javascript components

```bash
$ bower install
```


- Optionally, you may install the requirements for the Modular File Renderer:

```bash
$ invoke mfr_requirements
```

and for addons:

```bash
$ invoke addon_requirements
```

- On Linux systems, you may have to install python-pip, MongoDB, libxml2, libxslt, elasticsearch, and GPG manually before running the above commands.

- If invoke setup hangs when 'Generating GnuPG key' (especially under linux), you may need to install some additonal software to make this work. For apt-getters this looks like: 

```bash
sudo apt-get install rng-tools
```

next edit /etc/default/rng-tools and set:

```
HRNGDEVICE=/dev/urandom
```

last start the rng-tools daemon with:

```
sudo /etc/init.d/rng-tools start
```

__source: http://www.howtoforge.com/helping-the-random-number-generator-to-gain-enough-entropy-with-rng-tools-debian-lenny __

## Starting Up

- Run your mongodb process.

```bash
$ invoke mongo
```

- Run your local development server.

```bash
$ invoke server
```

## Running the shell

To open the interactive Python shell, run:

```bash
$ invoke shell
```

## Running Tests

To run all tests:

```bash
$ invoke test
```

To run a certain test method

```bash
$ nosetests tests/test_module.py:TestClass.test_method
```

### Testing Addons

Addons tests are not run by default. To execute addons tests, run

```bash
$ invoke test_addons
```

### Testing Email


First, set `MAIL_SERVER` to `localhost:1025` in you `local.py` file.

website/settings/local.py

```python
...
MAIL_SERVER = "localhost:1025"
...
```

Sent emails will show up in your server logs.

*Optional*: fire up a pseudo-mailserver with:

```bash
$ invoke mailserver -p 1025
```

## Using Celery

### Installing Celery + RabbitMQ

- Install RabbitMQ. On MacOSX with homebrew,

```bash
$ brew update
$ brew install rabbitmq
```
The scripts are installed to `/usr/local/sbin`, so you may need to add `PATH=$PATH:/usr/local/sbin` to your `.bash_profile`.

For instructions for other OS's, see [the official docs](http://www.rabbitmq.com/download.html).

Then start the RabbitMQ server with

```bash
$ invoke rabbitmq
```

If you want the rabbitmq server to start every time you start your computer (MacOSX), run

```bash
$ ln -sfv /usr/local/opt/rabbitmq/*.plist ~/Library/LaunchAgents
$ launchctl load ~/Library/LaunchAgents/homebrew.mxcl.rabbitmq.plist
```

### Starting A Celery Worker

```bash
invoke celery_worker
```

## Using Search

### Solr
- Make sure [Java is installed](https://www.java.com/en/download/help/index_installing.xml)

- In your `website/settings/local.py` file, set `SEARCH_ENGINE` to 'solr'.

```python
SEARCH_ENGINE = 'solr'
```

- Start the Solr server and migrate the models.

```bash
$ invoke solr
$ invoke migrate_search
```

#### Starting A Local Solr Server

```bash
$ invoke solr
```

This will start a Solr server on port 8983.

### Elasticsearch

- Install Elasticsearch

#### Mac OSX

```bash
$ brew install elasticsearch
```
_note: Oracle JDK 7 must be installed for elasticsearch to run_

#### Ubuntu 

```bash
$ wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.2.1.deb 
$ sudo dpkg -i elasticsearch-1.2.1.deb
```

#### Using Elasticsearch
- In your `website/settings/local.py` file, set `SEARCH_ENGINE` to 'elastic'.

```python
SEARCH_ENGINE = 'elastic'
```
- Start the Elasticsearch server and migrate the models.

```bash
$ invoke elasticsearch
$ invoke migrate_search
```
#### Starting a local Elasticsearch server

```bash
$ invoke elasticsearch
```


## Using Bower for front-end dependencies

We use [bower](http://bower.io/) to automatically download and manage dependencies for front-end libraries.

To get the bower CLI, you must have Node installed.

```bash
$ brew update && brew install node
$ npm install -g bower
```

To install a library:

```bash
$ bower install zeroclipboard --save
```

The `--save` option automatically adds an entry to the `bower.json` after downloading the library.

This will save the library in `website/static/vendor/bower_components/`, where it can be imported like any other module.


## Summary

If you have all the above services installed, you can start *everything* up with this sequence

```bash
invoke mongo -d  # Runs mongod as a daemon
invoke mailserver
invoke rabbitmq
invoke celery_worker
invoke solr
invoke server
```

