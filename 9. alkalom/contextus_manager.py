"""
Kontextus manager - Context manager

Bizonyos típusú resource-okat managel 
    -> Managel - pl. fileműveletnél ő automatikusan le fogja zárni a megnyitott file-t

Mit nevezünk resource-nak?
Olyan objektumok, amelyek valamilyen külső tényezővel / dologgal végeznek iterációt.
Tipikus reasource-ok: pl. megnyitott file objektumokt, adatbázis kapcsolat, API-ok stb.

Context manager:

(code block)
with resource_definition as resoure_alias_name:
    műveletek a resourcal


"""
file_path = r"C:\WORK\Prooktatas\2024-november\9. alkalom\test_file.txt"

data = "ez csak egy teszt adat"
with open(file_path, "w", encoding="utf-8") as f:
    f.write(data)
