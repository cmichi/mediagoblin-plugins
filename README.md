# Readme

This repository is a loose collection of various plugins I write/wrote
for the [GNU MediaGoblin](http://mediagoblin.org) project.
A while ago I dumped flickr and deviantart and migrated to
my own [MediaGoblin instance](http://media.micha.elmueller.net). 

**Project status:** I am merely starting out writing stuff for
MediaGoblin. Some things may still be a little bit wobbly.
Currently this code has only been tested with v0.7.1.


# Plugins

In order to install a plugin execute `../../bin/python2.7 setup.py develop`
in its folder. Afterwards execute `./bin/gmg dbupdate` in the MediaGoblin
root.


## advanced-sampleplugin

An advanced version of the 
[sampleplugin](http://mediagoblin.readthedocs.org/en/latest/pluginwriter/quickstart.html)
described in the MediaGoblin documentation. This one uses template hooks,
template variables, config files and default configuration.

## piwik

Piwik is a the free software alternative to Google Analytics.
This (very simple plugin) inserts your Piwik tracking code right before 
`</body>`. Sure you could also just add the code in the theme directly. 
But then you would have to add it after each MediaGoblin update. Using 
a plugin is more comfortable.

## flattr

Adds a [Flattr](http://flattr.com/) auto-submit button to each media entry 
detail view.


# Helpful links

[MediaGoblin Plugin API](http://mediagoblin.readthedocs.org/en/v0.5.1/pluginwriter/api.html)


# License

MediaGoblin is licensed under AGPLv3, thus the plugins have to be as well.
See `LICENSE` for the AGPLv3 text.
