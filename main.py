import streamlit as st
import requests
import time

response = requests.get('https://api.github.com', headers={'Accept': 'application/vnd.github+json'}, timeout=5, allow_redirects=False, verify=True, auth=None, cookies=None, json=None, files=None, proxies=None,
                         hooks=None, stream=False, cert=None, data=None)


print(response.text)

api_url = "https://api.example.com/data"

# Limite de chamadas de API
api_limit = 600

# Tempo entre chamadas (em segundos)
wait_time = 60

# Número total de chamadas feitas
total_calls = 0

# Contador de chamadas no minuto atual
current_minute_calls = 0

def get_data(query_params):
    global total_calls
    global current_minute_calls

    # Verifica se já atingiu o limite de chamadas no minuto atual
    if current_minute_calls >= api_limit / 60:
        print("Atingido o limite de chamadas no minuto atual. Aguarde 60 segundos...")
        time.sleep(60)
        current_minute_calls = 0

    response = requests.get(api_url, params=query_params)

    # Se a resposta for bem-sucedida, incrementa o contador de chamadas
    if response.status_code == 200:
        total_calls += 1
        current_minute_calls += 1

        # Espera o tempo definido entre chamadas, se necessário
        if current_minute_calls > 0 and current_minute_calls % (api_limit / 600) == 0:
            print(f"Esperando {wait_time} segundos para evitar o limite de chamadas de API...")
            time.sleep(wait_time)

        return response.json()

    # Trata erros da resposta
    print(f"Erro ao obter dados: {response.status_code} - {response.text}")
    return None

def link_button(title, url):
    st.markdown(f'[{title}]({url})', unsafe_allow_html=True)

def app():
    st.title("by.ohvapex")

    st.write("Dá uma olhada nisso aqui meu querido")

    st.header("Segue ai que é nois")

    link_button("Youtube", "https://www.youtube.com/VapeeeeS2")
    link_button("Steam", "https://steamcommunity.com/id/ohvape/")
    link_button("Discord Bar do Zé", "https://discord.com/invite/Qruu8yv6zv")
    link_button("NameMC", "https://pt.namemc.com/profile/ohvapex.1")

    st.header("Se quiser conhecer melhor")
    
    link_button("Insta", "https://www.instagram.com/joaotheridiculous/")
    link_button("Twitter/X", "https://twitter.com/kkkkkvapezin")

    st.header ("Vou deixar meu pix aqui pra você, rs")

    link_button("E-mail", "jeitodenoob23@gmail.com")


if __name__ == "__ main__":
    app()

