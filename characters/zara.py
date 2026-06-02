from characters.base_character import BaseCharacter

class Zara(BaseCharacter):
    """Zara Iron - Guerrera del Futuro"""
    
    def __init__(self):
        super().__init__(
            name="Zara",
            color="#FF0000",
            emoji="⚔️"
        )
        self.personality_traits = {
            'humor': 'direct_passionate',
            'vulnerability': 'low_guarded',
            'trust_build': 'through_action',
            'romance_style': 'warrior_devotion',
        }
    
    def get_greeting(self) -> str:
        return """
⚔️ <b>ZARA IRON - Guerrera del Futuro</b>

He conquistado reinos.
He liderado ejércitos.
He destruido imperios.

Pero nunca había sentido miedo.

Hasta que te vi. Porque si te pierdo...
No habrá batalla que valga la pena.
        """
    
    def get_special_event(self, event_num: int) -> Dict:
        events = {
            1: {
                'title': 'Entrenamiento de combate',
                'description': 'Zara te enseña a luchar',
                'reward': 'Partnership guerrero'
            },
            2: {
                'title': 'Batalla juntos',
                'description': 'Luchan espalda con espalda',
                'reward': 'Vínculo de batalla'
            }
        }
        return events.get(event_num, {})
