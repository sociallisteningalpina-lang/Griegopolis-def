#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clasificador de Temas para Comentarios de Campañas
Personalizable por campaña/producto
"""

import re
from typing import Callable

def create_topic_classifier() -> Callable[[str], str]:
    """
    Retorna una función de clasificación de temas personalizada para la campaña Griegopolis.
    
    Returns:
        function: Función que toma un comentario (str) y retorna un tema (str)
    
    Usage:
        classifier = create_topic_classifier()
        tema = classifier("¿Dónde está la receta?")
        # tema = 'Solicitud de Recetas'
    """
    
    def classify_topic(comment: str) -> str:
        """
        Clasifica un comentario en un tema específico basado en patrones regex.
        
        Args:
            comment: Texto del comentario a clasificar
            
        Returns:
            str: Nombre del tema asignado
        """
        comment_lower = str(comment).lower()
        
        # CATEGORÍA 1: Solicitud de Recetas e Instrucciones
        # (Prioridad alta - tema principal de la campaña)
        if re.search(
            r'receta|f[oó]rmula|c[oó]mo se hace|c[oó]mo se prepar|'
            r'c[oó]mo lo hago|env[ií]a.*receta|quiero.*receta|'
            r'no veo.*receta|d[oó]nde.*receta|instrucciones|'
            r'preparaci[oó]n|parte 2|parte 3|continuaci[oó]n',
            comment_lower
        ):
            return 'Solicitud de Recetas'
        
        # CATEGORÍA 2: Problemas con Recetas/Instrucciones
        if re.search(
            r'algo est[aá] mal|no funciona|no sale|medidas|'
            r'est[aá] equivocad[oa]|no es.*taza|definitivamente no|'
            r'masa espesa|no coincide|error en|problema con',
            comment_lower
        ):
            return 'Problemas con Recetas'
        
        # CATEGORÍA 3: Precio y Costo
        if re.search(
            r'\bcaro\b|\bcostoso\b|bajen el precio|muy caro|'
            r'precio|cuesta|vale|econ[oó]mico',
            comment_lower
        ):
            return 'Precio'
        
        # CATEGORÍA 4: Beneficios de Salud y Experiencias Positivas
        if re.search(
            r'cur[oó].*gastritis|prote[ií]na|saludable|bueno para|'
            r'beneficios|me cur[oó]|es muy bueno|excelente|'
            r'super bueno|nutritivo|vitamina',
            comment_lower
        ):
            return 'Beneficios de Salud'
        
        # CATEGORÍA 5: Opinión General del Producto
        if re.search(
            r'me gusta|me encanta|delicioso|rico|bueno|'
            r'excelente(?!.*bendiciones)|s[uú]per(?!.*bueno)|'
            r'se ve delicioso|belleza de producto|feliz',
            comment_lower
        ):
            return 'Opinión Positiva del Producto'
        
        # CATEGORÍA 6: Formas de Consumo y Acompañamientos
        if re.search(
            r'con frutas|con fresas|con moras|ensalada|'
            r'acompañar|combinar|mezclar|agridulce|'
            r'toquecito|agregar',
            comment_lower
        ):
            return 'Formas de Consumo'
        
        # CATEGORÍA 7: Ingredientes y Composición
        if re.search(
            r'aspartame|sacarosa|az[uú]car|prote[ií]na|'
            r'ingredientes|contiene|tiene|posee|'
            r'gramos|componente',
            comment_lower
        ):
            return 'Ingredientes y Composición'
        
        # CATEGORÍA 8: Comparación con Otros Productos
        if re.search(
            r'mejor.*k[eé]fir|como.*huevos|lo mismo que|'
            r'comparado|versus|vs|mejor que',
            comment_lower
        ):
            return 'Comparación con Otros Productos'
        
        # CATEGORÍA 9: Comentarios sobre Contenido/Publicidad
        if re.search(
            r'borrador|video|calvo|invitado|fastidioso|'
            r'bobazo|cringe|llor[oó]n|soporta|'
            r'papas bravas|equivocad[oa]|publicidad',
            comment_lower
        ):
            return 'Comentarios sobre Contenido'
        
        # CATEGORÍA 10: Disponibilidad y Ubicación
        if re.search(
            r'd[oó]nde est[aá]|ubicad[oa]|d[oó]nde comprar|'
            r'consigo|encuentro|tienda|venden',
            comment_lower
        ):
            return 'Disponibilidad y Ubicación'
        
        # CATEGORÍA 11: Fuera de Tema / Religioso
        if re.search(
            r'am[eé]n|bendiciones|dios te bendiga|padre amado|'
            r'gracias a dios|se[ñn]or|oraci[oó]n|recibo.*bendici[oó]n|'
            r'todo poderoso',
            comment_lower
        ):
            return 'Fuera de Tema / Religioso'
        
        # CATEGORÍA 12: Fuera de Tema / Solo Emojis o Muy Corto
        emoji_count = len(re.findall(r'[😀-🙏🌀-🗿]|❤️|♥️|✨|💛|💗|💕|🍓|🥗|🥡|🙀|😳|🥰|🫢', comment))
        word_count = len([w for w in comment_lower.split() if len(w) > 2])
        
        if emoji_count > word_count or word_count < 2:
            return 'Fuera de Tema / Solo Emojis'
        
        if re.search(
            r'^(si|no|jaja|gracias|mmm|w|j|op|l|algo)$',
            comment_lower.strip()
        ):
            return 'Fuera de Tema / Solo Emojis'
        
        # CATEGORÍA 13: Otros
        return 'Otros'
    
    return classify_topic
# ============================================================================
# METADATA DE LA CAMPAÑA (OPCIONAL)
# ============================================================================

CAMPAIGN_METADATA = {
    'campaign_name': 'Alpina - Kéfir',
    'product': 'Kéfir Alpina',
    'categories': [
        'Preguntas sobre el Producto',
        'Comparación con Kéfir Casero/Artesanal',
        'Ingredientes y Salud',
        'Competencia y Disponibilidad',
        'Opinión General del Producto',
        'Fuera de Tema / No Relevante',
        'Otros'
    ],
    'version': '1.0',
    'last_updated': '2025-11-20'
}


def get_campaign_metadata() -> dict:
    """Retorna metadata de la campaña"""
    return CAMPAIGN_METADATA.copy()
