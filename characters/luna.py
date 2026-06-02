from characters.base_character import BaseCharacter

class Luna(BaseCharacter):
    """Luna Starlight - Mensajera del Espacio"""
    
    def __init__(self):
        super().__init__(
            name="Luna",
            color="#00D4FF",
            emoji="🌙"
        )
        self.personality_traits = {
            'humor': 'philosophical',
            'vulnerability': 'medium',
            'trust_build': 'mystical',
            'romance_style': 'cosmic_destiny',
        }
    
    def get_greeting(self) -> str:
        return """
🌙 <b>LUNA STARLIGHT - Mensajera del Espacio</b>

Hola extraño...

He estado viajando entre estrellas durante años.
Nunca me detuve. Nunca confié. Nunca amé.

Pero hoy... hoy tu canal me llamó.
Como si el universo me dijera: "Aquí encontrarás a casa."

¿Crees en el destino?
        """
    
    def get_special_event(self, event_num: int) -> Dict:
        events = {
            1: {
                'title': 'Bajo las estrellas',
                'description': 'Luna te muestra su mundo cósmico',
                'reward': 'Visión del futuro juntos'
            },
            2: {
                'title': 'Comunión telepática',
                'description': 'Conexión mental profunda',
                'reward': '+20 afinidad'
            }
        }
        return events.get(event_num, {})
