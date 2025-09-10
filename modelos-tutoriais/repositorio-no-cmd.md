Passo a passo de como usar o GitHub com o CMD:

1 - Logar no Github e ir no repositório desejado

2 - Clicar em "Code" e copiar o link em HTTPS

3 - Abra o cmd e entrar na pasta desejada pelo comando CD (recomendado a pasta Downloads), escreva: git clone https://github.com/seu-usuario/seu-repositorio.git

4 - Caso você esteja usando um repositório privado e seja um colaborador, vc terá que fazer uma verificação que o próprio cmd te redireciona. Depois de fazer o login, volte para o cmd

5 - Use o comando dir e depois cd na pasta onde o repositório está localizado

6 - Para mover um arquivo para dentro do GitHub, você cria uma pasta, coloca o arquivo que você quer, coloca ele dentro da pasta do repositório e depois usa o comando git status

7 - Use o comando git add . para adicionar todas as alterações feitas

8 - Use o comando git commit -m"mensagem com as alterações feitas"

9 - Caso você esteja em um repositório privado, vai aparecer dois comandos ao tentar usar o commit, o primeiro deles é um que vc copia e cola e muda a mensagem dentro das aspas pro seu email, e o outro serve para você escolher o nome que vai aparecer no commit

10 - Para enviar as alterações para o GitHub, use o comando git push -u origin main (ou o nome da branch atual)

INFO EXTRA:

- Usar a setinha para cima e para baixo no CMD, ele mostra os comandos utilizados anteriormente

- Um arquivo word não aparece pra pré-visualização no github, ele só será exibido se estiver no formato PDF

- Vídeo que explica como configurar o git: https://www.youtube.com/watch?v=IJ2VDiDLzj8&list=PLDgemkIT111A4GXwC2loYiLAvfIlMQRlZ&index=1&ab_channel=FernandoLeonid

- Se você quiser visualizar todos os commits, vá para o repositório no GitHub e clique em "Commits" para visualizar todas as alterações feitas por cada membro do grupi
