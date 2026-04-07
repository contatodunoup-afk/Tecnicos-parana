# Guia de Deploy no GitHub

## Pré-requisitos
1. **Git** - [Download aqui](https://git-scm.com/download/win)
2. **Conta GitHub** - [Criar em github.com](https://github.com/signup)
3. **Personal Access Token** - [Gerar neste link](https://github.com/settings/tokens)

## ⚙️ Passo 1: Instalar Git
1. Download e instale Git para Windows
2. Reinicie o PowerShell após instalação
3. Verifique com: `git --version`

## 🔑 Passo 2: Gerar Personal Access Token no GitHub
1. Vá em https://github.com/settings/tokens
2. Clique em "Generate new token" (Classic)
3. Dê um nome: `Mapa-Parana-Deploy`
4. Selecione as permissões: `repo`, `workflow`
5. Copie e guarde o token com segurança

## 📁 Passo 3: Fazer upload para GitHub

Abra PowerShell na pasta do projeto e execute:

```powershell
# Configurar Git (primeira vez)
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@gmail.com"

# Adicionar todos os arquivos
git add .

# Fazer primeiro commit
git commit -m "Initial commit: Mapa Prática Service+ Paraná PR"

# Adicionar repositório remoto
git remote add origin https://github.com/SEU_USUARIO/Tecnicos-parana.git

# Fazer push (quando pedir password, cole o token)
git branch -M main
git push -u origin main
```

## 🌐 Passo 4: Ativar GitHub Pages

1. Vá ao repositório no GitHub
2. Acesse: **Settings** → **Pages**
3. Em "Source", selecione: **Deploy from a branch**
4. Selecione a branch: **main**
5. Selecione a pasta: **/ (root)**
6. Clique em "Save"
7. Aguarde alguns minutos...

Seu site estará em: `https://SEU_USUARIO.github.io/Tecnicos-parana/`

## 📝 Comandos Úteis para Futuras Atualizações

```powershell
# Ver status
git status

# Adicionar arquivo específico
git add mapa.html

# Fazer commit
git commit -m "Descrição da mudança"

# Fazer push
git push

# Ver histórico
git log --oneline
```

## ✅ Checklist

- [ ] Git instalado
- [ ] Conta GitHub criada
- [ ] Token pessoal gerado
- [ ] Repositório criado no GitHub
- [ ] Primeiro push feito
- [ ] GitHub Pages ativado
- [ ] Site live em https://seu-usuario.github.io/Tecnicos-parana/

## 🆘 Dúvidas?

Se o token expirar, gere um novo seguindo o Passo 2.
Se tiver erro ao fazer push, verifique se o repositório existe no GitHub.
