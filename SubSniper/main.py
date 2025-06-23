import asyncio
import httpx


wordlist_path = ('Digite a sua wordlist!: ')
with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wdl:


    listas_attack = wdl.read().splitlines()

print('digite o dominio: ')
action = str(input(''))
if not any (action.endswith(ext) for  ext  in ['.com', '.com.br', '.org', '.net']):
    action += '.com'

for subd in listas_attack:
    subd = subd.strip()
    print(f'{subd}.{action}')

subdominios = [f'{subd.strip()}.{action}' for subd in listas_attack]

#----------------------------------------

semaforo = asyncio.Semaphore(100)

async def testa_subdominio(url):
    try:
        async with semaforo:
            async with httpx.AsyncClient() as client:
                resp =  await client.get(url, timeout=5)
            if resp.status_code in [200, 301, 403]:
                return url
    except Exception as e:
        print(f"[ERRO] {url} => {e}")
    return None

    
async def main():
    subdominios = [f"{subd.strip()}.{action}" for subd in listas_attack]
    tasks = []
    for url in subdominios:
        url = url.replace('http://', '').replace('https://', '')
        tasks.append(testa_subdominio(f"http://{url}"))
        tasks.append(testa_subdominio(f"https://{url}"))
    
    resultados = await asyncio.gather(*tasks)

#--------------------------------------------

    with open("ativos.txt", "w") as f:
        vivos = [r for r in resultados if r]
        if not vivos:
            f.write("Nenhum subdominio ativo encontrado.\n")
        for r in vivos:
            print(f" ONLINE: {r}")
            f.write(f"{r}\n")

asyncio.run(main())