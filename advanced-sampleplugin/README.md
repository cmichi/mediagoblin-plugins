# Readme

To install the plugin enter your `mediagoblin` folder and execute:

	git clone https://github.com/cmichi/mediagoblin-plugins.git
	cd mediagoblin-plugins/advanced-sampleplugin/
	make

To configure the plugin add to the `[plugins]` section of your
`mediagoblin_local.ini`:

	[plugins]
	[[advanced-sampleplugin]]
	bar = "custom-foo"

