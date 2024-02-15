import streamlit as st
import pandas as pd
import io

def process_csv(file, mult):
    df = pd.read_csv(file)
    
    df = df * mult
    
    return df

def main():
    st.title("Spotify Playlist Creation")

    uploaded_file= st.file_uploader("Choose the input csv here", type=["csv"])

    no_artists_per_playlist = st.number_input("How many artists per playlist max?", value=1, step=1, min_value = 1)
    no_original_song_per_playlist = st.number_input("How many original songs per playlist max?", value = 1, step=1, min_value = 1)

    if uploaded_file is not None:
        
        df = process_csv(uploaded_file, mult)

        #to_csv
        csv_as_string = df.to_csv(index=False)
        csv_as_bytes = io.BytesIO(csv_as_string.encode())
        st.download_button("CSV herunterladen", csv_as_bytes, "bearbeitete_daten.csv")

        #to_excel
        excel_as_bytes = io.BytesIO()
        df.to_excel(excel_as_bytes, index=False, sheet_name='Sheet1')
        excel_as_bytes.seek(0)
        st.download_button("Excel herunterladen", excel_as_bytes, "bearbeitete_daten.xlsx")

if __name__ == "__main__":
    main()