import pandas as pd

# Annahme: Die CSV-Datei hat den Namen 'input.csv'
input_csv = 'input.csv'

# Lese die CSV-Datei in einen DataFrame
df = pd.read_csv(input_csv)

sad_playlist = pd.DataFrame(columns=df.columns)
upbeat_dance = pd.DataFrame(columns=df.columns)
good_mood = pd.DataFrame(columns=df.columns)
not_assigned = pd.DataFrame(columns=df.columns)

# Iteriere über jede Zeile des ursprünglichen DataFrames
for index, row in df.iterrows():
    mood = str(row['Mood']).lower()
    version = str(row['Version']).lower()

    if 'sad' in mood:
        sad_playlist = sad_playlist.append(row)
    elif 'upbeat' in version:
        upbeat_dance = upbeat_dance.append(row)
    elif 'good' in mood:
        good_mood = good_mood.append(row)
    elif pd.isnull(mood) or pd.isnull(version):
        not_assigned = not_assigned.append(row)

def filter_artists(bucket_df):
    artist_count = {}
    for index, row in bucket_df.iterrows():
        for i in range(1, 4):
            artist = str(row[f'Artist {i}'])
            if artist != 'nan':
                artist_count[artist] = artist_count.get(artist, 0) + 1
    filtered_rows = []
    for index, row in bucket_df.iterrows():
        artist_row_count = sum([artist_count.get(str(row[f'Artist {i}']), 0) for i in range(1, 4)])
        if artist_row_count <= 10:
            filtered_rows.append(row)
            for i in range(1, 4):
                artist = str(row[f'Artist {i}'])
                if artist != 'nan':
                    artist_count[artist] = artist_count.get(artist, 0) + 1
    return pd.DataFrame(filtered_rows)

sad_playlist = filter_artists(sad_playlist)
upbeat_dance = filter_artists(upbeat_dance)
good_mood = filter_artists(good_mood)