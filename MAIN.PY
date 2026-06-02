import logging
from telegram.ext import Application
from config import config
from handlers.character_selection import select_handler, character_callback, view_callback
from handlers.chapter_handler import play_handler, next_handler
from handlers.choice_handler import choice_callback
from handlers.start_handler import start_handler
from handlers.error_handler import error_handler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def main():
    """Iniciar bot de novias virtuales"""
    
    app = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()
    
    # Handlers de inicio
    app.add_handler(start_handler)
    app.add_handler(select_handler)
    
    # Handlers de personajes
    app.add_handler(character_callback)
    app.add_handler(view_callback)
    
    # Handlers de capítulos
    app.add_handler(play_handler)
    app.add_handler(next_handler)
    
    # Handlers de elecciones
    app.add_handler(choice_callback)
    
    # Error handler
    app.add_error_handler(error_handler)
    
    logger.info("🌟 Sistema de Novias Virtuales iniciado...")
    app.run_polling()

if __name__ == '__main__':
    main()
