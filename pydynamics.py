#!/usr/bin/env python2
#-*- coding: utf-8 -*-

print "This program is currently depreciated"

import sys, os, shutil

current_dir = os.getcwd()
sys.path.insert(0,"/usr/lib/pymodules/python2.7/pmg_tk/startup/")
sys.path.insert(0,"/usr/lib/python2.7/dist-packages/pmg_tk/startup/")
sys.path.insert(0,"/usr/local/lib/python2.7/dist-packages/pmg_tk/startup/")

import dynamics_pymol_plugin
dynamics_pymol_plugin.init_function(1)
		
if os.path.isfile(sys.argv[1]) and len(sys.argv) == 3:
	#name = dynamics.load(sys.argv[1])
	#dir_path_project = dynamics.dynamics(name)
	#print dir_path_project + name + "_multimodel.pdb"
	#print sys.argv[2]
	os.chdir(current_dir)
	#shutil.copy(dir_path_project + name + "_multimodel.pdb", sys.argv[2])
elif dynamics_pymol_plugin.help_name.count(sys.argv[1]) == 1 or dynamics_pymol_plugin.clean_name.count(sys.argv[1]) == 1:
	name = sys.argv[1]
	dir_path_project = dynamics_pymol_plugin.dynamics(name)
else:
	print "Exit"
