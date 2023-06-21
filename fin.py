import openai
import os
import csv

openai.api_key = os.getenv("KLUCZ_API")
file_path = "DataSet.csv"
row_number = 2

with open(file_path, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    for i, row in enumerate(csvreader, 1):
        if i == row_number:
            print(row)
            row_number += 1
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user",
                     "content": "Powiedz jednym słowem.Do ktorej z tych kategorii(Aborcja, Alkohol, Anoreksja, Aplikacje mobilne, Bankowość, Broń / Militaria, Czat, Gry online, Hazard, Kibole, Malware/Spyware/Hacking, Memy / Obrazki, Nacjonalizm, Narkotyki, Poczta online, Pornografia, Przekleństwa, Przemoc, Samookaleczenie, Sekty, Serwisyspołecznościowe, Tatuaże, Tytoń, Udostępnianie plików, Usługi, Wiadomości, Wyszukiwarki, Zakupy) przypisałbyś ta strone" + ', '.join(row) + "?"}
                ]
            )
            response = completion.choices[0].message['content']
            print(response)
            print("Tokens used:", completion['usage']['total_tokens'])
