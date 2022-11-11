# Distribution Summary
 A collection of ArcGIS geoprocessing tools and utilities to work with geospatial-temporal data. 
 
# ArcTime TBX

# Truncate Datetime
This tool is a simple geoprocessing scripting tool intended to assist with temporal data preparation by truncating the date time object to set constants for better grouping and aggregation for time space cubes and other analysis methods. If the set times are -1, the current date and time will be used for that parameter.  

# Usage
Use this script with an input date field to create a formated time string based on your needs. 

<table width="100%" border="0" cellpadding="5">
<tbody>
<tr>
<th width="30%">
<b>Parameter</b>
</th>
<th width="50%">
<b>Explanation</b>
</th>
<th width="20%">
<b>Data Type</b>
</th>
</tr>
<tr>
<td class="info">Input_Feature_Class</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>Is the input feature class or table for which a new time field will be added. </SPAN></P></DIV></DIV></DIV><div class="noContent" style="text-align:center; margin-top: -1em">___________________</div><br />
<span style="font-weight: bold">Python Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>Depends on https://docs.python.org/2/library/time.html#time.strftime. </SPAN></P></DIV></DIV></DIV></td>
<td class="info" align="left">Feature Layer</td>
</tr>
<tr>
<td class="info">Date_Time_Field</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>This is the ArcGIS date field that will be used to construct the datetime objects used in the created Pandas data frame. Years allowed by the tool will dependon python version. For example 2.7 cannot handle years before 1900. </SPAN></P></DIV></DIV></DIV><div class="noContent" style="text-align:center; margin-top: -1em">___________________</div><br />
<span style="font-weight: bold">Python Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>Generally the fields are selected from the feature class to be converted into a numpy array, then into a pandas data frame, then back to structured numpy array to be joined based on the object ID. This tool assumes there is an object ID to use to join to.</SPAN></P></DIV></DIV></DIV></td>
<td class="info" align="left">Field</td>
</tr>
<tr>
<td class="info">New_Field_Name</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>This is the name of the new text field that will be added to the feature class and then populated by a new time string based on the format string. If the name already exists, then a unique one will be added. </SPAN></P></DIV></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">String</td>
</tr>
<tr>
<td class="info">Set_Year</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><P><SPAN>This is the year you want to set all the datetimes to for the new field. If it is -1, it will use the current time period determined by the datetime object. </SPAN></P></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Long</td>
</tr>
<tr>
<td class="info">Set_Month</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><P><SPAN>This is the month you want to set all the datetimes to for the new field. If it is -1, it will use the current time period determined by the datetime object. </SPAN></P></DIV><DIV><P><SPAN /></P></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Long</td>
</tr>
<tr>
<td class="info">Set_Day</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><P><SPAN>This is the day you want to set all the datetimes to for the new field. If it is -1, it will use the current time period determined by the datetime object. </SPAN></P></DIV><DIV><P><SPAN /></P></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Long</td>
</tr>
<tr>
<td class="info">Set_Hour</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><P><SPAN>This is the hour you want to set all the datetimes to for the new field. If it is -1, it will use the current time period determined by the datetime object. </SPAN></P></DIV><DIV><P><SPAN /></P></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Long</td>
</tr>
<tr>
<td class="info">Set_Minute</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><P><SPAN>This is the minute you want to set all the datetimes to for the new field. If it is -1, it will use the current time period determined by the datetime object. </SPAN></P></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Long</td>
</tr>
<tr>
<td class="info">Set_Second</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><P><SPAN>This is the second you want to set all the datetimes to for the new field. If it is -1, it will use the current time period determined by the datetime object. </SPAN></P></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Long</td>
</tr>
</tbody>
</table>

# Add Time String Field

This tool is a simple strf time script intended to add a new text field with a formatted string based on the format string input into it. This tool uses pandas to convert and add the new unique field using the arcpy.da extend table function.

# Usage
This tool is intended to provide an easy way to created formatted string fields using the </SPAN><A href="https://docs.python.org/2/library/time.html"><SPAN>strftime function</SPAN></A><SPAN>. 

