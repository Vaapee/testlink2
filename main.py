import streamlit as st

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

import requests

response = requests.get('https://api.github.com', params={'foo': 'bar'}, headers={'Accept': 'application/vnd.github+json'}, timeout=5, allow_redirects=False, verify=False, stream=True, cert=None, auth=None, cookies=None, hooks=None, json=None, files=None, data=None, params=None, headers=None, timeout=5, allow_redirects=False, proxies=None,
                         hooks=None, stream=False, verify=True, cert=None, data=None)

print(response.text)


if __name__ == "__ main__":
    app()

