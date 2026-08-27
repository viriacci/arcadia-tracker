# MC Zlecenia Tracker

Desktop app (PySide6) do śledzenia zleceń z itemami/blokami do zebrania w Minecraft.
Karty = zlecenia. W każdej karcie: lista itemów, cel w sztukach i stackach,
pole "zebrano" z przyciskiem sumującym, i wyliczane "pozostało" (szt. + stacki).
Dane zapisują się automatycznie do `orders.json` obok pliku .exe.

## Ikony (ważne)

Nie ma tu żadnych grafik z gry — tekstury Minecrafta należą do Mojang/Microsoft
i nie mogę ich rozpowszechniać. Jeśli chcesz mieć realne ikony przedmiotów:

1. Wypakuj tekstury ze swojego zainstalowanego Minecrafta / resource packa
   (np. z `assets/minecraft/textures/item/` i `.../block/` w pliku .jar wersji gry,
   które i tak masz legalnie).
2. Wrzuć pliki `.png` do folderu `icons/` obok `main.py` (lub obok .exe po zbudowaniu),
   nazwane tak jak item, np. `Iron Ingot.png`.
3. To jest miejsce do rozbudowy w kodzie (`ICONS_DIR` w `main.py`) — obecna wersja
   ma już gotowy folder i ścieżkę, ale UI na razie nie renderuje ikon (tekst-only MVP).
   Daj znać jeśli chcesz, żebym dodał wyświetlanie ikon w tabeli — to prosta zmiana
   (QTableWidgetItem + setIcon(QIcon(path))).

## 1. Instalacja Pythona

Pobierz Python 3.11+ (https://www.python.org/downloads/), przy instalacji
zaznacz "Add Python to PATH".

## 2. Pliki projektu

Rozpakuj folder `mc_tracker/` (main.py, items_data.py, requirements.txt) w dowolnym miejscu.

## 3. Środowisko + zależności

Otwórz cmd/PowerShell w folderze projektu:

```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 4. Test przed kompilacją

```
python main.py
```

Jeśli okno się otwiera i działa — lecimy dalej.

## 5. Kompilacja do .exe (PyInstaller)

```
pyinstaller --noconfirm --onefile --windowed --name "MCZleceniaTracker" ^
  --add-data "items_data.py;." main.py
```

Uwagi:
- `--windowed` = brak konsoli w tle (GUI-only).
- `--onefile` = jeden plik .exe (wolniejszy start, ale wygodny do rozdania).
  Jeśli zależy Ci na szybszym starcie, użyj `--onedir` zamiast `--onefile`.
- Gotowy plik pojawi się w `dist\MCZleceniaTracker.exe`.
- Folder `icons/` (jeśli go używasz) i plik `orders.json` powinny leżeć
  **obok** .exe, nie wewnątrz niego — trzymaj je w folderze `dist/`.

## 6. (opcjonalnie) własna ikonka .exe

Dodaj plik `.ico` i przy kompilacji doklej `--icon="twoja_ikonka.ico"`.

## Struktura zlecenia (dane)

Każdy item w zleceniu ma: nazwę, wielkość stacku (auto-uzupełniana z
`items_data.py`, edytowalna ręcznie), cel (ile potrzeba), i "zebrano"
(sumowane przyciskiem "Dodaj" — wpisujesz ile aktualnie masz w ręku/skrzyni
i doklejasz do licznika, zamiast nadpisywać).

## Rozszerzenia, które mogę dorobić na żądanie
- realne ikony itemów z folderu `icons/`
- export/import zleceń do pliku (współdzielenie z innymi)
- sortowanie/filtrowanie itemów wg "co jeszcze brakuje"
- pasek postępu (progress bar) per zlecenie
