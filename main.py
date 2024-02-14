import streamlit as st
import pandas as pd
import io

def process_csv(file, mult):
    df = pd.read_csv(file)
    
    df = df * mult
    
    return df

def main():
    st.title("CSV Datei bearbeiten")

    uploaded_file = st.file_uploader("Datei auswählen", type=["csv"])
    mult = st.number_input("Fehler 1:", value=0, step=1)
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