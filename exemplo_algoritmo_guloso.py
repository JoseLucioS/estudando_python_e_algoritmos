estados_para_abranger = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

estacoes = {}
estacoes["kum"] = set(["id", "nv", "ut"])
estacoes["kdois"] = set(["wa", "id", "mt"])
estacoes["ktres"] = set(["or", "nv", "ca"])
estacoes["kquatro"] = set(["nv", "ut"])
estacoes["kcinco"] = set(["ca", "az"])

estacoes_selecionadas = set()

if __name__ == "__main__":
    while estados_para_abranger:
        melhor_estacao = None
        estados_cobertos = set()
        for estacao, estados in estacoes.items():
            cobertos = estados & estados_para_abranger
            if len(cobertos) > len(estados_cobertos):
                melhor_estacao = estacao
                estados_cobertos = cobertos
        estados_para_abranger -= estados_cobertos
        estacoes_selecionadas.add(melhor_estacao)
    
    print("Estações selecionadas:", estacoes_selecionadas)