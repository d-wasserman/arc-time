# ArcTime

A collection of ArcGIS geoprocessing tools and utilities for working with geospatial-temporal data.

## Tools

The `ArcTime.tbx` toolbox contains the following geoprocessing script tools:

- **Truncate DateTime** – Set individual datetime components (year, month, day, etc.) to fixed values across a date field.
- **Round DateTime** – Round a datetime field down to the nearest specified time unit interval.
- **Add Time String Field** – Add a formatted text field derived from a datetime field using a `strftime`-style format string.
- **Temporal Split** – Split a feature class into multiple output feature classes based on time bins.
- **Temporal Kernel Density** – Run batch kernel densities across time bins, producing a time-enabled raster table for use with mosaic datasets.
- **Temporal Mean Center** – Compute mean centers across time bins, outputting a merged, time-enabled feature class.

---

## Tool Details

### Truncate DateTime

Truncates a datetime field by overwriting individual date/time components (year, month, day, hour, minute, second) with fixed values. Useful for grouping and aggregating data for space-time cubes and other temporal analyses. Set any component to `-1` to preserve the original value from each record.

**Parameters**

| Parameter | Description | Data Type |
|---|---|---|
| Input_Feature_Class | The input feature class or table to which the new truncated datetime field will be added. | Feature Layer |
| Date_Time_Field | The existing ArcGIS date field used to populate the new datetime values. Requires an Object ID field for joining results. | Field |
| New_Field_Name | Name for the new date field. If the name already exists, a unique name will be generated automatically. | String |
| Set_Year | Year to assign to all records. Use `-1` to keep each record's original year. | Long |
| Set_Month | Month to assign to all records. Use `-1` to keep each record's original month. | Long |
| Set_Day | Day to assign to all records. Use `-1` to keep each record's original day. | Long |
| Set_Hour | Hour to assign to all records. Use `-1` to keep each record's original hour. | Long |
| Set_Minute | Minute to assign to all records. Use `-1` to keep each record's original minute. | Long |
| Set_Second | Second to assign to all records. Use `-1` to keep each record's original second. | Long |

---

### Add Time String Field

Adds a new text field to a feature class populated with a formatted datetime string derived from an existing date field. Uses Python's [`strftime`](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) format codes. See [strftime.org](http://strftime.org/) for a format string reference.

**Parameters**

| Parameter | Description | Data Type |
|---|---|---|
| Input_Feature_Class | The input feature class or table to which the new text field will be added. | Feature Layer |
| Date_Time_Field | The existing ArcGIS date field used to generate the formatted string. Requires an Object ID field for joining results. | Field |
| New_Field_Name | Name for the new text field. If the name already exists, a unique name will be generated automatically. | String |
| Format_String | A `strftime`-style format string defining the output format (e.g., `%Y-%m-%d`, `%H:%M`). Do not include quotes. | String |

**Common format directives**

| Directive | Meaning |
|---|---|
| `%Y` | Year with century (e.g., 2024) |
| `%y` | Year without century (e.g., 24) |
| `%m` | Month as zero-padded decimal [01–12] |
| `%d` | Day of month as zero-padded decimal [01–31] |
| `%H` | Hour (24-hour clock) [00–23] |
| `%I` | Hour (12-hour clock) [01–12] |
| `%M` | Minute [00–59] |
| `%S` | Second [00–61] |
| `%A` | Locale's full weekday name |
| `%B` | Locale's full month name |
| `%p` | Locale's AM or PM |
| `%%` | A literal `%` character |

---

### Round DateTime

Rounds a datetime field down to the nearest interval for a given time unit. The smallest non-`-1` parameter determines the rounding unit; all smaller units are set to zero.

**Examples:**
- `Rounding_Hour = 2` → rounds to every 2-hour period; minutes and seconds set to zero.
- `Rounding_Minute = 15` → rounds to every 15-minute period; seconds set to zero.

**Parameters**

| Parameter | Description | Data Type |
|---|---|---|
| Input_Feature_Class | The input feature class or table to which the new rounded datetime field will be added. | Feature Layer |
| Date_Time_Field | The existing ArcGIS date field. Requires an Object ID field for joining results. | Field |
| New_Field_Name | Name for the new date field. If the name already exists, a unique name will be generated automatically. | String |
| Rounding_Year | Rounding interval for years. Use `-1` to preserve the original value. | Long |
| Rounding_Month | Rounding interval for months. Use `-1` to preserve the original value. | Long |
| Rounding_Day | Rounding interval for days. Use `-1` to preserve the original value. | Long |
| Rounding_Hour | Rounding interval for hours. Use `-1` to preserve the original value. | Long |
| Rounding_Minute | Rounding interval for minutes. Use `-1` to preserve the original value. | Long |
| Rounding_Second | Rounding interval for seconds. Use `-1` to preserve the original value. Microseconds are always set to zero. | Long |