# Parameters
<table width="100%" border="0" cellpadding="5">
<tbody>
<tr>
<th width="30%">
<b>Parameter</b>
</th>
<th width="50%">
<b>Explanation</b>
</th>
<th width="20%">
<b>Data Type</b>
</th>
</tr>
<tr>
<td class="info">Input_Feature_Class</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><P><SPAN>Is the input feature class or table for which a new time field will be added. </SPAN></P></DIV></DIV><div class="noContent" style="text-align:center; margin-top: -1em">___________________</div><br />
<span style="font-weight: bold">Python Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><P><SPAN>Depends on https://docs.python.org/2/library/time.html#time.strftime. </SPAN></P></DIV></DIV></td>
<td class="info" align="left">Feature Layer</td>
</tr>
<tr>
<td class="info">Date_Time_Field</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><P><SPAN>This is the ArcGIS date field that will be used to construct the datetime objects used in the created Pandas data frame. </SPAN></P></DIV></DIV><div class="noContent" style="text-align:center; margin-top: -1em">___________________</div><br />
<span style="font-weight: bold">Python Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><P><SPAN>Generally the fields are selected from the feature class to be converted into a numpy array, then into a pandas data frame, then back to structured numpy array to be joined based on the object ID. This tool assumes there is an object ID to use to join to.</SPAN></P></DIV></DIV></td>
<td class="info" align="left">Field</td>
</tr>
<tr>
<td class="info">New_Field_Name</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><P><SPAN>This is the name of the new text field that will be added to the feature class and then populated by a new time string based on the format string. If the name already exists, then a unique one will be added. </SPAN></P></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">String</td>
</tr>
<tr>
<td class="info">Format_String</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>The format string determines the output time format. Do not add quotes. </SPAN></P><P><SPAN>Check the documentation </SPAN><A href="https://docs.python.org/2/libarary/time.html"><SPAN>link here for details</SPAN></A><SPAN>. </SPAN></P><P><SPAN>Directive	Meaning	Notes</SPAN></P><P><SPAN>%a	Localeӳ abbreviated weekday name.	 </SPAN></P><P><SPAN>%A	Localeӳ full weekday name.	 </SPAN></P><P><SPAN>%b	Localeӳ abbreviated month name.	 </SPAN></P><P><SPAN>%B	Localeӳ full month name.	 </SPAN></P><P><SPAN>%c	Localeӳ appropriate date and time representation.	 </SPAN></P><P><SPAN>%d	Day of the month as a decimal number [01,31].	 </SPAN></P><P><SPAN>%H	Hour (24-hour clock) as a decimal number [00,23].	 </SPAN></P><P><SPAN>%I	Hour (12-hour clock) as a decimal number [01,12].	 </SPAN></P><P><SPAN>%j	Day of the year as a decimal number [001,366].	 </SPAN></P><P><SPAN>%m	Month as a decimal number [01,12].	 </SPAN></P><P><SPAN>%M	Minute as a decimal number [00,59].	 </SPAN></P><P><SPAN>%p	Localeӳ equivalent of either AM or PM.	(1)</SPAN></P><P><SPAN>%S	Second as a decimal number [00,61].	(2)</SPAN></P><P><SPAN>%U	Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.	(3)</SPAN></P><P><SPAN>%w	Weekday as a decimal number [0(Sunday),6].	 </SPAN></P><P><SPAN>%W	Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.	(3)</SPAN></P><P><SPAN>%x	Localeӳ appropriate date representation.	 </SPAN></P><P><SPAN>%X	Localeӳ appropriate time representation.	 </SPAN></P><P><SPAN>%y	Year without century as a decimal number [00,99].	 </SPAN></P><P><SPAN>%Y	Year with century as a decimal number.	 </SPAN></P><P><SPAN>%Z	Time zone name (no characters if no time zone exists).	 </SPAN></P><P><SPAN>%%	A literal '%' character.	 </SPAN></P><P><SPAN>Notes:</SPAN></P><P><SPAN /></P><P><SPAN>When used with the strptime() function, the %p directive only affects the output hour field if the %I directive is used to parse the hour.</SPAN></P><P><SPAN>The range really is 0 to 61; this accounts for leap seconds and the (very rare) double leap seconds.</SPAN></P><P><SPAN>When used with the strptime() function, %U and %W are only used in calculations when the day of the week and the year are specified.</SPAN></P><P><SPAN>Taken from: http://strftime.org/</SPAN></P></DIV></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">String</td>
</tr>
</tbody>
</table>

# Round DateTime
This tool is a simple geoprocessing scripting tool intended to assist with temporal data preparation by rounding the datetime field to the nearest unit placed in the respective time settings.
# Usage
If the round times are -1, the current date and time will be used for that parameter. The smallest unit to not have a -1 will be used as an indicator that the other units below it should be set to 0.

