from googleapiclient.discovery import build
import random

DEVELOPER_KEY = '' # Pon tu clave de desarrollador
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

# Construye el servicio youtube
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

letters_and_numbers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Desordena la lista de letras y numeros
random.shuffle(letters_and_numbers)

#Coge una letra/numero de forma 'random' de la lista 'letters_and_numbers'
to_search = random.choice(letters_and_numbers)

list_pages_tokens = []
channels = []

# Hace una busqueda
search_response = youtube.search().list(
    q=to_search,
    part='snippet',
    maxResults=50
).execute()

# Consigue los tokens de la siguiente pagina y los almacena en una lista
for i in range(random.randint(0, 50), random.randint(50, 100)):
    search_response = youtube.search().list(
        q=to_search,
        part='snippet',
        maxResults=50,
        pageToken=search_response.get('nextPageToken')
    ).execute()
    nextPageToken = search_response.get('nextPageToken')
    list_pages_tokens.append(nextPageToken)
    print(f"Esta es tu siguiente pagina random: {nextPageToken}")

# Almacena en una variable un token random de la lista de tokens
selected_page_token = random.choice(list_pages_tokens)

# Busca canales dentro del pagina 'random'
search_response = youtube.search().list(
    q=to_search,
    part='snippet',
    maxResults=50,
    pageToken=selected_page_token
).execute()

# Recorre el search response i almacena en una lista el nombre del canal i su id
for search_result in search_response.get('items', []):
    channels.append([search_result['snippet']['channelTitle'], search_result['snippet']['channelId']])

# Selecciona un canal random de la lista de canales
selected_channel = random.choice(channels)

# Imprime el canal 'random' y su link
print(f"El canal random seleccionados es '{selected_channel[0]}', cuyo link es: {'https://www.youtube.com/channel/'+selected_channel[1]}")

# Imprime informacion, com la cantidad de canales que se eligieron, tokens, la letra buscada y el token seleccionado
print(f"Se eligieron entre {len(channels)} canales y se eligio una pagina de entre {len(list_pages_tokens)} paginas")
print(f"La letra buscada es '{busqueda}' y el pagina token elegida es '{selected_page_token}'")
