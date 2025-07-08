# Eliminar espacios dobles "  " y cambiarlos por un solo espacio " " de la columna Producto
def normalize_producto_spaces(df):
    df["Producto"] = df["Producto"].replace(r'\s+', ' ', regex=True)

    return df

# Corregir nombre de cargo
def replace_attribute_values(ATTRIBUTE, VALUES, df):
    df[ATTRIBUTE] = df[ATTRIBUTE].replace(VALUES)


def normalize_data_camana(CAMANA, camana):
    camana = replace_attribute_values("CARGO", CAMANA['cargo_renames'], camana)

    camana = normalize_producto_spaces(camana)

    camana = replace_attribute_values("Producto", CAMANA["producto_renames"], camana, "")

    return camana