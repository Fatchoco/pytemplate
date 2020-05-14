"""This is docstring for subhelper_b."""
import pytemplate.subfolder_a.subhelper_a as abc


def sub_b01():
    """This is sub_b01 docstring."""
    abc.sub_a01("subfolder_b")
    print("This is subhelper_b's module")
    return "Finish sub_b01"
