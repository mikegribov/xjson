# -*- coding: utf-8 -*-

from src.xjson import XJson
import os
import sys

from src.plugins.json import PluginJson

#plugin = PluginJson("D:\\WORK\\GITHUB\\djson\\tests\examples\\single_file_objarr.json")
#print(plugin.get())

# fj = FiledJson(os.path.join("examples", "countries"))

#dj = DJson(os.path.join("tests", "examples", "countries", "single_file"))
#dj = DJson(os.path.join("tests", "examples", "empty_file"))
#dj = DJson(os.path.join("tests", "examples", "single_file_object.json"))
#dj = DJson(os.path.join("tests", "examples", "single_file_objarr.json"))
#dj = DJson(os.path.join("tests", "examples", "single_file_arrobj.json"))
#dj = DJson(os.path.join("tests", "examples", "single_file_array.json"))

#dj = DJson(os.path.join("tests", "examples", "empty_dir"))
#dj = DJson(os.path.join("tests", "examples", "countries", "dir_one_level"))
dj = XJson(os.path.join("tests", "examples", "countries", "dir_several_level"))

print(dj.structure)
#print(dj.get_value('russia.population'))
print(dj.alias('russia_population'))

#print(DJson().copy_from(dj))
#print(dj.copy(exclude_info = True))
#print(dj.structure)
