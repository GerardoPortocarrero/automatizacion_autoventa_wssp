import pandas as pd
import numpy as np

def delete_rows_by_quantity(df):
    # Solo valores numéricos y diferentes de 0
    df = df[pd.to_numeric(df["Cantidad"], errors="coerce").fillna(0) != 0]

    return df

def melt_dataframe(df):
    # transformar tabla formato reporte autoventa gral
    df = pd.melt(
        df,
        id_vars=["APELLIDOS Y NOMBRE", "CARGO", "Producto"],  # Las columnas que deben permanecer fijas
        var_name="Fecha",                                     # Nombre de la nueva columna para las fechas
        value_name="Cantidad"                                 # Nombre de la nueva columna con los valores
    )

    return df

def fill_empty_cells(df):
    # rellenar 'espacios vacios' o 'punto' con NaN
    df = df.replace(r'^\s*$|^\.$', np.nan, regex=True)

    # rellenar los valores NaN con 0
    df = df.fillna(0)

    return df

def fill_name(df): # Rellenar los valores faltantes en la columna con el valor anterior
    df["APELLIDOS Y NOMBRE"] = df["APELLIDOS Y NOMBRE"].ffill()
    df["CARGO"] = df["CARGO"].ffill()

    return df

def clean_empty_rows(df):
    # Encuentra la primera fila que tenga al menos un valor no nulo
    first_valid_row_index = df['APELLIDOS Y NOMBRE'].first_valid_index()

    # Elimina todas las filas anteriores a esa
    df = df.loc[first_valid_row_index:].reset_index(drop=True)

    return df

def transform_data_camana(camana):
    camana = clean_empty_rows(camana)

    camana = fill_name(camana)

    camana = fill_empty_cells(camana)
    
    camana = melt_dataframe(camana)

    camana = delete_rows_by_quantity(camana)

    return camana