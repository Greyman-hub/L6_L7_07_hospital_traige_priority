import math

def parse_vitals_summary(vitals_csv):
    if not isinstance(vitals_csv, str) or not vitals_csv.strip():
        return None

    parts = vitals_csv.split(',')

    if len(parts) != 3:
        return None

    try:
        hr = float(parts[0].strip())
        spo2 = float(parts[1].strip())
        temp = float(parts[2].strip())
    except ValueError:
        return None

    if not all(math.isfinite(x) for x in (hr, spo2, temp)):
        return None

    if hr < 0 or not 0 <= spo2 <= 100 or temp <= 0:
        return None

    critical = hr > 120 or spo2 < 90 or temp > 39.0

    return f"Vitals: HR={hr}, SpO2={spo2}% - {'CRITICAL' if critical else 'STABLE'}"


def compute_patient_bmi(bmi_string):
    if not isinstance(bmi_string, str) or not bmi_string.strip():
        return None

    parts = bmi_string.split('/')

    if len(parts) != 2:
        return None

    try:
        weight = float(parts[0].strip())
        height = float(parts[1].strip())
    except ValueError:
        return None

    if not math.isfinite(weight) or not math.isfinite(height):
        return None

    if weight <= 0 or height <= 0:
        return None

    bmi = weight / (height ** 2)

    return round(bmi, 2)


def assign_ward_bed(allocation_code):
    if not isinstance(allocation_code, str) or not allocation_code.strip():
        return None

    parts = allocation_code.strip().split('-')

    if len(parts) != 2:
        return None

    ward = parts[0].strip().upper()
    bed_str = parts[1].strip()

    ward_names = {
        "ER": "Emergency Room",
        "ICU": "Intensive Care Unit",
        "GEN": "General Ward",
        "PED": "Pediatrics"
    }

    if ward not in ward_names or not bed_str:
        return None

    try:
        bed_num = int(bed_str)
    except ValueError:
        return None

    if bed_num <= 0:
        return None

    return f"{ward_names[ward]} Bed #{bed_num}"


def main():
    print("==== Running parse_vitals_summary ====")
    v_input = input("Enter vitals (HR,SpO2,Temp): ")
    result = parse_vitals_summary(v_input)
    print("Summary:", result if result is not None else "Invalid vitals input")

    print("\n==== Running compute_patient_bmi ====")
    b_input = input("Enter weight/height (e.g. 70/1.75): ")
    result = compute_patient_bmi(b_input)
    print("BMI:", result if result is not None else "Invalid BMI input")

    print("\n==== Running assign_ward_bed ====")
    w_input = input("Enter allocation (e.g. ICU-05): ")
    result = assign_ward_bed(w_input)
    print("Assignment:", result if result is not None else "Invalid allocation code")


if __name__ == "__main__":
    main()
