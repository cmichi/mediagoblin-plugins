# Readme

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
