from characters.base_character import BaseCharacter

class Nova(BaseCharacter):
    """Nova V. - Hacker Cyberpunk"""
    
    def __init__(self):
        super().__init__(
            name="Nova",
            color="#A020F0",
            emoji="🌃"
        )
        self.personality_traits = {
            'humor': 'dark_sarcasm',
            'vulnerability': 'high',
            'trust_build': 'slow_then_fast',
            'romance_style': 'slow_burn',
        }
    
    def get_greeting(self) -> str:
        return """
🌃 <b>NOVA V. - Hacker Cyberpunk</b>

⚠️ [TRANSMISIÓN INTERCEPTADA — CANAL SEGURO]

Hola... soy Nova. Necesitaba refugio. Encontré tu canal.

¿Me ayudas?

Este será un viaje de 100 capítulos donde tus decisiones importan.
Donde descubriremos si alguien como yo merece ser amado.
        """
    
    def get_special_event(self, event_num: int) -> Dict:
        """Eventos especiales de Nova"""
        events = {
            1: {
                'title': 'Primera visita a su departamento',
                'description': 'Nova te muestra su espacio privado',
                'reward': 'Primer recuerdo compartido'
            },
            2: {
                'title': 'Noche de lluvia',
                'description': 'Lluvia en Neo-City, vulnerabilidad',
                'reward': '+15 afinidad'
            },
            5: {
                'title': 'Cumpleaños de Maya',
                'description': 'Celebración familiar',
                'reward': 'Inclusión en familia'
            }
        }
        return events.get(event_num, {})
