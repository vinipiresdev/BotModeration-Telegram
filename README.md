# AegisGuard

Bot para Telegram que analisa mensagens e bloqueia conteúdo inapropriado automaticamente.

## Tecnologias

- Python 3.10+
- python-telegram-bot
- Astral AI Moderation API

## Instalação

```bash
pip install -r requirements.txt
```

## Configuração

No `bot.py`, coloque suas credenciais:

```python
TELEGRAM_TOKEN = "seu_token_aqui"
api_key = "sua_api_key_aqui"
```

O token do Telegram é obtido pelo @BotFather. A API key pelo painel de controle do astralai.pro.
- https://astralai.pro/dashboard

## Como rodar

```bash
python bot.py
```

## Como funciona

Toda mensagem enviada ao bot é analisada pela API de moderação da Astral AI. Se a mensagem for considerada inapropriada, o bot responde informando o motivo. Caso contrário, informa que foi aprovada.

Os logs ficam salvos em `bot.log` e também aparecem no terminal em tempo real.

Desenvolvido com 💙 por [vinipiresdev](https://github.com/vinipiresdev)