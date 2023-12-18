# Estudos Práticos de Modelos LLM

Repositório criado para o desafio prático número 8, que pode ser visualizado no repositório da minha faculdade em [PONDERADA8](https://rmnicola.github.io/m8-ec-encontros/sprint4/encontro10/ponderada8)

## Tradutor de Áudio

Os arquivos deste repositório destinam-se à formulação de uma aplicação de tradução que suporta tanto entradas de áudio quanto texto.

### Pré-requisitos
Certifique-se de ter um ambiente OpenIA configurado e ter o python instalado e configurados corretamente no seu sistema. Caso contrário, siga as instruções de instalação nos links a seguir:

- OpenIA: [Tutoria de uso](https://platform.openai.com/docs/quickstart?context=python)


### Passos para Inicialização do Projeto:

. Entre em src:
``` bash
    cd src
```

. Instales todas as depêndecias usadas
``` bash
    pip install -r requiments.txt
```

. Execulte:
``` bash
    python main.py
```

O programa será iniciado com um temporizador, e quando este atingir zero, você terá 5 segundos para gravar seu áudio. Após o término do processamento da sua fala, aparecerá um campo de entrada destinado ao idioma para traduzir seu áudio.


[Video da demostração](https://clipchamp.com/watch/8hBKB2lLtcN)
