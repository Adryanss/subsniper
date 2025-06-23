# 🎯 SUBSNIPER

> Scanner assíncrono de subdomínios com suporte a wordlist massiva  
> Asynchronous subdomain scanner with massive wordlist support

---

## 🚀 Descrição | Description

**SUBSNIPER** é uma ferramenta desenvolvida em Python 3 com foco em performance, capaz de escanear milhões de subdomínios de forma rápida e eficiente utilizando `asyncio` e `httpx`.

**SUBSNIPER** is a Python 3 tool focused on high-performance scanning, capable of handling millions of subdomains quickly and efficiently using `asyncio` and `httpx`.

---

## 📦 Requisitos | Requirements

- Python 3.10+
- httpx

Instale as dependências:

```bash
pip install httpx
pip install syncio

⚙️ Como usar | How to use
python main.py
Digite o domínio desejado (ex: exemplo.com)

A ferramenta irá ler a wordlist_attack.txt

Testa todos os subdomínios usando HTTP e HTTPS

Salva os que responderem com status [200, 301, 403] no arquivo ativos.txt

📁 Exemplo de wordlist | Sample wordlist

Inclui um arquivo wordlistest.txt com alguns subdomínios básicos para teste.

Para usar outra wordlist, basta substituir o arquivo ou editar o caminho no código.

💡 Funcionalidades | Features

    Suporte a milhões de linhas (testado com 8.9M)

    Scanner assíncrono ultra rápido

    Verificação em HTTP e HTTPS

    Semáforo para limitar concorrência

    Salva resultados válidos em ativos.txt

⚠️ Aviso de responsabilidade | Disclaimer

    Essa ferramenta foi criada apenas para fins educacionais e de pesquisa.
    O uso indevido em domínios sem autorização pode configurar atividade ilegal.
    O autor não se responsabiliza por qualquer uso indevido.

This tool was created for educational and research purposes only.
Unauthorized use on third-party domains may be illegal.
The author is not responsible for any misuse.


👑 Autor | Author

Desenvolvido por @Adryanss

🔥 Powered by Adryanss Underground
