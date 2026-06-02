from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, CallbackQueryHandler
from database.db_manager import db
from characters.nova import Nova
from characters.luna import Luna
from characters.aria import Aria
from characters.zara import Zara
from characters.eden import Eden

CHARACTERS = {
    'nova': Nova(),
    'luna': Luna(),
    'aria': Aria(),
    'zara': Zara(),
    'eden': Eden(),
}

async def select_character(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Mostrar menú de selección de personajes"""
    
    user_id = update.effective_user.id
    user = db.get_user(user_id)
    
    if not user:
        user = db.create_user(user_id, update.effective_user.first_name)
    
    # Verificar si usuario ya tiene personaje activo
    active_char = db.get_active_character(user_id)
    
    if active_char:
        message = f"Ya estás con <b>{active_char}</b>.\n\n¿Quieres cambiar?"
    else:
        message = """
<b>🌟 BIENVENIDO AL SISTEMA DE NOVIAS VIRTUALES</b>

Eres el usuario número {user_id}

Aquí hay 5 personajes increíbles esperándote.

Cada uno tiene su propia historia de 100 capítulos.
Cada decisión que tomes afectará tu relación con ellas.

¿A quién quieres conocer?
        """.format(user_id=user_id)
    
    # Crear botones para cada personaje
    keyboard = [
        [
            InlineKeyboardButton(
                f"🌃 Nova (Cyberpunk)",
                callback_data="char_nova"
            ),
            InlineKeyboardButton(
                f"🌙 Luna (Espacio)",
                callback_data="char_luna"
            )
        ],
        [
            InlineKeyboardButton(
                f"✨ Aria (Ángel)",
                callback_data="char_aria"
            ),
            InlineKeyboardButton(
                f"⚔️ Zara (Guerrera)",
                callback_data="char_zara"
            )
        ],
        [
            InlineKeyboardButton(
                f"🌊 Eden (Sirena)",
                callback_data="char_eden"
            )
        ],
        [
            InlineKeyboardButton(
                "📊 Ver mis personajes",
                callback_data="view_characters"
            )
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        message,
        reply_markup=reply_markup,
        parse_mode='HTML'
    )

async def character_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Manejar selección de personaje"""
    
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    char_name = query.data.split('_')[1]  # "char_nova" -> "nova"
    
    # Guardar personaje activo
    db.set_active_character(user_id, char_name)
    
    # Obtener personaje
    character = CHARACTERS[char_name]
    
    # Enviar saludo del personaje
    greeting = character.get_greeting()
    
    await query.edit_message_text(
        text=greeting,
        parse_mode='HTML'
    )
    
    # Ofrecer comenzar historia
    keyboard = [
        [InlineKeyboardButton(
            "📖 Comenzar historia",
            callback_data=f"start_story_{char_name}"
        )]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.message.reply_text(
        f"¿Estás listo para la historia de {character.name.title()}?",
        reply_markup=reply_markup
    )

async def view_my_characters(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Ver progreso con todos los personajes"""
    
    query = update.callback_query
    await query.answer()
    
    user_id = query.from_user.id
    progress_list = db.get_all_character_progress(user_id)
    
    message = "<b>📊 Tu progreso con cada personaje:</b>\n\n"
    
    for progress in progress_list:
        character = CHARACTERS[progress.character_name]
        bar = character.get_affinity_bar(progress.affinity)
        
        message += f"""
{character.emoji} <b>{progress.character_name.upper()}</b>
   Capítulo: {progress.current_chapter}/100
   Afinidad: {bar} ({progress.affinity:.0f}/100)
   Tiempo: {progress.playtime_hours:.1f}h
   
"""
    
    await query.edit_message_text(
        text=message,
        parse_mode='HTML'
    )

# Handlers
select_handler = CommandHandler('select', select_character)
character_callback = CallbackQueryHandler(
    character_selected,
    pattern=r'^char_\w+$'
)
view_callback = CallbackQueryHandler(
    view_my_characters,
    pattern=r'^view_characters$'
)