# Parameters
<table width="100%" border="0" cellpadding="5">
<tbody>
<tr>
<th width="30%">
<b>Parameter</b>
</th>
<th width="50%">
<b>Explanation</b>
</th>
<th width="20%">
<b>Data Type</b>
</th>
</tr>
<tr>
<td class="info">Input_Feature_Class</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>Is the input feature class or table for which a new time field will be added. </SPAN></P></DIV></DIV></DIV><div class="noContent" style="text-align:center; margin-top: -1em">___________________</div><br />
<span style="font-weight: bold">Python Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>Depends on https://docs.python.org/2/library/time.html#time.strftime. </SPAN></P></DIV></DIV></DIV></td>
<td class="info" align="left">Feature Layer</td>
</tr>
<tr>
<td class="info">Date_Time_Field</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>This is the ArcGIS date field that will be used to construct the datetime objects used in the created Pandas data frame. Years allowed by the tool will dependon python version. For example 2.7 cannot handle years before 1900. </SPAN></P></DIV></DIV></DIV><div class="noContent" style="text-align:center; margin-top: -1em">___________________</div><br />
<span style="font-weight: bold">Python Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>Generally the fields are selected from the feature class to be converted into a numpy array, then into a pandas data frame, then back to structured numpy array to be joined based on the object ID. This tool assumes there is an object ID to use to join to.</SPAN></P></DIV></DIV></DIV></td>
<td class="info" align="left">Field</td>
</tr>
<tr>
<td class="info">New_Field_Name</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>This is the name of the new text field that will be added to the feature class and then populated by a new rounded datetime. If the name already exists, then a unique one will be added. </SPAN></P></DIV></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">String</td>
</tr>
<tr>
<td class="info">Rounding_Year</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><P><SPAN>This is the number that the current unit will be rounded to. If the round times are -1, the current date and time will be used for that parameter. The smallest unit to not have a -1 will be used as an indicator that the other units below it should be set to 0. </SPAN></P><UL><LI><P><SPAN>Examples: If Hour =2, the date times will be rounded every 2 hour period, and minutes and seconds would be set to zero. </SPAN></P></LI><LI><P><SPAN>Examples: If Minute= 15, the date times will be rounded to every 15 minute period, and seconds would be set zero. </SPAN></P></LI></UL></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Long</td>
</tr>
<tr>
<td class="info">Rounding_Month</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><P><SPAN>This is the number that the current unit will be rounded to. If the round times are -1, the current date and time will be used for that parameter. The smallest unit to not have a -1 will be used as an indicator that the other units below it should be set to 0. </SPAN></P><UL><LI><P><SPAN>Examples: If Hour =2, the date times will be rounded every 2 hour period, and minutes and seconds would be set to zero. </SPAN></P></LI><LI><P><SPAN>Examples: If Minute= 15, the date times will be rounded to every 15 minute period, and seconds would be set zero. </SPAN></P></LI></UL><DIV><P><SPAN /></P></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Long</td>
</tr>
<tr>
<td class="info">Rounding_Day</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><P><SPAN>This is the number that the current unit will be rounded to. If the round times are -1, the current date and time will be used for that parameter. The smallest unit to not have a -1 will be used as an indicator that the other units below it should be set to 0. </SPAN></P><UL><LI><P><SPAN>Examples: If Hour =2, the date times will be rounded every 2 hour period, and minutes and seconds would be set to zero. </SPAN></P></LI><LI><P><SPAN>Examples: If Minute= 15, the date times will be rounded to every 15 minute period, and seconds would be set zero. </SPAN></P></LI></UL><DIV><P><SPAN /></P></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Long</td>
</tr>
<tr>
<td class="info">Rounding_Hour</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><P><SPAN>This is the number that the current unit will be rounded to. If the round times are -1, the current date and time will be used for that parameter. The smallest unit to not have a -1 will be used as an indicator that the other units below it should be set to 0. </SPAN></P><UL><LI><P><SPAN>Examples: If Hour =2, the date times will be rounded every 2 hour period, and minutes and seconds would be set to zero. </SPAN></P></LI><LI><P><SPAN>Examples: If Minute= 15, the date times will be rounded to every 15 minute period, and seconds would be set zero. </SPAN></P></LI></UL><DIV><P><SPAN /></P></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Long</td>
</tr>
<tr>
<td class="info">Rounding_Minute</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><P><SPAN>This is the number that the current unit will be rounded to. If the round times are -1, the current date and time will be used for that parameter. The smallest unit to not have a -1 will be used as an indicator that the other units below it should be set to 0. </SPAN></P><UL><LI><P><SPAN>Examples: If Hour =2, the date times will be rounded every 2 hour period, and minutes and seconds would be set to zero. </SPAN></P></LI><LI><P><SPAN>Examples: If Minute= 15, the date times will be rounded to every 15 minute period, and seconds would be set zero. </SPAN></P></LI></UL></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Long</td>
</tr>
<tr>
<td class="info">Rounding_Second</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>This is the number that the current unit will be rounded to. If the round times are -1, the current date and time will be used for that parameter. The smallest unit to not have a -1 will be used as an indicator that the other units below it should be set to 0. *Microseconds will be set to 0 by this script, you can edit it further if you really want to round microsecond times. </SPAN></P><UL><LI><P><SPAN>Examples: If Hour =2, the date times will be rounded every 2 hour period, and minutes and seconds would be set to zero. </SPAN></P></LI><LI><P><SPAN>Examples: If Minute= 15, the date times will be rounded to every 15 minute period, and seconds would be set zero. </SPAN></P></LI></UL><P><SPAN /></P></DIV></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Long</td>
</tr>
</tbody>
</table>
</div>

