# POLYMOD | Social Contact Data

This repository is self-contained from original source to downloadable dataset with ETL already performed. ETL changes can be made through PRs, and once a PR pass tests and is merged, the dataset is reproduced. 

A description of the dataset can be found [here](https://cordis.europa.eu/project/id/502084/reporting).

The original datasource can be found [here](https://zenodo.org/record/1215899). 

**SAMPLE SIZE:** 97,250

**FEATURES**

name | type | description
--- | --- | ---
`participant_id` | int | the participant id
`participant_age` | int | age of the participant
`contact_age` | int | age of the contact
`household_size` | int | participant household size
`contact_home` | bool | contact took place in home
`contact_work` | bool | contact took place in work
`contact_school` | bool | contact took place in school
`contact_transport` | bool | contact took place in transport
`contact_leisure` | bool | contact took place in leisure activity
`contact_other` | bool | contact took place in some other situation 
`gender_female` | bool | participant is a female
`gender_male` | bool | participant is a male
`country_be` | bool | participant is in Belgium
`country_de` | bool | participant is in Germany
`country_fi` | bool | participant is in Finland
`country_gb` | bool | participant is in Great Britain
`country_it` | bool | participant is in Italy
`country_nl` | bool | participant is in Netherlands
`country_pl` | bool | participant is in Poland
