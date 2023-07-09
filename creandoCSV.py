import numpy as np
import pandas as pd

def create_csv_file(file_path):

    data = np.array([
        ['Nombre', 'Carrera', 'Año', 'deep_dive_response'],
        ['Abadi Cherem Elias', 'Economía', '2011',''],
        ['Abad Lopez Carlos Adrian', 'Matemáticas Aplicadas', '2002',''],
        ['Miguel Bosé ', 'Economía', '1900','']
    ])

    df = pd.DataFrame(data=data[1:, :], columns=data[0, :])

    df.to_csv(file_path, index=False)


file_path = 'titulados.csv' 
create_csv_file(file_path)