---

### Temporal Split

Splits a feature class into multiple output feature classes — one per time bin — based on a start (and optional end) datetime field and a defined time interval. The resulting feature classes can be iterated in ModelBuilder for further geoprocessing.

**Parameters**

| Parameter | Description | Data Type |
|---|---|---|
| Input_Feature_Class | The input feature class to be split by time bins. | Feature Layer |
| Output_Workspace | The output geodatabase or folder where the split feature classes will be saved. | Workspace |
| Start_Time_or_Single_Time_Field | The datetime field to use for binning. Used as both start and end if no end time field is provided. | Field |
| End_Time *(Optional)* | An optional end datetime field for datasets with event duration. If omitted, only the start time field is used. | Field |
| Time_Interval | The size of each time bin. Examples: `1 Day`, `12 Hours`, `30 Seconds`, `1 Minute`. Units larger than weeks are not supported — convert to days or weeks instead. | String |
| Bin_Start *(Optional)* | Override the bin start time. If provided, binning begins from this datetime rather than the minimum value in the start time field. | Date |
| Compact_Workspace | If checked, compacts the output workspace after the tool completes (geodatabases only). | Boolean |

---

### Temporal Kernel Density

Runs batch kernel densities on a feature class across tool-generated time bins. Each bin produces a kernel density raster. A temporal record table is created in the output workspace linking each raster to its corresponding time bin for use with mosaic datasets and time-based animations.

**Parameters**

| Parameter | Description | Data Type |
|---|---|---|
| Input_Feature_Class | The input point feature class. | Feature Layer |
| Output_Workspace | A geodatabase workspace to store output rasters and the temporal record table. A geodatabase is required for mosaic dataset creation; a folder workspace stores raw rasters only. | Workspace |
| Output_Table_Name | Name for the output temporal record table that links rasters to their time bins. | String |
| Start_Time_or_Single_Time_Field | The datetime field used for binning. Used as both start and end if no end time field is provided. | Field |
| End_Time *(Optional)* | An optional end datetime field for datasets with event duration. | Field |
| Time_Interval | The size of each time bin (e.g., `1 Day`, `6 Hours`). | String |
| Bin_Start *(Optional)* | Override the bin start time. | Date |
| Population_Field | Optional field to use as kernel density population weight. Leave blank or set to `NONE` to use point count. | Field |
| Cell_Size | Output raster cell size. | Double |
| Search_Radius | Kernel density search radius. | Double |
| Area_Unit_Scale_Factor | The area unit for density output (e.g., `SQUARE_MILES`). | String |
| Out_Cell_Values | Output cell value type: `DENSITIES` or `EXPECTED_COUNTS`. | String |
| Compact_Workspace | If checked, compacts the output workspace after the tool completes. | Boolean |

---

### Temporal Mean Center

Computes mean centers across tool-generated time bins on a feature class. Outputs a single merged, time-enabled feature class with bin metadata (bin number, start/end datetime, and the SQL query used) appended as fields.

**Parameters**

| Parameter | Description | Data Type |
|---|---|---|
| Input_Feature_Class | The input feature class. | Feature Layer |
| Output_Feature_Class | Path for the output merged mean center feature class. | Feature Class |
| Start_Time_or_Single_Time_Field | The datetime field used for binning. | Field |
| End_Time *(Optional)* | An optional end datetime field for event-duration datasets. | Field |
| Time_Interval | The size of each time bin (e.g., `1 Day`, `6 Hours`). | String |
| Bin_Start *(Optional)* | Override the bin start time. | Date |
| Weight_Field *(Optional)* | Optional field for weighted mean center calculation. | Field |
| Case_Field *(Optional)* | Optional field to group records for per-case mean center calculation. | Field |
| Dimension_Field *(Optional)* | Optional numeric field used as a third dimension in the mean center calculation. | Field |

---

## Dependencies

- ArcGIS Desktop 10.4+ or ArcGIS Pro
- Python 3.x
- pandas
- numpy

## Scripts

The `Scripts/` folder contains the Python files backing each tool, as well as `SharedArcNumericalLib.py` — a shared utility library (imported as `san`) used across all tools.

## License

Apache License 2.0 — see [LICENSE](LICENSE) for details.