# Temporal Split
This tool is a simple geoprocessing scripting tool intended to split a feature class based on a time field or a start or end time into multiple feature classes based on a start or end time. The bins are based on a time interval and a predetermined start time.
# Usage
This tool is used to split a feature class based on time interval. After being split, iterators in model builder can be used to do aggregation, kernel densities, and other geoprocessing operations.
# Parameters
<table width="100%" border="0" cellpadding="5">
<tbody>
<tr>
<th width="30%">
<b>Parameter</b>
</th>
<th width="50%">
<b>Explanation</b>
</th>
<th width="20%">
<b>Data Type</b>
</th>
</tr>
<tr>
<td class="info">Input_Feature_Class</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>Is the input feature class or table that will be split based on a datetime field. </SPAN></P></DIV></DIV></DIV><div class="noContent" style="text-align:center; margin-top: -1em">___________________</div><br />
<span style="font-weight: bold">Python Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>Uses Python deltatime and datetime libraries. </SPAN></P></DIV></DIV></DIV></td>
<td class="info" align="left">Feature Layer</td>
</tr>
<tr>
<td class="info">Output_Workspace</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><P><SPAN>The output workspace such as a file geodatabase, that will receive the new output feature classes split based on a date field. </SPAN></P></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Workspace</td>
</tr>
<tr>
<td class="info">Start_Time_or_Single_Time_Field</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><P><SPAN>Either the single datetime field or a start field that will be used with an endtime to extract all datetime values that are within the range of the created timebins. </SPAN></P></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Field</td>
</tr>
<tr>
<td class="info">End_Time (Optional) </td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><P><SPAN>This optional field is only used with specific datasets that have an end time field. If there is not end time field chosen, only start time will be used to both construct the time ranges and the final end time. </SPAN></P></DIV></DIV><div class="noContent" style="text-align:center; margin-top: -1em">___________________</div><br />
<span style="font-weight: bold">Python Reference</span><br /><DIV STYLE="text-align:Left;"><P STYLE="font-size:12ptmargin:0 0 0 0;"><SPAN STYLE="font-weight:bold;"><SPAN>if </SPAN></SPAN><SPAN><SPAN>FieldExist(</SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>inFeatureClass</SPAN></SPAN><SPAN><SPAN>, </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>end_time</SPAN></SPAN><SPAN><SPAN>) </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>and </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>end_time</SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>:</SPAN></SPAN><SPAN STYLE="font-weight:bold;" /><SPAN STYLE="font-weight:bold;"><SPAN>    </SPAN></SPAN><SPAN><SPAN>arcPrint(</SPAN></SPAN><SPAN><SPAN>"Using start and end time to grab feature classes whose bins occur within an events "</SPAN></SPAN><SPAN /><SPAN><SPAN>             </SPAN></SPAN><SPAN><SPAN>"start or end time."</SPAN></SPAN><SPAN><SPAN>)</SPAN></SPAN><SPAN /><SPAN><SPAN>    end_time_min, end_time_max </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN><SPAN>get_min_max_from_field(</SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>inFeatureClass</SPAN></SPAN><SPAN><SPAN>, </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>end_time</SPAN></SPAN><SPAN><SPAN>)</SPAN></SPAN><SPAN /><SPAN><SPAN>    start_time_field </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>start_time</SPAN></SPAN><SPAN STYLE="font-style:italic;" /><SPAN STYLE="font-style:italic;"><SPAN>    </SPAN></SPAN><SPAN><SPAN>end_time_field </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>end_time</SPAN></SPAN><SPAN STYLE="font-style:italic;" /><SPAN STYLE="font-style:italic;"><SPAN>    </SPAN></SPAN><SPAN><SPAN>start_time_range </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN><SPAN>start_time_min</SPAN></SPAN><SPAN /><SPAN><SPAN>    end_time_range </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN><SPAN>end_time_max</SPAN></SPAN><SPAN /><SPAN STYLE="font-weight:bold;"><SPAN>else:</SPAN></SPAN><SPAN STYLE="font-weight:bold;" /><SPAN STYLE="font-weight:bold;"><SPAN>    </SPAN></SPAN><SPAN><SPAN>arcPrint(</SPAN></SPAN><SPAN><SPAN>"Using only first datetime start field to construct time bin ranges."</SPAN></SPAN><SPAN><SPAN>)</SPAN></SPAN><SPAN /><SPAN><SPAN>    start_time_field </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>start_time</SPAN></SPAN><SPAN STYLE="font-style:italic;" /><SPAN STYLE="font-style:italic;"><SPAN>    </SPAN></SPAN><SPAN><SPAN>end_time_field </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>start_time</SPAN></SPAN><SPAN STYLE="font-style:italic;" /><SPAN STYLE="font-style:italic;"><SPAN>    </SPAN></SPAN><SPAN><SPAN>start_time_range </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN><SPAN>start_time_min</SPAN></SPAN><SPAN /><SPAN><SPAN>    end_time_range </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN>start_time_max</SPAN></P></DIV></td>
<td class="info" align="left">Field</td>
</tr>
<tr>
<td class="info">Time_Interval</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>The number of seconds, minutes, hours, days, weeks, or years that will represent a single time step. Examples of valid entries for this parameter are 1 Day, 12 Hours, 30 Seconds, or 1 Minute. Units greater than weeks will break the tool, if you need years, put it into day or week equivalents. </SPAN></P></DIV></DIV></DIV><div class="noContent" style="text-align:center; margin-top: -1em">___________________</div><br />
<span style="font-weight: bold">Python Reference</span><br /><DIV STYLE="text-align:Left;"><P STYLE="font-size:12ptmargin:0 0 0 0;"><SPAN STYLE="font-weight:bold;"><SPAN>@</SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>arcToolReport</SPAN></SPAN><SPAN STYLE="font-weight:bold;" /><SPAN STYLE="font-weight:bold;"><SPAN>def </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>construct_time_bin_ranges</SPAN></SPAN><SPAN><SPAN>(</SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>first_time</SPAN></SPAN><SPAN><SPAN>, </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>last_time</SPAN></SPAN><SPAN><SPAN>, </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>time_delta</SPAN></SPAN><SPAN><SPAN>)</SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>:</SPAN></SPAN><SPAN STYLE="font-weight:bold;" /><SPAN STYLE="font-weight:bold;"><SPAN>    </SPAN></SPAN><SPAN><SPAN>temporal_counter </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>first_time</SPAN></SPAN><SPAN STYLE="font-style:italic;" /><SPAN STYLE="font-style:italic;"><SPAN>    </SPAN></SPAN><SPAN><SPAN>total_time_range </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>last_time </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>- </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>first_time</SPAN></SPAN><SPAN STYLE="font-style:italic;" /><SPAN STYLE="font-style:italic;"><SPAN>    </SPAN></SPAN><SPAN><SPAN>bin_count </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN><SPAN>int</SPAN></SPAN><SPAN><SPAN>(np.ceil(total_time_range.total_seconds() </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>/ </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>time_delta</SPAN></SPAN><SPAN><SPAN>.total_seconds()))</SPAN></SPAN><SPAN /><SPAN><SPAN>    nested_time_bin_pairs </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN><SPAN>[]</SPAN></SPAN><SPAN /><SPAN><SPAN>    </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>for </SPAN></SPAN><SPAN><SPAN>bin </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>in </SPAN></SPAN><SPAN><SPAN>range</SPAN></SPAN><SPAN><SPAN>(bin_count)</SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>:</SPAN></SPAN><SPAN STYLE="font-weight:bold;" /><SPAN STYLE="font-weight:bold;"><SPAN>        </SPAN></SPAN><SPAN><SPAN>start_time </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN><SPAN>temporal_counter</SPAN></SPAN><SPAN /><SPAN><SPAN>        end_time </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN><SPAN>temporal_counter </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>+ </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>time_delta</SPAN></SPAN><SPAN STYLE="font-style:italic;" /><SPAN STYLE="font-style:italic;"><SPAN>        </SPAN></SPAN><SPAN><SPAN>nested_time_bin_pairs.append([start_time, end_time])</SPAN></SPAN><SPAN /><SPAN><SPAN>        temporal_counter </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN><SPAN>end_time</SPAN></SPAN><SPAN /><SPAN><SPAN>    </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>return </SPAN></SPAN><SPAN><SPAN>nested_time_bin_pairs</SPAN></SPAN></P><P STYLE="font-size:12ptmargin:0 0 0 0;"><SPAN><SPAN>Lު</SPAN></SPAN></P><DIV><P><SPAN /></P></DIV></DIV></td>
<td class="info" align="left">Time unit</td>
</tr>
<tr>
<td class="info">Bin_Start (Optional) </td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>This is the time you want the binning process to start from. If you place a datetime here, it will replace the minimum time value of the start time field you selected as the bin start time. </SPAN></P><P><SPAN>For example selecting 1990/1/1 12:00:00 AM would start the binning interval at that time period rather than a minimum calculated by the script. </SPAN></P></DIV></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Date</td>
</tr>
<tr>
<td class="info">Compact_Workspace</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><P><SPAN>Optionally will compact the workspace after the tool runs. Will skip on a workspace you can't compact. </SPAN></P></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Boolean</td>
</tr>
</tbody>
</table>
</div>

