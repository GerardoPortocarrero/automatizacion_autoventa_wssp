# Ordenar orden de columnas
def set_column_order(columns, df):
    df = df[columns]

    return df

# Agregar columna con su sede
def add_sede_column(column_value, df):
    df['Sede'] = column_value

    return df

# Eliminar espacios dobles "  " y cambiarlos por un solo espacio " " de la columna Producto
def normalize_producto_spaces(df):
    # Reemplaza múltiples espacios internos por uno solo
    df["Producto"] = df["Producto"].replace(r'\s+', ' ', regex=True)
    
    # Elimina espacios al inicio y final del string
    df["Producto"] = df["Producto"].str.strip()

    return df

# Corregir nombre de cargo
def replace_attribute_values(ATTRIBUTE, VALUES, df):
    df[ATTRIBUTE] = df[ATTRIBUTE].replace(VALUES)

    return df

def normalize_data_camana(CAMANA, camana):
    camana = replace_attribute_values("CARGO", CAMANA['cargo_renames'], camana)

    camana = normalize_producto_spaces(camana)

    camana = replace_attribute_values("Producto", CAMANA["producto_renames"], camana)

    camana = add_sede_column(CAMANA['name'], camana)

    camana = set_column_order(CAMANA['relevant_columns'], camana)

    return camana

def normalize_data_pedregal(PEDREGAL, pedregal):
    pedregal = replace_attribute_values("CARGO", PEDREGAL['cargo_renames'], pedregal)

    pedregal = normalize_producto_spaces(pedregal)

    pedregal = replace_attribute_values("Producto", PEDREGAL["producto_renames"], pedregal)

    pedregal = add_sede_column(PEDREGAL['name'], pedregal)

    pedregal = set_column_order(PEDREGAL['relevant_columns'], pedregal)

    return pedregal

def normalize_data_chala(CHALA, chala):
    chala = replace_attribute_values("CARGO", CHALA['cargo_renames'], chala)

    chala = normalize_producto_spaces(chala)

    chala = replace_attribute_values("Producto", CHALA["producto_renames"], chala)

    chala = add_sede_column(CHALA['name'], chala)

    chala = set_column_order(CHALA['relevant_columns'], chala)

    return chala