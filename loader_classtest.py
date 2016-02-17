#!/usr/bin/python
#
# Example OO (Class) Plugin Loading
#
#    Copyright (C) 2016  Glen Pitt-Pladdy
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#
# See: https://www.pitt-pladdy.com/blog/_20160217-161338_0000_Simple_Python_Plugins/
#


import imp
import sys
import gc

# Name of the plugin we are going to load
name = 'plugin_classtest'


# Convenience memory display function - run garbage collect and print number of objects
def collectprint ( stage=None ):
	gc.collect()	# garbage collect
	if stage != None:
		print stage
		print "\t#objects: %d" % len(gc.get_objects())
	else:
		print "number of objects: %d" % len(gc.get_objects())


# load module
collectprint( 'Before Loading' )
info = imp.find_module ( name )	# search path optional and includes prefix, return (file, pathname, description)
plugin = imp.load_module ( name, *info )	# returns object
collectprint( 'Module Loaded' )

# use class
obj = plugin.plugintest ()	# gets object for plugintest
collectprint( 'Object Instance' )
del info
del plugin
collectprint( 'Cleaned up module vars' )

# run method
obj.test ()
collectprint( 'After test() method run' )

# unload
del obj
collectprint( 'Destroyed object' )
sys.modules.pop ( name )
collectprint( 'Removed module' )


