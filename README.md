Basic Read

This is for adding 'default colors', for users to select colors for various models.

It adds colors based on an apps frontend framework.

Install as 3rd party django app (i.e. add to 'installed_apps' in settings)

Create a model that will hold custom colors in any app; that model should extend 'ColorModel' from colors app.

Steps for app:
Install app
create a custom color model that extends the ColorModel
it will show any bootstrap colors in the form when adding a new whatever in addition to user created colors
