def validate_inputs(values):
    for key, val in values.items():
        if not (0 <= val <= 255):
            raise ValueError(f"{key} должно быть в диапазоне 0–255")

def check_point_inside(values):
    return (
        values['R1'] <= values['r'] <= values['R2'] and
        values['G1'] <= values['g'] <= values['G2'] and
        values['B1'] <= values['b'] <= values['B2']
    )