# Temporal Kernel Density
This geogrocessing script is intended to do batch kernel densities on a feature class based on tool determined time bins. Each bin will be a kernel density raster in a final moasic dataset. 
# Usage
This tool is used to visualize temporal data by splitting a feature class into time bins with make feature layer and then running a kernel density tool on each time bin. After this tool is run mosaic datasets can be used to create animations of change over time. 
# Parameters
<table width="100%" border="0" cellpadding="5">
<tbody>
<tr>
<th width="30%">
<b>Parameter</b>
</th>
<th width="50%">
<b>Explanation</b>
</th>
<th width="20%">
<b>Data Type</b>
</th>
</tr>
<tr>
<td class="info">Input_Feature_Class</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>Is the input feature class or table that will be split based on a datetime field. </SPAN></P></DIV></DIV></DIV><div class="noContent" style="text-align:center; margin-top: -1em">___________________</div><br />
<span style="font-weight: bold">Python Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>Uses Python deltatime and datetime libraries. </SPAN></P></DIV></DIV></DIV></td>
<td class="info" align="left">Feature Class</td>
</tr>
<tr>
<td class="info">Output_Workspace</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>The output workspace such as a file geodatabase, that will receive the new moasic dataset of kernel densities split based on a date field. It is best to use a brand new FGDB. </SPAN></P></DIV></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Workspace</td>
</tr>
<tr>
<td class="info">Output_Time_Table_Name</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><P><SPAN>This is the name of the output table that is built to create the temporal relationship between the output kernel densities and the mosaic footprint. </SPAN></P></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">String</td>
</tr>
<tr>
<td class="info">Start_Time_or_Single_Time_Field</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>Either the single datetime field or a start field that will be used with an endtime to extract all datetime values that are within the range of the created timebins. </SPAN></P></DIV></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Field</td>
</tr>
<tr>
<td class="info">End_Time (Optional) </td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>This optional field is only used with specific datasets that have an end time field. If there is not end time field chosen, only start time will be used to both construct the time ranges and the final end time. </SPAN></P></DIV></DIV></DIV><div class="noContent" style="text-align:center; margin-top: -1em">___________________</div><br />
<span style="font-weight: bold">Python Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN STYLE="font-weight:bold;"><SPAN>if </SPAN></SPAN><SPAN><SPAN>FieldExist(</SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>inFeatureClass</SPAN></SPAN><SPAN><SPAN>, </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>end_time</SPAN></SPAN><SPAN><SPAN>) </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>and </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>end_time</SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>:</SPAN></SPAN><SPAN /><SPAN STYLE="font-weight:bold;"><SPAN /></SPAN><SPAN><SPAN>arcPrint(</SPAN></SPAN><SPAN><SPAN>"Using start and end time to grab feature classes whose bins occur within an events "</SPAN></SPAN><SPAN /><SPAN><SPAN /></SPAN><SPAN><SPAN>"start or end time."</SPAN></SPAN><SPAN><SPAN>)</SPAN></SPAN><SPAN /><SPAN><SPAN>end_time_min, end_time_max </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN><SPAN>get_min_max_from_field(</SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>inFeatureClass</SPAN></SPAN><SPAN><SPAN>, </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>end_time</SPAN></SPAN><SPAN><SPAN>)</SPAN></SPAN><SPAN /><SPAN><SPAN>start_time_field </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>start_time</SPAN></SPAN><SPAN /><SPAN STYLE="font-style:italic;"><SPAN /></SPAN><SPAN><SPAN>end_time_field </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>end_time</SPAN></SPAN><SPAN /><SPAN STYLE="font-style:italic;"><SPAN /></SPAN><SPAN><SPAN>start_time_range </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN><SPAN>start_time_min</SPAN></SPAN><SPAN /><SPAN><SPAN>end_time_range </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN><SPAN>end_time_max</SPAN></SPAN><SPAN /><SPAN STYLE="font-weight:bold;"><SPAN>else:</SPAN></SPAN><SPAN /><SPAN STYLE="font-weight:bold;"><SPAN /></SPAN><SPAN><SPAN>arcPrint(</SPAN></SPAN><SPAN><SPAN>"Using only first datetime start field to construct time bin ranges."</SPAN></SPAN><SPAN><SPAN>)</SPAN></SPAN><SPAN /><SPAN><SPAN>start_time_field </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>start_time</SPAN></SPAN><SPAN /><SPAN STYLE="font-style:italic;"><SPAN /></SPAN><SPAN><SPAN>end_time_field </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>start_time</SPAN></SPAN><SPAN /><SPAN STYLE="font-style:italic;"><SPAN /></SPAN><SPAN><SPAN>start_time_range </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN><SPAN>start_time_min</SPAN></SPAN><SPAN /><SPAN><SPAN>end_time_range </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN>start_time_max</SPAN></P></DIV></DIV></DIV></td>
<td class="info" align="left">Field</td>
</tr>
<tr>
<td class="info">Time_Interval</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>The number of seconds, minutes, hours, days, weeks, or years that will represent a single time step. Examples of valid entries for this parameter are 1 Day, 12 Hours, 30 Seconds, or 1 Minute. Units greater than weeks will break the tool, if you need years, put it into day or week equivalents. </SPAN></P></DIV></DIV></DIV><div class="noContent" style="text-align:center; margin-top: -1em">___________________</div><br />
<span style="font-weight: bold">Python Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN STYLE="font-weight:bold;"><SPAN>@</SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>arcToolReport</SPAN></SPAN><SPAN /><SPAN STYLE="font-weight:bold;"><SPAN>def </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>construct_time_bin_ranges</SPAN></SPAN><SPAN><SPAN>(</SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>first_time</SPAN></SPAN><SPAN><SPAN>, </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>last_time</SPAN></SPAN><SPAN><SPAN>, </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>time_delta</SPAN></SPAN><SPAN><SPAN>)</SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>:</SPAN></SPAN><SPAN /><SPAN STYLE="font-weight:bold;"><SPAN /></SPAN><SPAN><SPAN>temporal_counter </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>first_time</SPAN></SPAN><SPAN /><SPAN STYLE="font-style:italic;"><SPAN /></SPAN><SPAN><SPAN>total_time_range </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>last_time </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>- </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>first_time</SPAN></SPAN><SPAN /><SPAN STYLE="font-style:italic;"><SPAN /></SPAN><SPAN><SPAN>bin_count </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN><SPAN>int</SPAN></SPAN><SPAN><SPAN>(np.ceil(total_time_range.total_seconds() </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>/ </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>time_delta</SPAN></SPAN><SPAN><SPAN>.total_seconds()))</SPAN></SPAN><SPAN /><SPAN><SPAN>nested_time_bin_pairs </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN><SPAN>[]</SPAN></SPAN><SPAN /><SPAN><SPAN /></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>for </SPAN></SPAN><SPAN><SPAN>bin </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>in </SPAN></SPAN><SPAN><SPAN>range</SPAN></SPAN><SPAN><SPAN>(bin_count)</SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>:</SPAN></SPAN><SPAN /><SPAN STYLE="font-weight:bold;"><SPAN /></SPAN><SPAN><SPAN>start_time </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN><SPAN>temporal_counter</SPAN></SPAN><SPAN /><SPAN><SPAN>end_time </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN><SPAN>temporal_counter </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>+ </SPAN></SPAN><SPAN STYLE="font-style:italic;"><SPAN>time_delta</SPAN></SPAN><SPAN /><SPAN STYLE="font-style:italic;"><SPAN /></SPAN><SPAN><SPAN>nested_time_bin_pairs.append([start_time, end_time])</SPAN></SPAN><SPAN /><SPAN><SPAN>temporal_counter </SPAN></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>= </SPAN></SPAN><SPAN><SPAN>end_time</SPAN></SPAN><SPAN /><SPAN><SPAN /></SPAN><SPAN STYLE="font-weight:bold;"><SPAN>return </SPAN></SPAN><SPAN>nested_time_bin_pairs</SPAN></P><P><SPAN /></P></DIV></DIV></DIV></td>
<td class="info" align="left">Time unit</td>
</tr>
<tr>
<td class="info">Bin_Start (Optional) </td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>This is the time you want the binning process to start from. If you place a datetime here, it will replace the minimum time value of the start time field you selected as the bin start time. </SPAN></P><P><SPAN>For example selecting 1990/1/1 12:00:00 AM would start the binning interval at that time period rather than a minimum calculated by the script. </SPAN></P></DIV></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Date</td>
</tr>
<tr>
<td class="info">Population_Field (Optional) </td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><P><SPAN>Values in the population field may be integer or floating point.</SPAN></P><P><SPAN>The options and default behaviors for the field are listed below.</SPAN></P><P><SPAN>Use None if no item or special value will be used and each feature will be counted once.</SPAN></P><P><SPAN>You can use Shape if input features contains Z.</SPAN></P><P><SPAN>Otherwise, the default field is POPULATION. The following conditions may also apply.</SPAN></P><P><SPAN>If there is no POPULATION field, but there is a POPULATIONxxxx field, this is used by default. The xxxx can be any valid character, such as POPULATION6, POPULATION1974, or POPULATIONROADTYPE.</SPAN></P><P><SPAN>If there is no POPULATION field or POPULATIONxxxx field, but there is a POP field, this is used by default.</SPAN></P><P><SPAN>If there is no POPULATION field, POPULATIONxxxx field, or POP field, but there is a POPxxxx field, this is used by default.</SPAN></P><P><SPAN>If there is no POPULATION field, POPULATIONxxxx field, POP field, or POPxxxx field, NONE is used by default.</SPAN></P></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Field</td>
</tr>
<tr>
<td class="info">Cell_Size</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><P><SPAN>The cell size for the output raster dataset.</SPAN></P><P><SPAN>This is the value in the environment if specifically set. If the environment is not set, then cell size is the shorter of the width or height of the output extent in the output spatial reference, divided by 250.</SPAN></P></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Long</td>
</tr>
<tr>
<td class="info">Search_Radius</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><P><SPAN>The search radius within which to calculate density. Units are based on the linear unit of the projection of the output spatial reference.</SPAN></P><P><SPAN>For example, if the units are in metersشo include all features within a one-mile neighborhoodسet the search radius equal to 1609.344 (1 mile = 1609.344 meters).</SPAN></P></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Double</td>
</tr>
<tr>
<td class="info">Area_Scale_Unit_Factor</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><P><SPAN>The desired area units of the output density values.</SPAN></P><P><SPAN>A default unit is selected based on the linear unit of the output spatial reference. You can change this to the appropriate unit if you wish to convert the density output. Values for line density convert the units of both length and area.</SPAN></P><P><SPAN>If no output spatial reference is specified, the output spatial reference will be the same as the input feature class. The default output density units is determined by the linear units of the output spatial reference as follows. If the output linear units are meters, the output area density units will be set to SQUARE_KILOMETERS, outputting square kilometers for point features or kilometers per square kilometers for polyline features. If the output linear units are feet, the output area density units will be set to SQUARE_MILES.</SPAN></P><P><SPAN>If the output units is anything other than feet or meters, the output area density units will be set to SQUARE_MAP_UNITS. That is, the output density units will be the square of the linear units of the output spatial reference. For example, if the output linear units is centimeters, the output area density units will be SQUARE_MAP_UNITS, which would result in square centimeters. If the output linear units is kilometers, the output area density units will be SQUARE_MAP_UNITS, which would result in square kilometers.</SPAN></P><P><SPAN>The available options and their corresponding output density units are the following:</SPAN></P><P><SPAN>SQUARE_MAP_UNITS נFor the square of the linear units of the output spatial reference.</SPAN></P><P><SPAN>SQUARE_MILES נFor miles (U.S.).</SPAN></P><P><SPAN>SQUARE_KILOMETERS נFor kilometers.</SPAN></P><P><SPAN>ACRES ؆or acres (U.S.).</SPAN></P><P><SPAN>HECTARES ؆or hectares.</SPAN></P><P><SPAN>SQUARE_YARDS ؆or yards (U.S.).</SPAN></P><P><SPAN>SQUARE_FEET ؆or feet (U.S.).</SPAN></P><P><SPAN>SQUARE_INCHES נFor inches (U.S.).</SPAN></P><P><SPAN>SQUARE_METERS ؆or meters.</SPAN></P><P><SPAN>SQUARE_CENTIMETERS נFor centimeters.</SPAN></P><P><SPAN>SQUARE_MILLIMETERS נFor millimeters.</SPAN></P></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">String</td>
</tr>
<tr>
<td class="info">Out_Cell_Values</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><P><SPAN>Determines what the values in the output raster represent.</SPAN></P><P><SPAN>DENSITIES ؔhe output values represent the predicted density value. This is the default.</SPAN></P><P><SPAN>EXPECTED_COUNTS ؔhe output values represent the predicted amount of the phenomenon within each cell.Since the cell value is linked to the specified cell size, the resulting raster cannot be resampled to a different cell size and still represent the amount of the phenomenon.</SPAN></P></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">String</td>
</tr>
<tr>
<td class="info">Compact_Workspace</td>
<td class="info" align="left">
<span style="font-weight: bold">Dialog Reference</span><br /><DIV STYLE="text-align:Left;"><DIV><DIV><P><SPAN>Optionally will compact the workspace after the tool runs. Will skip on a workspace you can't compact. </SPAN></P></DIV></DIV></DIV><p><span class="noContent">There is no python reference for this parameter.</span></p></td>
<td class="info" align="left">Boolean</td>
</tr>
</tbody>
</table>
</div>
