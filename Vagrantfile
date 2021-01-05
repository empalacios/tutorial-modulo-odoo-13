# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "debian/contrib-buster64"
  config.vm.network "forwarded_port", guest:8069, host:8069
  #config.vm.network "forwarded_port", guest:5432, host:5432
  config.vm.synced_folder "modulos", "/home/vagrant/modulos", create:true
  #config.vm.synced_folder "odoo", "/usr/lib/python3/dist-packages/odoo", create:true
  config.vm.provision "shell", inline: <<-SHELL
    adduser vagrant adm
    
    apt-get update

    ###########################################
    ###########################################
    ##        Instalación de Postgres        ##
    ###########################################
    ###########################################
    apt-get install -y postgresql

    # Configuracion postgres
    sudo -u postgres psql -c "ALTER ROLE postgres PASSWORD 'postgres';"
    sudo -u postgres psql -c "CREATE USER odoo WITH CREATEDB NOCREATEROLE PASSWORD 'odoo';"
    echo "host    all    all    0.0.0.0/0    trust" | sudo tee -a /etc/postgresql/11/main/pg_hba.conf
    echo "listen_addresses = '*'" | sudo tee -a /etc/postgresql/11/main/postgresql.conf
    service postgresql reload



    ###########################################
    ###########################################
    ##          Instalación de Odoo          ##
    ###########################################
    ###########################################
    # Dependencias de Odoo
    apt-get install -y python3-babel \
      python3-dateutil \
      python3-decorator \
      python3-docutils \
      python3-feedparser \
      python3-gevent \
      python3-html2text \
      python3-jinja2 \
      python3-libsass \
      python3-lxml \
      python3-mako \
      python3-mock \
      python3-ofxparse \
      python3-passlib \
      python3-polib \
      python3-psutil \
      python3-psycopg2 \
      python3-pydot \
      python3-pyparsing \
      python3-pypdf2 \
      python3-qrcode \
      python3-reportlab \
      python3-serial \
      python3-usb \
      python3-vatnumber \
      python3-vobject \
      python3-werkzeug \
      python3-xlsxwriter \
      python3-zeep \
      postgresql-client \
      python3-suds

    # Para impresion de facturas en PDF
    apt-get install -y libfontenc1 xfonts-75dpi xfonts-base xfonts-encodings xfonts-utils
    wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.buster_amd64.deb
    dpkg -i wkhtmltox_0.12.5-1.buster_amd64.deb

    # Para el importar/exportar archivos excel
    apt-get install -y python3-xlrd

    # Obtener el instalador de odoo
    odoo_executable_major_version=13
    odoo_executable_minor_version=0
    odoo_executable_date_released=20201003
    odoo_executable_type=_all
    odoo_executable=odoo_$odoo_executable_major_version.$odoo_executable_minor_version.$odoo_executable_date_released$odoo_executable_type.deb
    wget https://download.odoocdn.com/$odoo_executable_major_version.$odoo_executable_minor_version/nightly/deb/$odoo_executable
    dpkg -i $odoo_executable

    # Configurar directorio de nuevos modulos
    cp /vagrant/odoo.conf /etc/odoo/odoo.conf

    sudo service odoo restart

    adduser vagrant odoo
  SHELL
end

