import wrangle
import pandas as pd

# define the urls for data
base_url = 'https://zenodo.org/record/1215899/files/2008_Mossong_POLYMOD_'

contact_common = 'contact_common.csv?download=1'
participant_common = 'participant_common.csv?download=1'
participant_extra = 'participant_extra.csv?download=1'
household_common = 'hh_common.csv?download=1'

# get the data into dataframes
df_contact_common = pd.read_csv(base_url + contact_common)
df_participant_common = pd.read_csv(base_url + participant_common)
df_participant_extra = pd.read_csv(base_url + participant_extra)
df_household_common = pd.read_csv(base_url + household_common)

# match household id with participant id
household_lookup = df_participant_common[['part_id', 'hh_id']].merge(df_household_common, on='hh_id')
household_lookup = household_lookup[['part_id', 'country', 'hh_size']]

# merge the tables
df_participant_temp = df_participant_common.merge(df_participant_extra, on='part_id')
df = df_contact_common.merge(df_participant_temp, on='part_id')
df = df.merge(household_lookup, on='part_id')

# use estimated age for missing contact age values
estimated_age = (df.cnt_age_est_min + df.cnt_age_est_max) / 2
estimated_age = estimated_age.fillna(0).astype(int)
df['contact_age'] = (df.cnt_age_exact.fillna(0) + estimated_age).astype(int)

# keep these cols
cols = ['part_id',
        'part_gender',
        'contact_age',
        'part_age',
        'country',
        'hh_size',
        'cnt_gender',
        'cnt_home',
        'cnt_work',
        'cnt_school',
        'cnt_transport',
        'cnt_leisure',
        'cnt_otherplace']

df = df[cols]

# convert string label values to multi-label columns
df = wrangle.col_to_multilabel(df, 'part_gender')
df = wrangle.col_to_multilabel(df, 'country')

# drop redundant columns
df.drop(['cnt_gender'], 1, inplace=True)

# use these column names instead
cols = ['participant_id',
        'contact_age',
        'age_group',
        'household_size',
        'contact_home',
        'contact_work',
        'contact_school',
        'contact_transport',
        'contact_leisure',
        'contact_other',
        'gender_female',
        'gender_male',
        'country_be',
        'country_de',
        'country_fi',
        'country_gb',
        'country_it',
        'country_lu',
        'country_nl',
        'country_pl']

# wrap up
df.columns = cols
_age_temp_ = df_participant_common[['part_id', 'part_age']]
df = df.merge(_age_temp_, left_on='participant_id', right_on='part_id')

# final cleanup

_drop_cols_ = ['age_group', 'part_id']

df = wrangle.col_move_place(df, 'part_age')
df = wrangle.col_move_place(df, 'participant_id')
df = wrangle.df_rename_col(df, 'part_age', 'participant_age')

df.drop(_drop_cols_, 1, inplace=True)
df = df.dropna()
df = df.astype(int)

df.to_csv('polymod_social_contact_data.csv', index=False)
