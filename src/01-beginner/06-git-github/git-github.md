![](https://joseluisramoncolmenares.files.wordpress.com/2020/05/diploma-git-github.png)

# Profesional de Git y Github

**Prof. Freddy Vega**

## Configurar Git con Windows Subsystem for Linux

Los pasos para configurar que Github pueda funcionar con WSL son los siguientes:

1. **Instalar Git Bash en Windows.**

   Git viene incluido en WSL.  Sin embargo, hasta donde he investigado, para que pueda funcionar correctamente es necesario que esté instalado directamente en Windows, siguiendo lo pasos que se indica [aquí](https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Configurando-Git-por-primera-vez) 

2. **Crear las llaves SSH para la conexión con Github.**

   El problema en la configuración de GIT desde WSL se presenta en las llave SSH. Hasta donde he visto, las llaves SSH que GIT desde WSL se tienen que configurar primero en Windows. Para generarlas seguir lo que se indica [aquí](https://help.github.com/es/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

3. **Agregar las llave SSH de Windows a tu cuenta de Github**

   Este paso ya está muy bien descrito en la documentación de Github. Puede acceder por el siguiente [link](https://help.github.com/es/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account).

4. **Configurar GIT en WSL**

   Abrir la BASH de WSL. Y realizar la configuración general ejecutando los siguiente comandos. 

   ```bash
   git config --global user.name "[nombre de usuario github]"
   git config --global user.email "[email de github]"
   ```

   Yo también agregué los siguientes comandos. 

   ```bash
   git config --global color.ui true
   git config --global core.editor code
   ```

5. **Conectar tus primer repo de Github**

   lo primero que tienes que hacer es ir a Github y crear el repositorio. Si quieres puedes dejarlos vacío, pero siempre es recomendable tener al menos un README.md. 

   Una vez creado, con WSL puede ir hasta la carpeta donde deseas empezar a trabajar con el repositorio y ejecutar los siguientes comandos

   ```bash
   git init
   git add .
   git commit -m "first commit"
   git remote add origin https://github.com/joseluisramon/HackerRank.git
   git push -u origin master
   ```

   Al hacer esto por primera vez se va a desplegar una ventana en la cual tienes que introducir tu usuario y contraseña de Github. Una vez hecho esto, el proceso funcionará sin problemas. 



## Comandos comunes de Git

[AGREGAR INFORMACIÓN AQUÍ]



