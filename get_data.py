import pandas as pd
from datetime import datetime

# Obtener el nombre de la hoja que coincide con el nombre objetivo
def get_matching_sheet_name(file_path, target_name):
    xls = pd.ExcelFile(file_path)
    for name in xls.sheet_names:
        if name.strip().lower() == target_name.strip().lower():
            return name
    raise ValueError(f"No se encontró una hoja que coincida con '{target_name}'")

# Eliminar todas las columnas excepto las relevantes
def get_relevant_columns(file_properties, df_wssp, MONTH):
    import pandas as pd

    df_wssp.columns = df_wssp.columns.astype(str)

    MES_OBJETIVO = MONTH - 1  # Ej: Julio si MONTH=8
    ANIO_OBJETIVO = 2025

    # Buscar el índice de la última fecha que pertenece al mes/año objetivo
    ultima_fecha_index = -1
    for i, col in enumerate(df_wssp.columns):
        try:
            fecha = pd.to_datetime(col, format="%Y-%m-%d %H:%M:%S", errors="raise")
            if fecha.month == MES_OBJETIVO and fecha.year == ANIO_OBJETIVO:
                ultima_fecha_index = i
        except ValueError:
            pass  # Ignorar columnas que no son fecha

    # Si se encontró al menos una fecha válida, cortar después de ella
    if ultima_fecha_index != -1:
        df_wssp = df_wssp.iloc[:, :ultima_fecha_index + 1]

    # Eliminar columnas irrelevantes
    df_wssp.drop(file_properties['irrelevant_columns'], axis=1, inplace=True, errors="ignore")

    return df_wssp

# Eliminar columna y fila vacia y asignar el encabezado
def adjust_excel_data(df):
    # Eliminar columnas unnamed (vacias)
    df = df.dropna(axis=1, how='all')

    # Tomar la fila 1 como nombres de columnas
    df.columns = df.iloc[1]
    
    # Eliminar las dos primeras filas (la original de encabezado y la fila de nombres)
    df = df.iloc[2:].reset_index(drop=True)

    # Convertir la fecha a string, incluso si los valores son datetime dentro de "object"
    #df['Día'] = df['Día'].apply(lambda x: x.strftime('%d/%m/%Y') if isinstance(x, pd.Timestamp) or isinstance(x, datetime) else str(x))
    
    return df

def get_camana_data(file_properties, MONTH):
    real_sheet_name = get_matching_sheet_name(file_properties['source'], file_properties['sheet_name'])
    df_wssp = pd.read_excel(file_properties['source'], sheet_name=real_sheet_name, header=None)

    df_wssp = adjust_excel_data(df_wssp)

    df_wssp = get_relevant_columns(file_properties, df_wssp, MONTH)

    return df_wssp

def get_pedregal_data(file_properties, MONTH):
    real_sheet_name = get_matching_sheet_name(file_properties['source'], file_properties['sheet_name'])
    df_wssp = pd.read_excel(file_properties['source'], sheet_name=real_sheet_name, header=None)

    df_wssp = adjust_excel_data(df_wssp)

    df_wssp = get_relevant_columns(file_properties, df_wssp, MONTH)

    return df_wssp

def get_chala_data(file_properties, MONTH):
    real_sheet_name = get_matching_sheet_name(file_properties['source'], file_properties['sheet_name'])
    df_wssp = pd.read_excel(file_properties['source'], sheet_name=real_sheet_name, header=None)

    df_wssp = adjust_excel_data(df_wssp)

    df_wssp = get_relevant_columns(file_properties, df_wssp, MONTH)

    return df_wssp