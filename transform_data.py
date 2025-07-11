import pandas as pd
import numpy as np

def delete_rows_by_quantity(df):
    # Normaliza columnas
    df["Cantidad"] = pd.to_numeric(df["Cantidad"], errors="coerce").fillna(0)
    df["Producto"] = df["Producto"].astype(str).str.strip()

    # Filtro: Cantidad distinta de 0 y Producto no vacío ni "0"
    df = df[
        (df["Cantidad"] != 0) &
        (df["Producto"] != "") &
        (df["Producto"].str.lower() != "nan") &
        (df["Producto"] != "0")  # Producto no sea "0"
    ]

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

def clean_empty_rows_overall(df):
    col = "APELLIDOS Y NOMBRE"

    # Buscar índice de la primera fila vacía en la columna APELLIDOS Y NOMBRE
    vacio_idx = df[col].apply(lambda x: pd.isna(x) or str(x).strip() == "").idxmax()

    # Si no hay ningún vacío, no elimines nada
    if (pd.isna(df.at[vacio_idx, col]) or str(df.at[vacio_idx, col]).strip() == ""):
        df = df.loc[:vacio_idx - 1]  # conservar solo filas antes del vacío

    # Si no hay vacíos en la columna, no cambia nada
    return df.reset_index(drop=True)


def transform_data_camana(camana):
    camana = clean_empty_rows(camana)

    camana = fill_name(camana)

    camana = clean_empty_rows_overall(camana)

    camana = fill_empty_cells(camana)
    
    camana = melt_dataframe(camana)

    camana = delete_rows_by_quantity(camana)

    return camana

def transform_data_pedregal(pedregal):
    pedregal = clean_empty_rows_overall(pedregal)

    pedregal = fill_empty_cells(pedregal)
    
    pedregal = melt_dataframe(pedregal)

    pedregal = delete_rows_by_quantity(pedregal)

    return pedregal

def transform_data_chala(chala):
    chala = clean_empty_rows(chala)

    chala = fill_name(chala)

    chala = clean_empty_rows_overall(chala)

    chala = fill_empty_cells(chala)
    
    chala = melt_dataframe(chala)

    chala = delete_rows_by_quantity(chala)

    return chala