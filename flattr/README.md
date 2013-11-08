# Readme

At the moment there is no fitting template hook for the button
in the upstream MediaGoblin version. I have opened an issue for
this, but until it is merged you have to add a template hook 
by yourself:

Edit the file `/mediagoblin/mediagoblin/templates/mediagoblin/user_pages/media.html`,
in line 70 you will see:

	<h2 class="media_title">
	{{ media.title }}
	</h2>

Just add this line after the `</h2>`:

	{% template_hook("near_media_title") %}

To install the plugin enter your `mediagoblin` folder and execute:

	git clone https://github.com/cmichi/mediagoblin-plugins.git
	cd mediagoblin-plugins/flattr/
	make

To configure the plugin add to the `[plugins]` section of your
`mediagoblin_local.ini`:

	[plugins]
	[[flattr]]
	uid = "your_flattr_username"

Currently there is an auto-submit button created on each media 
page.

# ToDo

 * Currently only works when JS enabled
 * Add possibility to disable the auto-submit button and instead
   use the same button for the whole website
 * The flattr button description currently uses the MediaGoblin
   MediaEntry description. If the user used e.g. Markdown syntax
   there, the syntax is also used within the Flattr thing description.
   The description should be sanatized.
