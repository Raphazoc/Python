
# Atualizando um dicionário com o método update()
perfil_usuario = {"nome": "Lucas", "tema": "claro", "notificacoes": True}

novas_configuracoes = {"tema": "escuro", "idioma": "pt-BR"}

# Atualiza o perfil com as novas configuracoes

perfil_usuario.update(novas_configuracoes)

print(perfil_usuario)