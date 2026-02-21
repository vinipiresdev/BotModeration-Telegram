import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
from openai import OpenAI

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = "seu_token_aqui"

client = OpenAI(
    base_url="https://api.astralai.pro/v1",
    api_key="sua_api_key_aqui"
)

CATEGORIAS_PT = {
    "harassment": "assédio",
    "harassment_threatening": "assédio com ameaça",
    "hate": "discurso de ódio",
    "hate_threatening": "discurso de ódio com ameaça",
    "self_harm": "automutilação",
    "self_harm_instructions": "instruções de automutilação",
    "self_harm_intent": "intenção de automutilação",
    "sexual": "conteúdo sexual",
    "sexual_minors": "conteúdo sexual envolvendo menores",
    "violence": "violência",
    "violence_graphic": "violência gráfica",
}

async def moderar_mensagem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    usuario = update.message.from_user
    logger.info(f"Mensagem de @{usuario.username} (id {usuario.id}): {texto}")

    response = client.moderations.create(input=texto)
    result = response.results[0]

    logger.info(f"Scores: {result.category_scores}")

    if result.flagged:
        categorias = [
            CATEGORIAS_PT.get(k, k)
            for k, v in result.categories.__dict__.items() if v
        ]
        motivo = ", ".join(categorias)
        logger.warning(f"BLOQUEADA de @{usuario.username}: {motivo}")
        await update.message.reply_text(f"⚠️ Mensagem bloqueada.\n\nMotivo: {motivo}")
    else:
        logger.info(f"APROVADA de @{usuario.username}")
        await update.message.reply_text("Mensagem aprovada!")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, moderar_mensagem))

logger.info("Bot iniciado!")
app.run_polling()