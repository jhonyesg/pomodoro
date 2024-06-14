# Pomodoro Timer App
Una aplicación de temporizador Pomodoro desarrollada con `tkinter` para la interfaz gráfica, `Pillow` para la manipulación de imágenes, y `pygame` para la reproducción de sonidos.
# Descripción

Esta aplicación permite a los usuarios seguir la técnica Pomodoro, que consiste en trabajar durante 25 minutos y luego tomar un descanso corto de 5 minutos. Después de cuatro ciclos de trabajo/descanso, se toma un descanso largo de 10 minutos. La interfaz gráfica incluye una imagen de un tomate, botones para iniciar y reiniciar el temporizador, y la funcionalidad para ampliar o reducir la interfaz.

<b>Características</b>
* Temporizador Pomodoro con ciclos de trabajo y descanso.
* Sonido de alarma al finalizar cada intervalo.
* Interfaz gráfica sin barra de título, con una imagen de tomate.
* Opciones para mover la ventana, y ampliar/reducir la interfaz.



### Requisitos
- [x] Python 3.x 
- [x] tkinter
- [x] Pillow
- [x] pygame

### Instalación
- [ ] I recommend the following:

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/pomodoro-timer.git
    cd pomodoro-timer
    ```.
2. Change the default/initial *admin* password for security purpose.
3. Instead of using the *admin* acccount, consider creating a different/separate credentials for different website/service.  This will make it easier for backup and recovery; especially, when you need to move the user to a different installation.

### extra
If you use this Docker for hosting and allow your user to login, I also recommend installing maldetect on the docker host to scan the /home volume.

Enjoy!!!

### GeoIP Blocking
```
http {
    ...
    geoip2 /etc/nginx/geoip2/GeoLite2-Country.mmdb {
        auto_reload 5m;
        $geoip2_country_code default=US source=$remote_addr country iso_code;
    }
    ...
    map $geoip2_country_code $allowed_country {
        default yes;
        FK no;
        FM no;
        EH no;
    }
}

server {
    ...
    if ($allowed_country = no) {
        return 444;
    }
    ...
}
```


## Release Notes
1.9.0 - remove php7.1 and add php7.4, update to GoLang 1.13.5 and dotnet 3.1

1.8.5 - build update for Vesta 0.9.8-25 and nginx 1.16.1

1.8.0 - replace phpmyadmin and phppgadmin with adminer.

1.6.0 - Add wordpress support.  Fix MongoDB weird build issue.  Python 3.7, DotNetCore 2.2, GoLang 1.12.5, and update postgis-2.4 to postgis-2.5

1.5.2 - with php7.3 support.

1.4.0 - Major release!  In this update, we remove support for php5.6 and 7.0 as it will no longer officially supported/at end of life (EOL): http://php.net/supported-versions.php  There is no excuse.  You know this day was coming.  

* PHP 7.3 has not release so it's not yet available, but templates were added to prep for 7.3 release at the end of the year.  We will also switch from nodejs 8.x to nodejs 10.x once it go into LTS at the end of this month.

* This release also default php to 7.2 and switch to golang 1.11.1

* I've made some attempts in 1.4.x to provide auto-upgrade with rsync but there were hickups along the way that I find may not work perfectly for everyone.  Therefore, as this is a Major upgrade (consider it like a fresh install), I would suggest to perform user backup, download of backup, and restore. It's the same step as you would expect to migrate another server: https://vestacp.com/docs/#how-to-migrate-user-to-another-server 

1.3.10 - finalizing stuff to get ready for 1.4.0

1.3.9 - update to 0.9.8-23, see security bulleton/notice in forum here: https://forum.vestacp.com/viewtopic.php?f=10&t=17795  The panel should have auto-updated, we're just updating the build for new user convenience.

1.3.6 - update nginx to 1.14 stable release, update dotnet

1.3.5 - update to 0.9.8-22 - REMINDER: if your server has not autoupdate to 0.9.8-22, please do so or update to this release.  There is a serious security issue in 0.9.8-20.

1.3.3 - update to 0.9.8-20

1.3.1 - upgrade documentation.  

```
- If you're using postgresql 9.5 then you want to backup all your users and then restore them on the new docker using vesta panel.  

- If you're not using postgresql, then ssh as admin and run 'sudo bash /bin/vesta-update.shell' to upgrade everything.  As always, it is best to backup all your users.
```

1.3.0 - **Breaking Changes**: update to postgresql-9.6, add pgaudit and postgis geo extension.  This is the most popular postgresql version that also work best with postgis.  Make sure you have all your postgresql databases backuped before updating to this version.

1.2.1 - Update to be more secure and compliance.  A bunch of security issues discovered during the holidays were patched by various vendors including cpu (meltdown & spectre) and .net core issues:

```
- php 5.6 v8js no longer supported due to security issues resulting in older v8 deprecation.
- update nginx to 1.13.9 - rebuilt with latest ngx_pagespeed
- update golang 1.10
- update to dotnet-sdk-2.1.101
- update from 3.4 to 3.6 for mongodb
```

1.1.0 - starting from this version, we upgraded to MariaDB 10.2.

1.0.8 - introducing vesta 0.9.8-18, update to this docker image then run */bin/vesta-update.sh* to update Vesta.

1.0.0 - introducing the recently released php7.2

0.9.27 - update nginx-1.13.7 and nodejs 8 lts (boron)

0.9.15 - add php-fpm

0.9.7 - update nginx-1.13.6, golang 1.9.2, and php7.1 stuff

0.9.6 - fix graph

0.9.4 - upgraded to latest nginx-1.13.5, .net core 2.0, and golang 1.9

0.9.0 - On Ubuntu 16.04, we've defaulted to php7.0 for some time, as it was the ubuntu default.  Since php7.1 are LTS for most php framework, it make sense to have it as the default.  As you know, this image support 3 different versions of php: 5.6, 7.0, and 7.1.  Default to php7.1 will help usher support for php7.2 as it become available later this year.

0.8.54 - add pagespeed and prep for next vesta release.  It has been completely redone in anticipation for next VestaCP release.  In order to upgrade to this image; please perform user backup, download of backup, and restore. It's the same step as you would expect to migrate another server: https://vestacp.com/docs/#how-to-migrate-user-to-another-server 

The docker image has been redone to keep all users IDs the same to simplify upgrade.  This means that, starting 0.8.52+, you can now simply upgrade the docker image when a new version is released.  

0.8.30 - first stable image

# MIT
