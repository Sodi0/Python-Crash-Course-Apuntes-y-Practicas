# Git - Sistema de Control de Versiones

## ¿Qué es Git?

Git es un sistema de control de versiones distribuido que enfatiza la velocidad, integridad de datos y soporte para flujos de trabajo distribuidos y no lineales. Fue creado por Linus Torvalds en 2005 para el desarrollo del kernel de Linux y actualmente es el sistema de control de versiones más adoptado.

## Conceptos Fundamentales

### Términos Clave
- **Repository (Repositorio)**: Almacenamiento del proyecto y su historial
- **Working Directory**: Carpeta con el código actual
- **Commit**: Captura instantánea del directorio de trabajo
- **Staging Area/Index**: Área intermedia antes de hacer commit
- **Branch**: Línea independiente de desarrollo

## Instalación

### Linux
```bash
# Debian/Ubuntu/Mint
apt-get install git

# RHEL/CentOS/Fedora
yum install git
```

### Windows
Descargar desde: https://git-scm.com/download/win

### macOS
```bash
# Instalar Homebrew primero
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Instalar Git
brew install git
```

## Configuración Inicial

```bash
# Identidad
git config --global user.name "Tu Nombre"
git config --global user.email tu@email.com

# Editor
git config --global core.editor emacs

# Ver configuración
git config --list
```

## Comandos Básicos

### Crear/Clonar Repositorio
```bash
git init                    # Crear repositorio local vacío
git clone <URL>            # Clonar repositorio remoto
```

### Comandos de Transporte de Datos
```bash
git add                    # Agregar archivos al staging area
git commit                 # Guardar cambios en el repositorio
git push                   # Enviar cambios al repositorio remoto
git fetch                  # Obtener cambios del repositorio remoto
git checkout               # Cambiar de rama o restaurar archivos
git merge                  # Fusionar ramas
```

### Comandos de Estado y Consulta
```bash
git status                 # Ver estado del árbol de trabajo
git log                    # Ver historial de commits
git ls-files -s           # Ver archivos en el index
```

### Manejo de Ramas
```bash
git branch                 # Listar ramas locales
git branch <nombre>        # Crear nueva rama
git branch -d <nombre>     # Eliminar rama
git branch -m <nombre>     # Renombrar rama actual
```

### Comandos Adicionales
```bash
git commit -am             # Combina add y commit
git pull                   # Combina fetch y merge
git remote -v              # Listar repositorios remotos
git remote add             # Agregar repositorio remoto
git rm                     # Eliminar archivos
git reset                  # Revertir cambios
```

## Archivo .gitignore

Contiene lista de archivos y carpetas que Git debe ignorar:
- Archivos del sistema operativo (Thumbs.db, .DS_Store)
- Archivos de configuración de IDE (.vscode)
- Archivos generados (*.exe, *.min.js)
- Dependencias (node_modules)
- Credenciales (wp-config.php)

## Flujo de Trabajo Típico

1. **Clonar repositorio**: `git clone` o `git init`
2. **Crear/cambiar rama**: `git branch` / `git checkout`
3. **Modificar archivos**: Editar código
4. **Agregar al staging**: `git add`
5. **Revisar cambios**: `git status`, `git diff`
6. **Hacer commit**: `git commit`
7. **Enviar cambios**: `git push`
8. **Obtener actualizaciones**: `git fetch` / `git pull`

## Tareas Típicas de Control de Versiones

- Rastrear cambios
- Realizar actualizaciones
- Obtener actualizaciones
- Resolver conflictos
- Ver diferencias (diffing)
- Ramificación y fusión
- Controlar conjuntos de cambios

## Recursos Recomendados

- [Documentación oficial de Git](https://git-scm.com/book/en/v2)
- [Tutorial de Atlassian](https://www.atlassian.com/git/tutorials)
- [Try GitHub](https://try.github.io)
- [Learn Git Branching](https://learngitbranching.js.org/)

---

*Basado en la presentación de Vyacheslav Koldovskyy*