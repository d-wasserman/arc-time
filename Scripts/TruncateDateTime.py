# Name: TruncateDateTime.py
# Purpose: Will take a selected datetime field and will truncate it to chosen values for each of the chosen sub dates.
# Author: David Wasserman
# Last Modified: 2/7/2018
# Copyright: David Wasserman
# Python Version:   2.7-3.1
# ArcGIS Version: 10.4 (Pro)
# --------------------------------
# Copyright 2016 David J. Wasserman
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# --------------------------------
# Import Modules
import os, arcpy, datetime
import pandas as pd
import SharedArcNumericalLib as san


# Function Definitions
@san.arc_tool_report
def IfValueTargetReturnAlt(value, alternative, target=None):
    """If value is not target (depending on parameters), return alternative."""
    if value is not target or value != target:
        return value
    else:
        return alternative


@san.arc_tool_report
def assign_new_datetime(datetime_obj, year, month, day, hour, minute, second, microsecond=0, original_dt_target=-1):
    """Will assign a new date time within an apply function based on the type of object present. Starts with asking
    for forgiveness rather than permission to get original object properties, then uses isinstance to the appropriate
    datetime object to return."""
    try:
        new_year = IfValueTargetReturnAlt(year, datetime_obj.year, original_dt_target)
        new_month = IfValueTargetReturnAlt(month, datetime_obj.month, original_dt_target)
        new_day = IfValueTargetReturnAlt(day, datetime_obj.day, original_dt_target)
    except:
        pass
    try:
        new_hour = IfValueTargetReturnAlt(hour, datetime_obj.hour, original_dt_target)
        new_minute = IfValueTargetReturnAlt(minute, datetime_obj.minute, original_dt_target)
        new_second = IfValueTargetReturnAlt(second, datetime_obj.second, original_dt_target)
        new_microsecond = IfValueTargetReturnAlt(microsecond, datetime_obj.microsecond, original_dt_target)
    except:
        pass
    try:
        if isinstance(datetime_obj, datetime.datetime):
            return datetime.datetime(year=new_year, month=new_month, day=new_day, hour=new_hour, minute=new_minute,
                                     second=new_second, microsecond=new_microsecond)
        elif isinstance(datetime_obj, datetime.date):
            return datetime.date(year=new_year, month=new_month, day=new_day)
        elif isinstance(datetime_obj, datetime.time):
            return datetime.time(hour=new_hour, minute=new_minute, second=new_second, microsecond=new_microsecond)
        else:  # If it is something else,send back max datetime.
            return datetime.date.min
    except:
        return datetime.date.min


def truncate_date_time(in_fc, input_field, new_field_name, set_year=None, set_month=None, set_day=None, set_hour=None,
                       set_minute=None, set_second=None, set_microsecond=None):
    """ This function will take in an feature class, and use pandas/numpy to truncate a date time so that the
     passed date-time attributes are set to a target."""
    try:
        # arc_print(pd.__version__) Does not have dt lib.
        arcpy.env.overwriteOutput = True
        desc = arcpy.Describe(in_fc)
        workspace = os.path.dirname(desc.catalogPath)
        col_new_field = arcpy.ValidateFieldName(san.create_unique_field_name(new_field_name, in_fc), workspace)
        san.add_new_field(in_fc, col_new_field, "DATE")
        OIDFieldName = arcpy.Describe(in_fc).OIDFieldName
        san.arc_print("Creating Pandas Dataframe from input table.")
        query = "{0} {1} {2}".format(arcpy.AddFieldDelimiters(in_fc, input_field), "is NOT", "NULL")
        fcDataFrame = san.arcgis_table_to_dataframe(in_fc, [input_field, col_new_field], query)
        JoinField = arcpy.ValidateFieldName("DFIndexJoin", workspace)
        fcDataFrame[JoinField] = fcDataFrame.index
        try:
            san.arc_print("Creating new date-time column based on field {0}.".format(str(input_field)), True)
            fcDataFrame[col_new_field] = fcDataFrame[input_field].apply(
                lambda dt: assign_new_datetime(dt, set_year, set_month, set_day, set_hour, set_minute, set_second,
                                               set_microsecond)).astype(datetime.datetime)
            del fcDataFrame[input_field]
        except Exception as e:
            del fcDataFrame[input_field]
            san.arc_print(
                "Could not process datetime field. "
                "Check that datetime is a year appropriate to your python version and that "
                "the time format string is appropriate.")
            san.arc_print(e.args[0])
            pass

        san.arc_print("Exporting new time field dataframe to structured numpy array.", True)
        finalStandardArray = fcDataFrame.to_records()
        san.arc_print("Joining new date-time field to feature class.", True)
        arcpy.da.ExtendTable(in_fc, OIDFieldName, finalStandardArray, JoinField, append_only=False)
        san.arc_print("Delete temporary intermediates.")
        del fcDataFrame, finalStandardArray
        san.arc_print("Script Completed Successfully.", True)


    except arcpy.ExecuteError:
        arcpy.AddError(arcpy.GetMessages(2))
    except Exception as e:
        arcpy.AddError(e.args[0])

        # End do_analysis function


# This test allows the script to be used from the operating
# system command prompt (stand-alone), in a Python IDE,
# as a geoprocessing script tool, or as a module imported in
# another script
if __name__ == '__main__':
    # Define Inputs
    FeatureClass = arcpy.GetParameterAsText(0)
    InputField = arcpy.GetParameterAsText(1)
    NewTextFieldName = arcpy.GetParameterAsText(2)
    SetYear = arcpy.GetParameter(3)
    SetMonth = arcpy.GetParameter(4)
    SetDay = arcpy.GetParameter(5)
    SetHour = arcpy.GetParameter(6)
    SetMinute = arcpy.GetParameter(7)
    SetSecond = arcpy.GetParameter(8)
    SetMicroSecond = arcpy.GetParameter(9)
    truncate_date_time(FeatureClass, InputField, NewTextFieldName, SetYear, SetMonth, SetDay, SetHour, SetMinute,
                       SetSecond, SetMicroSecond)
