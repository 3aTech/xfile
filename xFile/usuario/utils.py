def get_user_permissions(user):
    """Retorna un diccionario con los permisos basados en el grupo del usuario"""
    permisos = {
        'ver_dashboard': False,
        'gestionar_arriendos': False,
        'gestionar_ubicaciones': False,
        'gestionar_inmuebles': False,
        'gestionar_usuarios': False,
        'administrar_sistema': False,
        'gestionar_urbanismos': False
    }
    
    grupos = user.groups.values_list('name', flat=True)
    
    if 'MASTER' in grupos:
        return {key: True for key in permisos}
    
    if 'COORDINADOR' in grupos:
        permisos['administrar_sistema'] = True
        permisos['ver_dashboard'] = True
        
    if 'ADMINISTRADOR' in grupos:
        permisos['gestionar_arriendos'] = True
        permisos['ver_dashboard'] = True
        
    if 'ASISTENTE ADMINISTRATIVO' in grupos:
        permisos['gestionar_inmuebles'] = True
        permisos['gestionar_ubicaciones'] = True
        permisos['ver_dashboard'] = True
        
    if 'USUARIO CMG' in grupos:
        permisos['ver_dashboard'] = True
        permisos['gestionar_urbanismos'] = True
        
    return permisos 