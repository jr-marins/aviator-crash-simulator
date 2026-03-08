# 🚀 Aviator Crash Simulator

Simulador de jogo estilo **Crash (Aviator)** desenvolvido para demonstrar conceitos de **backend, RNG (Random Number Generation) e arquitetura de aplicações web** usando Python.

O projeto simula a lógica de um jogo de apostas onde um multiplicador cresce aleatoriamente e o jogador precisa definir um **cashout automático** para obter lucro.

Este projeto surgiu por **curiosidade técnica sobre como plataformas de jogos de azar funcionam internamente**, e foi desenvolvido como forma de **praticar desenvolvimento backend, simulação de algoritmos probabilísticos e organização de aplicações web**.

---

# 🧠 Conceitos Demonstrados

* Separação de responsabilidades (Engine / Routes / Interface)
* RNG (Random Number Generation)
* Simulação estatística
* Controle de estado com sessão
* Estrutura de projeto web
* Testes básicos de lógica

---

# 🛠️ Tecnologias Utilizadas

* Python
* Flask
* HTML
* CSS
* Jinja2
* Virtual Environment (venv)

---

# 📂 Estrutura do Projeto

```
aviator-crash-simulator
│
├── app
│   ├── engine.py
│   ├── routes.py
│   └── __init__.py
│
├── templates
│   └── index.html
│
├── static
│   └── style.css
│
├── tests
│   └── test_engine.py
│
├── run.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ▶️ Como Executar o Projeto

### 1️⃣ Clonar o repositório

```
git clone https://github.com/seu-usuario/aviator-crash-simulator.git
cd aviator-crash-simulator
```

---

### 2️⃣ Criar ambiente virtual

```
python -m venv venv
```

Ativar:

Windows

```
venv\Scripts\activate
```

Linux / Mac

```
source venv/bin/activate
```

---

### 3️⃣ Instalar dependências

```
pip install -r requirements.txt
```

---

### 4️⃣ Rodar aplicação

```
python run.py
```

Abrir no navegador:

```
http://127.0.0.1:5000
```

---

# 🎮 Funcionalidades

* Definir saldo inicial
* Escolher valor da aposta
* Definir multiplicador de cashout
* Simular rodada
* Atualização dinâmica do saldo
* Resultado da rodada exibido em tempo real

---

# 📊 Lógica do Multiplicador

O multiplicador é gerado utilizando um RNG simplificado:

```
multiplicador = 0.99 / random()
```

Este modelo simula a vantagem matemática da casa.

---

# 🧪 Testes

O projeto inclui testes simples para validar a lógica do motor de apostas.

```
pytest
```

---

# 🚀 Possíveis Melhorias

* Histórico de apostas
* Gráfico de saldo ao longo do tempo
* API REST
* Autenticação de usuários
* Banco de dados
* Animação do gráfico de multiplicador
* Deploy em nuvem

---

# 🎯 Objetivo do Projeto

Este projeto foi desenvolvido com dois objetivos principais:

1. **Praticar desenvolvimento backend com Python**, aplicando conceitos de arquitetura de software, separação de responsabilidades e lógica de negócio.

2. **Explorar tecnicamente como jogos de azar do tipo "crash" funcionam**, entendendo a geração de números aleatórios (RNG), probabilidade e a lógica por trás desses sistemas.

A ideia foi reproduzir uma versão simplificada desse tipo de jogo para fins **educacionais e de estudo de engenharia de software**.

---

# 👨‍💻 Autor

**Marcos Marins**

Estudante de desenvolvimento backend focado em:

* Python
* Engenharia de Software
* Análise de Dados
