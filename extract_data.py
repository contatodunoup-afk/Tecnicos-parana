import openpyxl
import json

# Carregar o arquivo Excel
wb = openpyxl.load_workbook('dados fundepar tecnicos.xlsx')
ws = wb.active

data = []
for idx, row in enumerate(ws.iter_rows(min_row=2, values_only=True)):
    if row[0] is None:  # Para quando encontrar linhas vazias
        break
    
    # Extrair dados importantes
    item = {
        "name": row[3] if row[3] else "N/A",  # name (coluna 4)
        "city": row[14] if row[14] else "N/A",  # city (coluna 15)
        "state": row[13] if row[13] else "BR",  # state (coluna 14)
        "phone": row[4] if row[4] else "",  # phone (coluna 5)
        "code": str(row[5]) if row[5] else "",  # code_prp (coluna 6)
        "lat": float(row[28]) if row[28] else 0,  # latitude (coluna 29)
        "lng": float(row[29]) if row[29] else 0   # longitude (coluna 30)
    }
    data.append(item)

# Salvar como JSON
with open('data_fundepar.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Total de registros: {len(data)}")
print("\nDados extraídos:")
print(json.dumps(data, ensure_ascii=False, indent=2))
