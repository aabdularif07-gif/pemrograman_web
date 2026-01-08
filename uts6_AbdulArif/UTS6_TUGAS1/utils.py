def konversi_nilai_ke_label(nilai_angka):
    if nilai_angka >= 85:
        return "A"
    elif nilai_angka >= 80:
        return "A-"
    elif nilai_angka >= 75:
        return "B+"
    elif nilai_angka >= 70:
        return "B"
    elif nilai_angka >= 65:
        return "B-"
    elif nilai_angka >= 60:
        return "C+"
    elif nilai_angka >= 55:
        return "C"
    elif nilai_angka >= 45:
        return "D"
    else:
        return "E"


def konversi_label_ke_bobot(label_huruf):
    label = label_huruf.lower()

    mapping = {
        "a": 4,
        "a-": 3.75,
        "b+": 3.5,
        "b": 3,
        "b-": 2.75,
        "c+": 2.5,
        "c": 2,
        "d": 1,
        "e": 0
    }

    return mapping.get(label)


def hitung_total_sks(sks_list):
    return sum(sks_list)


def hitung_total_nilai(sks_list, nilai_list):
    total = 0
    for sks, nilai in zip(sks_list, nilai_list):
        label = konversi_nilai_ke_label(nilai)
        bobot = konversi_label_ke_bobot(label)
        total += bobot * sks
    return total


def hitung_ips(sks_list, nilai_list):
    total_sks = sum(sks_list)
    total_bobot = hitung_total_nilai(sks_list, nilai_list)
    return total_bobot / total_sks
