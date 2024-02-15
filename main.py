import streamlit as st
import pandas as pd
import io

def process_csv(file):
    df = pd.read_csv(file)
    
    df = df * 2
    
    return df

def main():
    st.title("Spotify Playlist Creation")

    top_col1, top_col2 = st.columns(2)
    with top_col1:
        uploaded_file = st.file_uploader("Choose the input csv here", type=["csv"])

    with top_col2:
        filler_song_file = st.file_uploader("Upload a new filler song file", type=["csv"])

    no_artists_per_playlist = st.number_input("How many artists per playlist max?", value=10, step=1, min_value = 1)
    no_original_song_per_playlist = st.number_input("How many original songs per playlist max?", value = 3, step=1, min_value = 1)

    if uploaded_file is not None:
        
        df = process_csv(uploaded_file)

        #to_csv
        col1, col2, col3 = st.columns(3)

        # Download-Button für die bearbeitete CSV-Datei
        with col1:
            csv_as_string = df.to_csv(index=False)
            csv_as_bytes = io.BytesIO(csv_as_string.encode())
            st.download_button("CSV herunterladen", csv_as_bytes, "bearbeitete_daten.csv")

        # Download-Button für die bearbeitete Excel-Datei
        with col2:
            excel_as_bytes = io.BytesIO()
            df.to_excel(excel_as_bytes, index=False, sheet_name='Sheet1')
            excel_as_bytes.seek(0)
            st.download_button("Excel herunterladen", excel_as_bytes, "bearbeitete_daten.xlsx")

        # Button für das Update der Spotify-Playlist
        with col3:
            if st.button("Update Spotify Playlist"):
                st.success("Spotify playlists successfully updated!")

    if st.button("Look at filler songs"):
        filler_df = pd.read_csv("filler.csv")
        st.dataframe(filler_df)

if __name__ == "__main__":
    main()