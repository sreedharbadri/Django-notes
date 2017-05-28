#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# and put there a class called ImportHelper(object) in it.
#
# This class will be specially casted so that instead of extending object,
# it will actually extend the class BasicImportHelper()
#
# That means you just have to overload the methods you want to
# change, leaving the other ones inteact.
#
# Something that you might want to do is use transactions, for example.
#
# Also, don't forget to add the necessary Django imports.
#
# This file was generated with the following command:
# manage.py dumpscript address
#
# to restore it, run
# manage.py runscript module_name.this_script_name
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script
import os, sys
from django.db import transaction

class BasicImportHelper(object):

    def pre_import(self):
        pass

    @transaction.atomic
    def run_import(self, import_data):
        import_data()

    def post_import(self):
        pass

    def locate_similar(self, current_object, search_data):
        # You will probably want to call this method from save_or_locate()
        # Example:
        #   new_obj = self.locate_similar(the_obj, {"national_id": the_obj.national_id } )

        the_obj = current_object.__class__.objects.get(**search_data)
        return the_obj

    def locate_object(self, original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        # You may change this function to do specific lookup for specific objects
        #
        # original_class class of the django orm's object that needs to be located
        # original_pk_name the primary key of original_class
        # the_class      parent class of original_class which contains obj_content
        # pk_name        the primary key of original_class
        # pk_value       value of the primary_key
        # obj_content    content of the object which was not exported.
        #
        # You should use obj_content to locate the object on the target db
        #
        # An example where original_class and the_class are different is
        # when original_class is Farmer and the_class is Person. The table
        # may refer to a Farmer but you will actually need to locate Person
        # in order to instantiate that Farmer
        #
        # Example:
        #   if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:
        #       pk_name="name"
        #       pk_value=obj_content[pk_name]
        #   if the_class == StaffGroup:
        #       pk_value=8

        search_data = { pk_name: pk_value }
        the_obj = the_class.objects.get(**search_data)
        #print(the_obj)
        return the_obj


    def save_or_locate(self, the_obj):
        # Change this if you want to locate the object in the database
        try:
            the_obj.save()
        except:
            print("---------------")
            print("Error saving the following object:")
            print(the_obj.__class__)
            print(" ")
            print(the_obj.__dict__)
            print(" ")
            print(the_obj)
            print(" ")
            print("---------------")

            raise
        return the_obj


importer = None
try:
    import import_helper
    # We need this so ImportHelper can extend BasicImportHelper, although import_helper.py
    # has no knowlodge of this class
    importer = type("DynamicImportHelper", (import_helper.ImportHelper, BasicImportHelper ) , {} )()
except ImportError as e:
    # From Python 3.3 we can check e.name - string match is for backward compatibility.
    if 'import_helper' in str(e):
        importer = BasicImportHelper()
    else:
        raise

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

try:
    import dateutil.parser
except ImportError:
    print("Please install python-dateutil")
    sys.exit(os.EX_USAGE)

def run():
    importer.pre_import()
    importer.run_import(import_data)
    importer.post_import()

def import_data():
    # Initial Imports

    # Processing model: address.models.Address_Detail

    from address.models import Address_Detail

    address_address_detail_1 = Address_Detail()
    address_address_detail_1.name = u'ajay'
    address_address_detail_1.email = u'ajay@edu.com'
    address_address_detail_1.gender = u'm'
    address_address_detail_1 = importer.save_or_locate(address_address_detail_1)

    address_address_detail_2 = Address_Detail()
    address_address_detail_2.name = u'chiru'
    address_address_detail_2.email = u'chiru@gmail.com'
    address_address_detail_2.gender = u'm'
    address_address_detail_2 = importer.save_or_locate(address_address_detail_2)

    address_address_detail_3 = Address_Detail()
    address_address_detail_3.name = u'kumar'
    address_address_detail_3.email = u'kumar@edu.com'
    address_address_detail_3.gender = u'm'
    address_address_detail_3 = importer.save_or_locate(address_address_detail_3)

    address_address_detail_4 = Address_Detail()
    address_address_detail_4.name = u'ramu'
    address_address_detail_4.email = u'ramu@edu.com'
    address_address_detail_4.gender = u'm'
    address_address_detail_4 = importer.save_or_locate(address_address_detail_4)

    # Processing model: address.models.New_Course

    from address.models import New_Course

    address_new_course_1 = New_Course()
    address_new_course_1.email = address_address_detail_2
    address_new_course_1.course = u'django'
    address_new_course_1 = importer.save_or_locate(address_new_course_1)

    address_new_course_2 = New_Course()
    address_new_course_2.email = address_address_detail_2
    address_new_course_2.course = u'python'
    address_new_course_2 = importer.save_or_locate(address_new_course_2)

    address_new_course_3 = New_Course()
    address_new_course_3.email = address_address_detail_4
    address_new_course_3.course = u'django'
    address_new_course_3 = importer.save_or_locate(address_new_course_3)

    address_new_course_4 = New_Course()
    address_new_course_4.email = address_address_detail_4
    address_new_course_4.course = u'python'
    address_new_course_4 = importer.save_or_locate(address_new_course_4)

    # Processing model: address.models.Person

    from address.models import Person


    # Processing model: address.models.Place

    from address.models import Place


    # Processing model: address.models.Restaurant

    from address.models import Restaurant


    # Processing model: address.models.Waiter

    from address.models import Waiter


    # Processing model: address.models.Reporter

    from address.models import Reporter


    # Processing model: address.models.Article

    from address.models import Article


    # Processing model: address.models.Publication

    from address.models import Publication


    # Processing model: address.models.Articles

    from address.models import Articles


