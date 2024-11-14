import os
from openai import OpenAI

# Utwórz instancję klienta OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def read_article(file_path):
    """Odczytuje zawartość pliku tekstowego."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def generate_html(article_content):
    """Funkcja do generowania HTML z użyciem OpenAI. Technika C.R.E.A.T.E"""
    prompt = ("""
            Mam zadanie polegające na przekształceniu artykułu tekstowego w kod HTML z odpowiednią strukturą i elementami wizualnymi.
            Potrzebuję, abyś zamienił poniższy artykuł w kod HTML, dodając odpowiednie tagi HTML. Chciałbym, abyś wstawił miejsca, gdzie mogą pojawić się obrazy, używając tagu <img src="image_placeholder.jpg" alt="Prompt do generowania grafiki"> oraz dodał podpisy pod obrazkami. Ważne jest, aby kod zawierał tylko zawartość do umieszczenia w sekcji <body> (czyli bez znaczników <html>, <head> i <body>).
            Przykład: Artykuł mówi o "Zalety zdrowego stylu życia". W wygenerowanym kodzie HTML powinno się pojawić coś takiego:
            <h1>Zalety zdrowego stylu życia</h1>
            <p>...treść artykułu...</p>
            <img src="image_placeholder.jpg" alt="Prompt do generowania grafiki">
            <figcaption>Wizualizacja zdrowego stylu życia</figcaption>
            Proszę zamienić artykuł w kod HTML, wstawiając odpowiednie tagi i obrazki tam, gdzie to zasadne. Nie dodawaj CSS ani JavaScript.
            Ostateczny kod HTML powinien zawierać tylko zawartość do umieszczenia w sekcji <body>, z tagami <h1>, <p>, <img> oraz <figcaption>, odpowiednio sformatowanymi.
            Oczekuję, że otrzymam HTML, który mogę bezpośrednio wkleić do pliku .html, gotowy do użycia w przeglądarce. Obrazki powinny być oznaczone tagiem <img> z odpowiednimi atrybutami alt.
            """
        f"Oto artykuł:\n{article_content}"
    )
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def save_html(content, output_path):
    """Zapisuje wygenerowany HTML do pliku."""
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(content)

def main():
    # Określenie ścieżki folderu roboczego
    base_dir = os.path.expanduser("~/Desktop/zadanie rekrutacyjne")

    # Ścieżka do pliku artykułu
    article_path = os.path.join(base_dir, "article.txt")

    # Ścieżka do zapisu pliku HTML
    output_path = os.path.join(base_dir, "article.html")
    
    # Odczytaj artykuł
    article_content = read_article(article_path)
    
    # Wygeneruj HTML z użyciem API OpenAI
    html_content = generate_html(article_content)
    
    # Zapisz wygenerowany HTML do pliku
    save_html(html_content, output_path)
    print(f"HTML wygenerowany i zapisany w: {output_path}")

if __name__ == "__main__":
    main()
