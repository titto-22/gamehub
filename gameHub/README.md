# GameHub - Sistema de Gerenciamento de Biblioteca de Jogos 🎮

Este é um sistema web desenvolvido com Django + Django REST Framework para gerenciar uma biblioteca de jogos, permitindo cadastro de usuários, jogos, avaliações, favoritos, empréstimos e notificações.

---

## ✅ Funcionalidades
- Cadastro de jogos com categoria, plataforma e desenvolvedora
- Biblioteca personalizada para cada usuário
- Marcar jogos como favoritos
- Avaliar jogos
- Emprestar jogos entre usuários
- Receber notificações (com envio simulado por email)
- API REST com autenticação JWT (opcional)

---

## 🛠️ Tecnologias Utilizadas
- Python 3.11+
- Django 4+
- Django REST Framework
- SimpleJWT (autenticação por token JWT)
- SQLite (banco padrão do Django)

---

## 🚀 Como Rodar o Projeto Localmente

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/gamehub.git
cd gamehub
```

### 2. Crie o ambiente virtual e ative-o
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Aplique as migrações
```bash
python manage.py migrate
```

### 5. Crie um superusuário (para acessar o /admin)
```bash
python manage.py createsuperuser
```

### 6. Rode o servidor local
```bash
python manage.py runserver
```

Acesse: http://127.0.0.1:8000/

---

## 📌 Endpoints Principais da API

### Autenticação JWT
```
POST /api/token/           → Gera token de acesso e refresh
POST /api/token/refresh/   → Gera novo token de acesso
```

### CRUD de recursos
```
GET/POST/PUT/DELETE:
/api/jogos/
/api/categorias/
/api/plataformas/
/api/desenvolvedoras/
```

> Obs: Por padrão, as rotas estão públicas (`AllowAny`). Você pode exigir token JWT se quiser.

---

## 📂 Estrutura de Diretórios
```
gamehub/
├── core/                 # App principal
│   ├── models.py         # Entidades do sistema (10 modelos)
│   ├── serializers.py    # Serialização para API
│   ├── views.py          # ViewSets expostos via API
│   ├── urls.py           # Rotas REST
│   ├── services.py       # Injeções de dependência
│   └── repositories.py   # Acesso aos dados com abstração
├── gameHub/              # Configurações do projeto
│   └── settings.py
└── manage.py
```

---

## 🧪 Testes Automatizados
- Os testes são feitos com **Katalon Studio**.
- Incluem:
  - Teste de autenticação
  - Testes GET e POST para /jogos/
  - Validação de resposta 200/201 e conteúdo do JSON

> Os arquivos `.zip` dos testes e instruções estão na pasta `/tests_katalon/`.

---

## 🧰 Jenkins
Há um `Jenkinsfile` incluído com os seguintes passos:
- Instala dependências
- Roda migrações
- Executa testes
- Faz linting do código

---

## 🔎 Análise de Código - SonarCloud
- A análise de qualidade é feita pelo [SonarCloud](https://sonarcloud.io)
- O projeto deve ser vinculado ao repositório do GitHub
- Gere o PDF com a análise da branch `main` para entrega final

---

## 📃 Licença
Este projeto é apenas para fins acadêmicos e educacionais.

---

Feito com 💻 por [Seu Nome Aqui]
