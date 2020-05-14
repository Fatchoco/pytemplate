""" This is Python docstring for Main runner file in project """
import pytemplate.helpers as helpers
import pytemplate.subfolder_a.subhelper_a
from pytemplate.subfolder_b import subhelper_b

if __name__ == "__main__":
    print(__file__)
    print("this is main program")
    helpers.helperno01()
    pytemplate.subfolder_a.subhelper_a.sub_a01("main")
    subhelper_b.sub_b01()
