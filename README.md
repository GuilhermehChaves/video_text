## videoText

version: 0.0.1

Script em Python desenvolvido para retornar o conteúdo em texto de um vídeo.

## Sobre o projeto

A função `run` tem quatro paramêtros como argumento:

1 - Caminho do vídeo

2 - Diretório onde irá salvar o vídeo cortado

3 - Diretório onde irá salvar o aúdio de cada video cortado

4 - O nome do arquivo txt salvo no fim da execução

## Exemplo

```python
import video_text as vt
vt.run('./video/input/filipe.mp4', './video/output/', './audio/', 'deschamps')
```

## Como funciona

O script corta o video em várias partes, em seguida extrai o áudio de cada uma e usando a biblioteca `SpeechRecognition` é feito o reconhecimento do texto de cada áudio extraido, no final é gerado um txt contendo as falas do vídeo (não fica 100% corretas) e os vídeos e áudios gerados são excluidos logo em seguida.

## Objetivo

Apesar de dependendo do tamanho do vídeo demorar um pouco ainda é mais rápido do que ouvir o vídeo e fazer a transcrição manualmente pois pode se perder em alguma parte e ter a necessidade de ficar voltando repetidamente, como o script não acerta 100% do texto você terá o trabalho apenas de revisar e corrigir algumas partes do texto gerado. 