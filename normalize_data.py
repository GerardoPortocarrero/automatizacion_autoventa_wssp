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
    df["Producto"] = df["Producto"].replace(r'\s+', ' ', regex=True)

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