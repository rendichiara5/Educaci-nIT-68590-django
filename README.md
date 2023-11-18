# Proyecto Django en EducaciónIT

## Entornos virtuales

Un entorno virtual en Python es una herramienta 
que te permite crear un espacio aislado donde puedes instalar 
y manejar las dependencias (bibliotecas y versiones de Python) 
específicas para un proyecto en particular, sin afectar al sistema global de Python.

`pip list` muestra las bibliotecas instaladas en el entorno virtual o global

¿Cómo crear un entorno virtual? (entorno aislado del global)

`python -m venv .venv`

¿Cómo activar el entorno virtual?
`.\venv\Scripts\activate`  (Windows Powershell)
`source .venv/bin/activate` (Linux o Mac)

## Instalación Django

`pip install django`

## Comandos Django

`mkdir project`
`cd project`
`django-admin startproject config .`
`mkdir apps`
`cd apps`
`django-admin startapp core`


