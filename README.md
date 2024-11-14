# Aplikacja OpenAI HTML Generator na potrzeby rekrutacji dla Oxido

## Opis

Aplikacja generuje plik HTML na podstawie treści artykułu dostarczonego w formie pliku tekstowego. Korzysta z API OpenAI, aby przetworzyć treść artykułu i wygenerować HTML zgodny z wytycznymi rekrutacyjnymi.

---

## Funkcjonalność

1. Łączy się z API OpenAI.
2. Odczytuje treść artykułu z pliku tekstowego (`artykul.txt`).
3. Wysyła artykuł z promptem do OpenAI w celu wygenerowania struktury HTML.
4. Zapisuje otrzymany kod HTML do pliku `artykul.html`.

Kod HTML zawiera:

- Odpowiednie tagi nagłówków i akapitów.
- Miejsca na grafiki z tagiem `<img>` i atrybutem `alt`.
- Podpisy pod grafikami.
- **Uwaga:** kod HTML nie zawiera tagów `<html>`, `<head>` ani `<body>`, aby spełnić wytyczne zadania.

---

## Wymagania

- Python 3.9
- Klucz API OpenAI

---

## Instalacja

1. Zainstaluj zależne biblioteki (np. OpenAI SDK) za pomocą:
   ```bash
   pip install openai
   ```
2. Skopiuj plik `artykul.txt` do folderu `oxido-zadanie-rekrutacyjne` na Pulpicie.

## Konfiguracja

Przed uruchomieniem ustaw swój klucz API OpenAI:

W Pythonie, zmień wartość `api_key` w pliku `main.py`:

```python
openai.api_key = "TWOJ_KLUCZ_API"
```

---

## Uruchomienie

### Python

1. Uruchom aplikację za pomocą:
   ```bash
   python main.py
   ```

Po uruchomieniu, plik `artykul.html` zostanie wygenerowany w folderze `oxido-zadanie-rekrutacyjne` na Pulpicie.

---

## Struktura Folderu

- `main.py` : Główny plik aplikacji.
- `artykul.txt`: Plik źródłowy z treścią artykułu.
- `artykul.html`: Wygenerowany plik HTML.
- `szablon.html`: Szablon HTML do podglądu pliku artykul.html.
- `README.md`: Dokumentacja aplikacji.
- `.gitignore.md`: Pliki/foldery nie będące uwzględniane w repozytorium github.

---

## Autor

Krzysztof Fila
