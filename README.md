# NetGuardian

Sistema de monitoramento de redes e informações do sistema.

## Funcionalidades
- Exibe hostname
- Exibe IP local
- Exibe sistema operacional
- Exibe versão do sistema
- Mostra tráfego de rede em tempo real
- Escaneia portas abertas

## Tecnologias
- Python
- Flask
- psutil
- HTML
- CSS
- JavaScript

## Instalação

```bash
git clone https://github.com/maristelagatinhapreta-jpg/-NetGuardian-.git
cd -NetGuardian-
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Execução

```bash
cd dashboard
python app.py
```

Acesse:

```text
http://127.0.0.1:5000
```

## Estrutura do projeto

```text
NetGuardian/
├── dashboard/
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── style.css
│       └── app.js
├── src/
│   ├── monitor.py
│   └── scanner.py
├── tests/
│   └── test_monitor.py
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

## Como usar

1. Inicie a aplicação.
2. Acesse a URL local no navegador.
3. Veja o dashboard com o hostname, IP, sistema e tráfego de rede.

## Futuras melhorias
- monitoramento de CPU e memória
- alertas de rede
- logs automáticos
- exportação de relatórios
- API REST
- autenticação
