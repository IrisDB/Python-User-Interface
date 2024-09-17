# Python User Interface

MoveApps

Github repository: *github.com/IrisDB/Python-User-Interface*

## Description
*Enter here the short description of the App that might also be used when filling out the description during App submission to MoveApps. This text is directly presented to Users that look through the list of Apps when compiling Workflows.*

## Documentation
*Enter here a detailed description of your App. What is it intended to be used for. Which steps of analyses are performed and how. Please be explicit about any detail that is important for use and understanding of the App and its outcomes. You might also refer to the sections below.*

### Application scope
#### Generality of App usability
This App was developed for any taxonomic group. 

#### Required data properties
*State here the required and/or optimal data properties for this App to perform properly.*

*Examples:*

This App is only applicable to data that reflect range resident behavior. 

The data should have a fix rate of at least 1 location per 30 minutes. 

The App should work for any kind of (location) data.

### Input type
`MovingPandas.TrajectoryCollection`

### Output type
`MovingPandas.TrajectoryCollection`

### Artefacts
*If the App creates artefacts (e.g. csv, pdf, jpeg, shapefiles, etc), please list them here and describe each.*

*Example:* `rest_overview.csv`: csv-file with Table of all rest site properties

### Settings 
*Please list and define all settings/parameters that the App requires to be set by the App user, if necessary including their unit. Please first state the Setting name the user encounters in the Settings menu defined in the appspecs.json, and between brackets the argument used in the Python code to be able to identify it quickly in the code if needed.*

*Example:* `Radius of resting site` (radius): Defined radius the animal has to stay in for a given duration of time for it to be considered resting site. Unit: `metres`.

### Changes in output data
This App passes on data for individuals that were selected in the user interface.

### Most common errors
*Please describe shortly what most common errors of the App can be, how they occur and best ways of solving them.*

### Null or error handling
*Please indicate for each setting as well as the input data which behaviour the App is supposed to show in case of errors or NULL values/input. Please also add notes of possible errors that can happen if settings/parameters are improperly set and any other important information that you find the user should be aware of.*

*Example:* **Setting `radius`:** If no radius AND no duration are given, the input data set is returned with a warning. If no radius is given (NULL), but a duration is defined then a default radius of 1000m = 1km is set. 
